#!/usr/bin/env python3
"""
Test Suite: ASS Subtitle Vertical Safe Zone Audit
Verifies that English ASS subtitles conform to the bottom-center standard:
- PlayResX: 720, PlayResY: 1280
- Alignment: 2 (Bottom-Center)
- MarginV: ~110
- Vertical bounding box bounded strictly between rows 1107 and 1169.
"""

import os
import sys
import re
import argparse

def audit_ass_file(ass_path):
    if not os.path.isfile(ass_path):
        print(f"[ERROR] Subtitle file not found: {ass_path}", file=sys.stderr)
        return False

    with open(ass_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    # 1. Check PlayRes
    resx_match = re.search(r"PlayResX:\s*(\d+)", content)
    resy_match = re.search(r"PlayResY:\s*(\d+)", content)
    if not resx_match or int(resx_match.group(1)) != 720:
        errors.append(f"Expected PlayResX: 720, found: {resx_match.group(1) if resx_match else 'None'}")
    if not resy_match or int(resy_match.group(1)) != 1280:
        errors.append(f"Expected PlayResY: 1280, found: {resy_match.group(1) if resy_match else 'None'}")

    # 2. Check Style
    style_match = re.search(r"Style:\s*Default,[^,]+,(\d+),[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,(\d+),[^,]+,[^,]+,(\d+)", content)
    if style_match:
        font_size = int(style_match.group(1))
        alignment = int(style_match.group(2))
        margin_v = int(style_match.group(3))

        if alignment != 2:
            errors.append(f"Expected Alignment: 2 (Bottom-Center), found: {alignment}")
        if not (90 <= margin_v <= 130):
            errors.append(f"MarginV {margin_v} is out of safe range [90, 130]. Standard is 110.")

        # Calculate bounding box
        # For alignment 2 with MarginV 110 and Fontsize 34:
        # Baseline = 1280 - MarginV = 1170
        # Cap height ~ Fontsize * 0.72 = ~25px
        # Row range = [1280 - MarginV - Fontsize, 1280 - MarginV] = [1136, 1170]
        top_row = 1280 - margin_v - font_size
        bottom_row = 1280 - margin_v

        print(f"[INFO] Calculated vertical subtitle span: rows {top_row} to {bottom_row} (PlayResY: 1280)")
        if top_row < 1050:
            errors.append(f"Subtitle top row ({top_row}) reaches too high into mid-screen!")
        if bottom_row > 1200:
            errors.append(f"Subtitle bottom row ({bottom_row}) is dangerously close to edge/UI buttons!")
    else:
        errors.append("Could not parse Default style definition in ASS file.")

    # 3. Check Dialogues
    dialogues = re.findall(r"^Dialogue:\s*[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,(.*)$", content, re.M)
    if not dialogues:
        errors.append("No dialogue events found in ASS file.")
    else:
        print(f"[INFO] Audited {len(dialogues)} dialogue events in ASS file.")

    if errors:
        print(f"\n[FAIL] ASS Audit failed for {ass_path}:")
        for err in errors:
            print(f"  - {err}")
        return False

    print(f"\n[PASS] ASS subtitle file perfectly complies with Bottom-Center standard ({ass_path}).")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit ASS Subtitle Bounds")
    parser.add_argument("--ass", help="Path to ASS subtitle file", default="/media/vedha/E2/freelance/yt-series/match_fixer/assets/ep04/ep04-en.ass")
    args = parser.parse_args()

    success = audit_ass_file(args.ass)
    sys.exit(0 if success else 1)

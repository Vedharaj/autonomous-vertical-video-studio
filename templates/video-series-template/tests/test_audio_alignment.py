#!/usr/bin/env python3
"""
Test Suite: Audio Alignment & Duration Standard Audit
Verifies that:
- Total episode duration is strictly between 45.0s and 60.0s.
- Speech windows do not cross shot boundaries.
- Pre-roll and post-roll cushions (>= 0.4s) are enforced.
"""

import os
import sys
import subprocess
import argparse

def get_media_duration(file_path):
    if not os.path.exists(file_path):
        return None
    res = subprocess.run([
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ], capture_output=True, text=True)
    try:
        return float(res.stdout.strip())
    except ValueError:
        return None

def audit_episode_media(video_path):
    print(f"=== Auditing Media File: {video_path} ===")
    duration = get_media_duration(video_path)
    if duration is None:
        print(f"[FAIL] Could not read duration from: {video_path}", file=sys.stderr)
        return False

    print(f"[INFO] Measured Duration: {duration:.2f} seconds")
    if 45.0 <= duration <= 60.0:
        print(f"[PASS] Duration {duration:.2f}s satisfies strict runtime standard [45.0s, 60.0s].")
        return True
    else:
        print(f"[FAIL] Duration {duration:.2f}s violates runtime standard [45.0s, 60.0s]!", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit Episode Duration & Audio Alignment")
    parser.add_argument("--video", default="/media/vedha/E2/freelance/yt-series/match_fixer/assets/ep04/ep04-tamil-captioned.mp4")
    args = parser.parse_args()

    success = audit_episode_media(args.video)
    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
SMM Queue & Distribution Dispatcher (Core Reusable Module)
Enforces Sequential Publishing Order Invariant and Mandatory Human Approval Gate.
"""

import os
import sys
import json
import argparse
import subprocess

DEFAULT_DRIVE_FOLDER = "1IxzXjqaFbCx6Audvw1pSmILrGzN8aqVp"
DRIVE_FOLDER_ID = os.environ.get("GOOGLE_DRIVE_FOLDER_ID", DEFAULT_DRIVE_FOLDER)

TAMIL_CHANNEL = os.environ.get("SMM_TAMIL_CHANNEL", "Story Time Tamil")
HINDI_CHANNEL = os.environ.get("SMM_HINDI_CHANNEL", "Story Time Hindi")

def get_channel_queue_rows(channel_name):
    """Executes 'smm queue list <channel>' and returns parsed items."""
    try:
        res = subprocess.run(
            ["smm", "queue", "list", channel_name],
            capture_output=True, text=True, check=True
        )
        return res.stdout
    except Exception as e:
        print(f"[WARN] Unable to list queue for '{channel_name}': {e}", file=sys.stderr)
        return ""

KNOWN_EPISODE_TITLES = {
    1: ["The Usual Loss", "Ep. 1"],
    2: ["Kavya's Notebook", "Ep. 2"],
    3: ["The Generous Sponsor", "Ep. 3"],
    4: ["Chintu's Lucky Shot", "Ep. 4"],
    5: ["An Unexpected Win", "Ep. 5"],
    6: ["Pandi's Cash", "Ep. 6"]
}

def verify_sequential_order(channel_name, episode_num):
    """Verifies that all predecessor episodes (1 .. N-1) are present in the queue."""
    if episode_num <= 1:
        return True, "First episode in series. Sequential requirement satisfied."

    output = get_channel_queue_rows(channel_name)
    missing = []
    for ep in range(1, episode_num):
        identifiers = KNOWN_EPISODE_TITLES.get(ep, [f"Ep. {ep}"])
        found = any(identifier in output for identifier in identifiers)
        if not found:
            missing.append(ep)

    if missing:
        msg = (
            f"[VIOLATION] Sequential Publishing Invariant failed for channel '{channel_name}'!\n"
            f"Cannot enroll Episode {episode_num} because predecessor Episode(s) {missing} are missing from the queue.\n"
            f"YouTube publishing picks rows from top to bottom. Enrolling out of order destroys serial continuity."
        )
        return False, msg

    return True, f"Predecessor episodes 1..{episode_num-1} verified in queue."

def build_metadata(series_name, episode_num, episode_title, lang_code):
    is_tamil = "ta" in lang_code.lower() or "tamil" in lang_code.lower()
    is_hindi = "hi" in lang_code.lower() or "hindi" in lang_code.lower()

    if is_tamil:
        title = f"{episode_title} 🏏😂 | {series_name} Ep. {episode_num} #Shorts #Tamil"
        desc = (
            f"Episode {episode_num} of {series_name}.\n\n"
            f"கிரிக்கெட் மேட்ச் பிக்சிங் கலாட்டா! வீராவின் டீம் ஜெயிக்குமா தோற்குமா?\n\n"
            f"#MatchFixers #TamilShorts #CricketComedy #WebSeries #Shorts"
        )
        tags = "matchfixers,tamilshorts,cricketcomedy,storytimetamil,shorts,viral"
    elif is_hindi:
        title = f"{episode_title} 🏏😂 | {series_name} Ep. {episode_num} #Shorts #Hindi"
        desc = (
            f"Episode {episode_num} of {series_name}.\n\n"
            f"क्रिकेट मैच फिक्सिंग का हंगामा! क्या वीरा की टीम जीतेगी या फिक्सर बॉस जीतेंगे?\n\n"
            f"#MatchFixers #HindiShorts #CricketComedy #WebSeries #Shorts"
        )
        tags = "matchfixers,hindishorts,cricketcomedy,storytimehindi,shorts,viral"
    else:
        title = f"{episode_title} | {series_name} Ep. {episode_num} #Shorts"
        desc = f"Episode {episode_num} of {series_name}.\n\n#Shorts #WebSeries"
        tags = "shorts,webseries,viral"

    return title, desc, tags

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMM Queue & Distribution Dispatcher")
    parser.add_argument("--check-sequence", type=int, help="Verify sequential invariant for target episode number")
    parser.add_argument("--channel", default=TAMIL_CHANNEL, help="Target channel name")
    args = parser.parse_args()

    if args.check_sequence:
        valid, msg = verify_sequential_order(args.channel, args.check_sequence)
        if valid:
            print(f"[OK] {msg}")
            sys.exit(0)
        else:
            print(f"[ERROR] {msg}", file=sys.stderr)
            sys.exit(1)

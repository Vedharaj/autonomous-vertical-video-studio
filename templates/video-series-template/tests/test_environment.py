#!/usr/bin/env python3
"""
Test Suite: Environment & Prerequisites Audit
Verifies Python dependencies, FFmpeg capabilities, directory layout, and API keys.
"""

import os
import sys
import shutil
import subprocess

def test_python_packages():
    print("[1/5] Checking Python packages...")
    required = ["requests", "numpy", "scipy"]
    missing = []
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"  [FAIL] Missing required Python packages: {missing}")
        return False
    print("  [PASS] All required Python packages installed (requests, numpy, scipy).")
    return True

def test_ffmpeg_capabilities():
    print("[2/5] Checking FFmpeg binary and libass / libx264 support...")
    ffmpeg_bin = shutil.which("ffmpeg")
    if not ffmpeg_bin:
        print("  [FAIL] ffmpeg binary not found in PATH.")
        return False

    res = subprocess.run([ffmpeg_bin, "-version"], capture_output=True, text=True)
    out = res.stdout.lower()
    has_libass = "enable-libass" in out or "libass" in out
    has_libx264 = "enable-libx264" in out or "libx264" in out

    if not has_libass:
        print("  [WARN] FFmpeg does not explicitly list libass in build configuration.")
    if not has_libx264:
        print("  [WARN] FFmpeg does not explicitly list libx264 in build configuration.")

    print(f"  [PASS] FFmpeg detected at {ffmpeg_bin}.")
    return True

def test_smm_cli():
    print("[3/5] Checking SMM CLI binary...")
    smm_bin = shutil.which("smm")
    if not smm_bin:
        print("  [WARN] 'smm' CLI not found in PATH. Social media queueing requires smm installed.")
        return True # Non-blocking for local generation
    print(f"  [PASS] 'smm' CLI found at {smm_bin}.")
    return True

def test_directory_layout():
    print("[4/5] Checking project-local directory structure...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    required_dirs = [
        "docs",
        "agents",
        ".agents/skills",
        ".agents/rules",
        "prompts",
        "config",
        "scripts/core",
        "tests",
        "assets/references"
    ]
    missing = []
    for d in required_dirs:
        path = os.path.join(base_dir, d)
        if not os.path.isdir(path):
            missing.append(d)

    if missing:
        print(f"  [FAIL] Missing project-local directories: {missing}")
        return False
    print("  [PASS] Complete project-local directory structure verified.")
    return True

def test_api_credentials():
    print("[5/5] Checking API credentials...")
    sarvam_key = os.environ.get("SARVAM_API_KEY")
    if not sarvam_key:
        print("  [INFO] SARVAM_API_KEY is not set in active shell. Load from config/.env when dubbing.")
    else:
        masked = sarvam_key[:6] + "..." + sarvam_key[-4:]
        print(f"  [PASS] SARVAM_API_KEY detected ({masked}).")
    return True

if __name__ == "__main__":
    print("=== Match Fixers: Environment Audit ===")
    results = [
        test_python_packages(),
        test_ffmpeg_capabilities(),
        test_smm_cli(),
        test_directory_layout(),
        test_api_credentials()
    ]
    if all(results):
        print("\n[ALL CHECKS PASSED] System is ready for video generation and dubbing.")
        sys.exit(0)
    else:
        print("\n[AUDIT FAILED] Resolve the errors above before continuing.", file=sys.stderr)
        sys.exit(1)

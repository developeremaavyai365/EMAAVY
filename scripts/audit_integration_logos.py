#!/usr/bin/env python3
"""Verify every integration has a local logo asset."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from integration_logos import LOGO_CATALOG, LOGO_DIR

missing = []
for slug, entry in LOGO_CATALOG.items():
    path = LOGO_DIR / entry["file"]
    if not path.exists():
        missing.append(f"{slug} -> {entry['file']}")

if missing:
    print("MISSING logos:")
    for m in missing:
        print(f"  - {m}")
    raise SystemExit(1)

print(f"OK: all {len(LOGO_CATALOG)} integration logos present in {LOGO_DIR}")

"""One-time helper script to copy the existing dynamic horse database.

This script copies data from the legacy ``hkjc_horses_dynamic.db`` file
to the new default ``hkjc_horses_dynamic_special.db`` file used by the
scraper.  Run it once if you already have data in the old database and
wish to retain it.

Usage:
    python copy_dynamic_db.py [--src OLD_DB] [--dst NEW_DB]
"""

import argparse
import os
import shutil

OLD_DB = "hkjc_horses_dynamic.db"
NEW_DB = "hkjc_horses_dynamic_special.db"

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the existing dynamic horse database to the new format."
    )
    parser.add_argument(
        "--src",
        default=OLD_DB,
        help=f"Source database (default: {OLD_DB})",
    )
    parser.add_argument(
        "--dst",
        default=NEW_DB,
        help=f"Destination database (default: {NEW_DB})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not os.path.exists(args.src):
        print(f"Source database '{args.src}' not found. Nothing to copy.")
        return

    if os.path.exists(args.dst):
        print(f"Destination database '{args.dst}' already exists. No action taken.")
        return

    shutil.copyfile(args.src, args.dst)
    print(f"Copied '{args.src}' to '{args.dst}'.")


if __name__ == "__main__":
    main()

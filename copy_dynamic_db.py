"""One-time helper script to copy the existing dynamic horse database.

This script copies data from the legacy ``hkjc_horses_dynamic.db`` file
to the new default ``hkjc_horses_dynamic_special.db`` file used by the
scraper.  Run it once if you already have data in the old database and
wish to retain it.

Usage:
    python copy_dynamic_db.py
"""

import os
import shutil

OLD_DB = "hkjc_horses_dynamic.db"
NEW_DB = "hkjc_horses_dynamic_special.db"


def main() -> None:
    if not os.path.exists(OLD_DB):
        print(f"Source database '{OLD_DB}' not found. Nothing to copy.")
        return

    if os.path.exists(NEW_DB):
        print(f"Destination database '{NEW_DB}' already exists. No action taken.")
        return

    shutil.copyfile(OLD_DB, NEW_DB)
    print(f"Copied '{OLD_DB}' to '{NEW_DB}'.")


if __name__ == "__main__":
    main()

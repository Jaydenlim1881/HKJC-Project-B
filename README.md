# HKJC-Project-B

Utilities for working with Hong Kong Jockey Club horse data.

## `copy_dynamic_db.py`

A one-time helper script that copies data from the legacy
`hkjc_horses_dynamic.db` file to the new default
`hkjc_horses_dynamic_special.db` file used by the scraper.

### Usage

```bash
python copy_dynamic_db.py [--src OLD_DB] [--dst NEW_DB]
```

#### Options

- `--src` Path to the source database. Defaults to `hkjc_horses_dynamic.db`.
- `--dst` Path to the destination database. Defaults to `hkjc_horses_dynamic_special.db`.

Run the script once if you already have data in the old database and wish to retain it.

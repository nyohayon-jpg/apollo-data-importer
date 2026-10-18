# apollo-data-importer

Nightly job that imports Greenleaf Grocers' CSV exports (products, stock, sales) into the Project Apollo database.

## How it works
1. Greenleaf IT drops CSVs on SFTP each night
2. Importer validates rows and keys products by `(store_id, product_id)`
3. Data is upserted into the apollo-api database

## Team
Priya Shah (owner), Maya Cohen (backend). Client contact: Sarah Kim.

## Run
```bash
python import.py --date YYYY-MM-DD
```

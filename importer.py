"""Nightly Greenleaf CSV importer."""
import csv


def product_key(row):
    # product_id is only unique within a store, so key by both
    return (row["store_id"], row["product_id"])


def load_products(path):
    products = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            products[product_key(row)] = row
    return products

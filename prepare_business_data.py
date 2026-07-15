"""Convert Yelp business JSON (one JSON object per line) into a clean CSV for Power BI."""
import json, csv

SRC = r"C:\Users\kyled\Desktop\yelp_dataset\yelp_academic_dataset_business.json"
OUT = r"C:\Users\kyled\Desktop\business_data.csv"

rows = 0
with open(SRC, encoding="utf-8") as f, open(OUT, "w", newline="", encoding="utf-8-sig") as o:
    w = csv.writer(o)
    w.writerow(["business_id", "name", "city", "state", "stars", "review_count",
                "status", "price_range", "primary_category", "latitude", "longitude"])
    for line in f:
        b = json.loads(line)
        attrs = b.get("attributes") or {}
        price = attrs.get("RestaurantsPriceRange2") or ""
        if price in ("None", "null"):
            price = ""
        cats = b.get("categories") or ""
        primary = cats.split(",")[0].strip() if cats else ""
        w.writerow([
            b["business_id"], b["name"], b["city"], b["state"],
            b["stars"], b["review_count"],
            "Open" if b.get("is_open") == 1 else "Closed",
            price, primary, b["latitude"], b["longitude"],
        ])
        rows += 1

print(f"Wrote {rows} businesses to {OUT}")

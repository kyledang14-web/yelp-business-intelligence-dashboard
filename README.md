# Yelp Business Intelligence Dashboard

---

## Dashboard Previews

**Summary Page**

![Summary page](summary_page.png)

**Activity Page**

![Activity page](activity_page.png)

---

## Overview

**Objective:**
Analyze the Yelp Open Dataset to understand where business activity concentrates geographically and how customer ratings relate to review volume, supporting market-entry and advertising decisions.

This project transforms 150K+ raw business records (JSON) into a clean analytical dataset and a 2-page interactive Power BI dashboard covering 7M+ customer reviews across 27 states and 1,000+ cities.

The work includes data extraction and cleaning, data modeling, DAX measure development, and interactive dashboard design.

---

## Tools Used

* Python (JSON parsing, data cleaning, feature extraction)
* Power BI (data modeling, DAX measures, interactive visuals, Top N filtering)

---

## Data Pipeline

1. **Extract & clean** — `prepare_business_data.py` parses the raw Yelp JSON (one object per line), extracts business attributes (price range, primary category, open/closed status), and outputs a clean 150,346-row CSV
2. **Model** — single detail table powers every visual, enabling instant cross-filtering across all pages (replaced static pre-aggregated tables that could not respond to slicers)
3. **Measures** — 7 DAX measures including Total Reviews, Total Businesses, States/Cities Represented, Average Rating, and threshold counts (500+ reviews, 4.5+ stars)
4. **Visualize** — 2-page dashboard with KPI cards, slicers, Top N geographic map, and ranked bar charts

---

## Dashboard Pages

**Summary** — portfolio-wide health: KPI cards, rating distribution, ratings vs. popularity scatter, top states by high-rated businesses, and top advertising opportunity businesses, filterable by state, city, and review-volume bucket

**Activity** — geographic engagement: KPI cards (7M+ reviews, 150K+ businesses), a Top 10 States by Yelp Activity map, and a Top Cities by Yelp Activity ranking

---

## Key Insights

* Yelp engagement is highly concentrated: the top 10 states account for the large majority of total review volume, led by Pennsylvania
* Philadelphia generates the most review activity of any city, ahead of New Orleans and Nashville
* Most businesses cluster between 3.5 and 4.5 stars — high review volume does not imply high ratings, and standout businesses (4.5+ stars with 500+ reviews) are a small identifiable segment
* Review volume is heavily skewed: the majority of businesses have fewer than 50 reviews, while a small group exceeds 1,000

---

## Files Included

* `yelp_business_dashboard.pbix` → Interactive Power BI dashboard (2 pages)
* `business_data.csv` → Cleaned dataset (150,346 businesses)
* `prepare_business_data.py` → Python script that converts the raw Yelp JSON into the clean CSV
* `summary_page.png` / `activity_page.png` → Dashboard screenshots

---

## Business Impact

* Identified the highest-activity states and cities to prioritize market entry and regional advertising spend
* Isolated high-rating, high-volume businesses as prime advertising partners
* Quantified the gap between popularity and quality, supporting more targeted business development than raw review counts alone
* Established a reusable pipeline: refreshing the dashboard with a new Yelp data drop only requires re-running one script

---

## Data Source

[Yelp Open Dataset](https://www.yelp.com/dataset) — business metadata subset

# Yelp Business Intelligence Dashboard

Built to answer a business question, not just to visualize data.

---

## Scenario — The Business Ask

To simulate how this work happens on a real team, I framed the project around a business scenario instead of building charts for their own sake.

**The situation:** A team that advertises and partners with local businesses is deciding where to focus next year. They have 150K+ businesses and 7M+ Yelp reviews sitting in a raw table — and no way to read it before a leadership meeting.

**The questions I set out to answer:**
1. **Where is activity concentrated?** Which states and cities dominate by business count and review volume — so we don't spread thin across 27 states?
2. **Are the biggest markets also the best?** Leadership assumes "more businesses = better market." Is that actually true, or do the highest-*rated* markets differ from the highest-*volume* ones?
3. **What does overall quality look like?** One view of the ratings spread across the whole marketplace.
4. **Where are the standout businesses?** For a premium-partner program, which states hold the most 4.5★+ businesses?
5. **Can it be sliced live?** Filter by state, city, and review volume on the spot, with every KPI recomputing.

I built a 2-page Power BI dashboard that answers all five.

---

## Dashboard Previews

**Summary Page**

![Summary page](summary_page.png)

**Activity Page**

![Activity page](activity_page.png)

---

## Overview

**Objective:**
Answer the business questions above using the Yelp Open Dataset — where activity concentrates, how ratings relate to volume, and which markets to prioritize — and package it so a non-technical stakeholder can explore it in a meeting.

This project analyzes 150K+ businesses and 7M+ customer reviews across 27 states and 1,000+ cities, combining SQL analysis with a 2-page interactive Power BI dashboard.

The work includes SQL data exploration and quality checks, data modeling, DAX measure development, and interactive dashboard design.

---

## Tools Used

* SQL (joins, aggregations, filtering, data quality checks — nulls, duplicates, invalid values)
* Power BI (data modeling, DAX measures, calculated columns, interactive visuals, Top N filtering)

---

## Data Pipeline
Raw Yelp Dataset

1.SQL Data Exploration & Validation
2.Data Cleaning & Quality Checks
3.Power BI Data Model
4.DAX Measures & Calculated Columns
5.Interactive Dashboard
6.Business Insights

---

## Workflow

1. **Explore & validate** — SQL queries against the Yelp business data: joins, aggregations, and filtering to profile the dataset, plus quality checks for nulls, duplicates, and invalid values
2. **Model** — a single 150,346-row detail table powers every visual, enabling instant cross-filtering across all pages (replaced static pre-aggregated tables that could not respond to slicers)
3. **Measures** — 7 DAX measures including Total Reviews, Total Businesses, States/Cities Represented, Average Rating, and threshold counts (500+ reviews, 4.5+ stars), plus calculated columns bucketing businesses by review volume
4. **Visualize** — a 2-page Power BI dashboard: KPI cards, a Top-N geographic map, ranked bar charts, and a ratings-vs-popularity scatter, all filterable by state, city, and review-volume bucket

---

## Dashboard Pages

**Summary** — portfolio-wide health: KPI cards, rating distribution, ratings vs. popularity scatter, top states by high-rated businesses, and top advertising opportunity businesses, filterable by state, city, and review-volume bucket

**Activity** — geographic engagement: KPI cards (7M+ reviews, 150K+ businesses), a Top 10 States by Yelp Activity map, and a Top Cities by Yelp Activity ranking

---

## Key Findings (Answering the Questions)

* **Q1 — Where's the activity?** Highly concentrated: Pennsylvania (34K businesses) and Florida (26K) dominate, and the top 10 states hold the large majority of all review volume. Philadelphia is the single most active city.
* **Q2 — Biggest = best? No.** California posts the **highest average rating (4.0★) with only ~5,200 businesses**, while Pennsylvania — the largest market by count — sits at a middling 3.57★. The biggest markets are not the highest-rated. *(This reframed the "more businesses = better market" assumption.)*
* **Q3 — Overall quality?** Ratings cluster between 3.5 and 4.5 stars and skew positive; very few businesses sit below 2★ — a bias worth naming rather than taking the 3.6★ average at face value.
* **Q4 — Standout businesses?** 4.5★+ businesses concentrate in PA and FL; the truly standout segment (4.5★+ with 500+ reviews) is small and clearly identifiable for targeting.
* **Q5 — Live slicing?** Every KPI and visual recomputes by state, city, and review-volume bucket, so questions like "what about just Florida?" are answered in the room.

---

## Files Included

* `yelp_business_dashboard.pbix` → Interactive Power BI dashboard (2 pages)
* `business_data.csv` → Cleaned dataset (150,346 businesses)
* `summary_page.png` / `activity_page.png` → Dashboard screenshots

---

## Business Impact

* Found the states and cities with the most Yelp activity — useful for deciding where to focus regionally
* Flagged businesses with both high ratings and high review volume as the strongest advertising targets
* Showed that review volume alone doesn't equal satisfaction — a heavily-reviewed business can still rate poorly
* Built the whole analysis on 150K+ real business records, filterable by state, city, and review-volume bucket

---

## Data Source

[Yelp Open Dataset](https://www.yelp.com/dataset) — business metadata subset

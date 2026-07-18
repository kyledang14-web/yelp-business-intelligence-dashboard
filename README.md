# Yelp Business Intelligence Dashboard

Built to answer a business question, not just to visualize data.

---

## Scenario — The Business Ask

To simulate how this work actually lands on an analyst's desk, I framed the project around a realistic, open-ended request instead of building charts for their own sake.

**The brief, the way a manager would give it:**

> "Build me a dashboard so I can actually see what's going on with the businesses on our platform. Right now, if leadership asks me how they're doing, where our strong markets are, or who our top businesses are, I've got nothing but a giant table. I want something I can pull up in a meeting and dig into myself — without coming to you every time."

No chart specs, no metrics named — just a goal and a frustration. Turning that vague ask into the right views was the job.

**What I translated it into:**
* **Scale & quality at a glance** — KPI cards for total businesses, reviews, states, cities, and average rating
* **Where the activity is** — top states and cities by review volume
* **Overall quality** — the ratings distribution across the whole marketplace
* **The standout businesses** — highly rated, high-volume targets, plus which states hold the most 4.5★+ businesses
* **Self-service** — slicers for state, city, and review volume so the stakeholder answers their own follow-ups

The result is a 2-page Power BI dashboard the stakeholder can read and explore on their own.

---

## Dashboard Previews

**Summary Page**

![Summary page](summary_page.png)

**Activity Page**

![Activity page](activity_page.png)

---

## Overview

**Objective:**
Turn an open-ended "help me see what's going on" request into a dashboard a non-technical stakeholder can read and explore on their own — using the Yelp Open Dataset to show where activity concentrates, how ratings relate to volume, and which businesses stand out.

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

## Key Findings

* **Activity is concentrated.** Pennsylvania (34K businesses) and Florida (26K) dominate, and the top 10 states hold the large majority of all review volume. Philadelphia is the single most active city.
* **The biggest markets aren't the best.** California posts the **highest average rating (4.0★) with only ~5,200 businesses**, while Pennsylvania — the largest market by count — sits at a middling 3.57★. Bigger ≠ better-rated.
* **Overall quality skews positive.** Ratings cluster between 3.5 and 4.5 stars; very few businesses sit below 2★ — a bias worth naming rather than taking the 3.6★ average at face value.
* **Standout businesses are a small, findable segment.** 4.5★+ businesses concentrate in PA and FL, and the truly standout group (4.5★+ with 500+ reviews) is small and clearly identifiable for targeting.
* **Everything is self-service.** Every KPI and visual recomputes by state, city, and review-volume bucket, so follow-ups like "what about just Florida?" are answered on the spot.

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

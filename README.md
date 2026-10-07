# CodeAlpha Task 3: Data Visualization (Jumia Skincare Market)

## What this project does
Visualizes the findings from Task 2's EDA on Jumia Nigeria's skincare market, pricing, brand concentration, and the relationship between price, discounts, and customer trust.

## Data source
`jumia_skincare.csv`, the 159-product skincare dataset built in Task 1 (CodeAlpha_WebScraping).

## Tools used
- Python
- pandas
- Matplotlib
- Seaborn

## Charts

### 1. Price Distribution
Most skincare products are priced under ₦15,000, with a long tail of a few premium products reaching up to ₦51,000. Confirms the market is right-skewed, median is a better "typical price" than the mean.

### 2. Top 10 Brands by Product Count
NIVEA (33) and Dettol (27) dominate the catalog, together over a third of all skincare products listed.

### 3. Price vs Rating
A scatterplot of all 159 products shows ratings clustering between 4 and 5 regardless of price, visual confirmation of the weak correlation (0.15) found in Task 2. A handful of low-rated outliers appear mostly at lower price points.

### 4. Discounted vs Full-Price: Rating & Review Count
Full-price products average a higher rating (4.23 vs 3.93) but fewer reviews (360 vs 691) than discounted ones. Discounts appear to drive purchase volume, not necessarily satisfaction.

### 5. Average Price by Top 5 Brands
NIVEA prices nearly 3x higher than Dettol, Vaseline, Generic, and Eva Soap, a clear premium positioning in this market.

## Files
- `visualize.py`: script that generates all charts
- `jumia_skincare.csv`: the dataset
- `chart1_price_distribution.png`
- `chart2_top_brands.png`
- `chart3_price_vs_rating.png`
- `chart4_discount_comparison.png`
- `chart5_avg_price_by_brand.png`
- `README.md`: this file
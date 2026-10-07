import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---- Load data ----
folder = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(folder, "jumia_skincare.csv"))

# recreate the discount_pct column from Task 2
df["discount_pct"] = (
    df["discount"].str.extract(r"(-?\d+)%")[0].astype(float).abs()
)

sns.set_style("whitegrid")

# ---- Chart 1: Price distribution ----
plt.figure(figsize=(8, 5))
sns.histplot(df["price"], bins=20, kde=True, color="teal")
plt.title("Price Distribution of Skincare Products on Jumia")
plt.xlabel("Price (₦)")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig(os.path.join(folder, "chart1_price_distribution.png"))
plt.close()

# ---- Chart 2: Top 10 brands by product count ----
top10 = df["brand"].value_counts().head(10)
plt.figure(figsize=(8, 5))
sns.barplot(x=top10.values, y=top10.index, hue=top10.index, palette="viridis", legend=False)
plt.title("Top 10 Brands by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig(os.path.join(folder, "chart2_top_brands.png"))
plt.close()

# ---- Chart 3: Price vs Rating scatterplot ----
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="price", y="rating", alpha=0.6, color="darkorange")
plt.title("Price vs Rating (Correlation: 0.15, weak)")
plt.xlabel("Price (₦)")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig(os.path.join(folder, "chart3_price_vs_rating.png"))
plt.close()

# ---- Chart 4: Discounted vs Not — rating & review count ----
df["is_discounted"] = df["discount_pct"].notna().map({True: "Discounted", False: "Full Price"})
summary = df.groupby("is_discounted")[["rating", "review_count"]].mean().reset_index()

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
sns.barplot(data=summary, x="is_discounted", y="rating", hue="is_discounted", palette="pastel", legend=False, ax=axes[0])
axes[0].set_title("Avg Rating: Discounted vs Full Price")
axes[0].set_xlabel("")
sns.barplot(data=summary, x="is_discounted", y="review_count", hue="is_discounted", palette="pastel", legend=False, ax=axes[1])
axes[1].set_title("Avg Review Count: Discounted vs Full Price")
axes[1].set_xlabel("")
plt.tight_layout()
plt.savefig(os.path.join(folder, "chart4_discount_comparison.png"))
plt.close()

# ---- Chart 5: Avg price by top 5 brand ----
top5_brands = df["brand"].value_counts().head(5).index
avg_price = df[df["brand"].isin(top5_brands)].groupby("brand")["price"].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_price.values, y=avg_price.index, hue=avg_price.index, palette="mako", legend=False)
plt.title("Average Price by Top 5 Brands")
plt.xlabel("Average Price (₦)")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig(os.path.join(folder, "chart5_avg_price_by_brand.png"))
plt.close()

print("All 5 charts saved successfully!")
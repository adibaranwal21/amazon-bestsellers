# Amazon Bestsellers Analysis (2009–2019)

This project analyzes the **Top 50 Amazon Bestsellers** from **2009 to 2019**, exploring trends in authors, genres, and book ratings over an 11-year span.

## 📌 Project Overview

The dataset contains annual bestseller information including title, author, user ratings, price, and genre. Two main analyses were conducted:

1. **Top Authors Analysis**

   * Identifies the authors who appeared most frequently in bestseller lists across the decade.
   * Outputs the results into a CSV file: `top_authors.csv`.

2. **Ratings by Genre Analysis**

   * Computes and compares the average user ratings for each book genre over the 11-year period.
   * Outputs the results into a CSV file: `avg_rating_by_genre.csv`.

## 📁 Files in This Repository

* **`top_authors.csv`** – List of authors with the highest number of bestselling books between 2009 and 2019.
* **`avg_rating_by_genre.csv`** – Average user rating for each genre based on bestseller data.
* **`README.md`** – Documentation for the project.

## 🔧 Methods & Tools

* **Python** (Pandas, NumPy)
* **Data cleaning**: handling duplicates, adjusting data types, organizing authors and genres
* **Data aggregation**: grouping by author and genre, computing averages and counts

## 📊 Key Insights

* Frequent bestseller authors tend to consistently write within the same genre.
* Certain genres maintain higher user ratings across the decade.
* Bestseller trends shift over time, but some authors dominate multiple years.

## 🚀 How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/amazon-bestsellers-analysis.git
   ```
2. Open the analysis notebook or script to review or extend the analysis.
3. Use the CSV files for further data exploration or visualization.

## 🤝 Contributing

Feel free to open issues or submit pull requests if you'd like to extend the analysis or add new visualizations.

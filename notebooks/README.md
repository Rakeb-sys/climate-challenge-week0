# African Climate Trends EDA (Pre-COP32)

This directory contains the Exploratory Data Analysis (EDA) and data cleaning pipeline for climate datasets across various African countries suchas Ethiopia, Kenya, Nigeria, Sudan and Tanzania. The goal is to transform raw NASA POWER meteorological data into high-quality, analysis-ready datasets to identify regional climate trends.

## 📋 Project Scope
- **Target Period:** 2015 – 2026
- **Objective:** Profile climate variables including Temperature (T2M), Precipitation (PRECTOTCORR), Humidity (RH2M), and Wind Speed (WS2M).
- **Goal:** Provide evidence-based insights into seasonal shifts and extreme weather anomalies in the lead-up to COP32.

## 🛠️ Data Cleaning Pipeline
To ensure scientific accuracy, the following steps are performed in the `<country>_eda.ipynb` notebooks:

1.  **Temporal Alignment:** Converts `YEAR` and `DOY` (Day of Year) into standard datetime objects.
2.  **Sentinel Handling:** Replaces NASA's `-999` placeholder values with `NaN` to prevent statistical skew.
3.  **Deduplication:** Removal of redundant rows to ensure data integrity.
4.  **Outlier Management:** Detection of anomalies using Z-scores ($|Z| > 3$). Outliers are reviewed and handled (dropped/capped) based on their physical plausibility.
5.  **Imputation:** Missing values are addressed using forward-fill for continuous weather patterns or row-deletion for highly sparse data (>30% missing).

## 📊 Key Visualizations & Analysis
The analysis focuses on three core areas:
- **Time Series:** Tracking monthly temperature averages and precipitation totals to identify peak rainy seasons and warming trends.
- **Correlations:** Heatmaps and scatter plots (e.g., T2M vs. RH2M) to understand the relationship between heat, moisture, and wind dynamics.
- **Distributions:** Bubble charts and log-scaled histograms to visualize the frequency and intensity of rainfall events.

## 📁 Repository Structure
- `notebooks/<country>_eda.ipynb`: Individual country analysis notebooks.
- `data/<country>_clean.csv`: Cleaned output files (Note: Excluded from version control via `.gitignore`).

## 📚 References & Resources
- [NASA POWER Data Documentation](https://nasa.gov)
- [Pandas Documentation: Time Series/Date handling](https://pydata.org)
- [Conventional Commits Specification](https://conventionalcommits.org)

📊 KAIM - Climate Data Analysis Project

📌 Overview

This project is designed for scalable Python-based climate data analysis, combining data cleaning, exploratory data analysis (EDA), and reproducible workflows.

It includes:

Structured source code (src/)
Interactive analysis via notebooks (notebooks/)
Automated testing (tests/)
Utility scripts (scripts/)
CI/CD integration via GitHub Actions

The goal is to analyze weather variables such as temperature, precipitation, humidity, and wind speed, and extract meaningful insights through statistical and visual analysis.

🗂️ Project Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml     # CI pipeline for running tests
├── .gitignore
├── requirements.txt
├── README.md
├── src/                      # Core Python modules (data processing, utilities)
├── notebooks/                # Jupyter notebooks for EDA and experiments
│   ├── __init__.py
│   └── README.md
├── tests/                    # Unit tests
│   └── __init__.py
└── scripts/                  # Helper scripts (data processing, automation)
    ├── __init__.py
    └── README.md

⚙️ Setup Instructions
1. Create and activate a virtual environment
python -m venv .venv
Windows
.venv\Scripts\activate
Linux / macOS
source .venv/bin/activate
2. Install dependencies
pip install -r requirements.txt

📊 Exploratory Data Analysis (EDA)
🔹 How to Run
Start Jupyter Notebook:
jupyter notebook
Navigate to:
notebooks/
Open the EDA notebook (e.g., eda.ipynb) and run all cells.
🔹 Analysis Workflow

The EDA follows a structured pipeline:

1. Data Cleaning
Outlier detection using Z-scores
Outlier handling via capping (±3 standard deviations)
Missing value handling:
Drop rows with >30% missing values
Forward-fill remaining gaps (time-series appropriate)

2. Feature Engineering
Creation of derived variables (e.g., T2M_RANGE)
Conversion of date column to datetime
Monthly aggregation of:
Temperature → mean
Precipitation → sum

3. Time Series Analysis
Monthly average temperature trends (2015–2026)
Monthly total precipitation
Identification of:
Warmest and coolest months
Peak rainy seasons

4. Correlation Analysis
Heatmap of numeric variables
Identification of strongest relationships
Scatter plots:
Temperature vs Humidity
Temperature range vs Wind speed

5. Distribution Analysis
Histogram of precipitation (log-scaled if skewed)
Bubble chart:
Temperature vs Humidity
Bubble size = precipitation

📁 Outputs

Generated outputs are organized as follows:

📌 Cleaned Data
data/<country>_clean.csv

⚠️ The data/ directory is excluded from version control via .gitignore.

📊 Visualizations

Stored (optionally) in:

reports/figures/
📝 Reports

Analysis summaries can be stored in(not currently available):

reports/
🧪 Running Tests

Run unit tests with:

pytest

Tests are automatically executed in CI via:

.github/workflows/unittests.yml

🤖 Automation Scripts

Scripts in scripts/ can be used for:

Data preprocessing
Batch execution of analysis
Pipeline automation

Run a script:

python scripts/<script_name>.py

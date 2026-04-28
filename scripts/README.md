Streamlit Dashboard

🔧 Setup
git checkout -b dashboard-dev
pip install -r requirements.txt
streamlit run app/main.py

🌍 Features
Country multi-select filter
Year range slider
Variable selector (T2M, PRECTOTCORR, RH2M)
Temperature trend visualization
Precipitation distribution boxplot

📦 Data
Dashboard reads local CSV files from:
../../dataset/<country>_clean.csv
Data is excluded via .gitignore

☁️ Deployment
Push repo to GitHub
Go to Streamlit Community Cloud
Select repo → set app/main.py as entry point
Deploy

✅ Git Requirements
git checkout -b dashboard-dev
git add .
git commit -m "feat: basic Streamlit UI"
git push origin dashboard-dev
import sys
import os

sys.path.append(os.path.dirname(__file__))

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, filter_data, monthly_temperature

st.set_page_config(page_title="Climate Dashboard", layout="wide")

# Title
st.title("🌍 African Climate Insights Dashboard")
st.markdown("Interactive exploration of climate trends across selected African countries")

# Sidebar Controls
st.sidebar.header("Filters")

countries = ['ethiopia', 'sudan', 'kenya', 'nigeria', 'tanzania']

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=countries
)

year_range = st.sidebar.slider(
    "Select Year Range",
    2015,
    2026,
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ['T2M', 'PRECTOTCORR', 'RH2M']
)

# Load Data
df = load_data(countries, base_path="../dataset/")

if df.empty:
    st.warning("No data found. Ensure CSV files exist in dataset/ directory.")
    st.stop()

# Filter Data
df_filtered = filter_data(df, [c.capitalize() for c in selected_countries], year_range)

# Layout
col1, col2 = st.columns(2)

# 🌡️ Temperature Trend
with col1:
    st.subheader("🌡️ Monthly Temperature Trend")

    temp_df = monthly_temperature(df_filtered)

    fig, ax = plt.subplots(figsize=(8,4))

    for country in temp_df['Country'].unique():
        subset = temp_df[temp_df['Country'] == country]
        ax.plot(subset['Date'], subset['T2M'], label=country)

    ax.set_title("Temperature Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("T2M")
    ax.legend()

    st.pyplot(fig)

# 🌧️ Precipitation Distribution
with col2:
    st.subheader("🌧️ Precipitation Distribution")

    fig2, ax2 = plt.subplots(figsize=(8,4))

    sns.boxplot(
        data=df_filtered,
        x='Country',
        y='PRECTOTCORR',
        ax=ax2
    )

    ax2.set_title("Rainfall Distribution by Country")

    st.pyplot(fig2)

# 📊 Variable Visualization
st.subheader(f"📊 {variable} Trend")

fig3, ax3 = plt.subplots(figsize=(10,4))

for country in df_filtered['Country'].unique():
    subset = df_filtered[df_filtered['Country'] == country]
    ax3.plot(subset['Date'], subset[variable], label=country)

ax3.set_title(f"{variable} Over Time")
ax3.legend()

st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | Climate Data Analysis Project")
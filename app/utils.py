import pandas as pd
import os


def load_data(countries, base_path="../dataset/"):
    dfs = []

    for c in countries:
        file_path = os.path.join(base_path, f"{c}_clean.csv")

        try:
            df = pd.read_csv(file_path)
            df["Country"] = c.capitalize()
            dfs.append(df)

        except FileNotFoundError:
            print(f"Missing file: {file_path}")
            continue

    if not dfs:
        return pd.DataFrame()

    df_all = pd.concat(dfs, ignore_index=True)

    df_all.columns = df_all.columns.str.strip()

    if "Date" in df_all.columns:
        df_all["Date"] = pd.to_datetime(df_all["Date"])
        df_all["Year"] = df_all["Date"].dt.year

    return df_all


def filter_data(df, selected_countries, year_range):
    return df[
        (df["Country"].isin(selected_countries)) &
        (df["Year"] >= year_range[0]) &
        (df["Year"] <= year_range[1])
    ]


def monthly_temperature(df):
    return (
        df.set_index("Date")
        .groupby("Country")
        .resample("ME")["T2M"]
        .mean()
        .reset_index()
    )
# This script cleans messy sales data and saves a cleaned version
# for analysis and reporting purposes.

import pandas as pd


# Load the CSV file into a pandas DataFrame
# This function reads the raw sales data file.
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df


# Standardize column names
# This makes column names easier to work with in Python.
def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


# Handle missing values in price and quantity columns
# Missing values can cause problems during analysis.
def handle_missing_values(df):

    if "price" in df.columns:
        df["price"] = df["price"].fillna(0)

    if "quantity" in df.columns:
        df["quantity"] = df["quantity"].fillna(0)

    return df


# Remove invalid rows with negative values
# Negative prices and quantities are likely data entry errors.
def remove_invalid_rows(df):

    if "price" in df.columns:
        df = df[df["price"] >= 0]

    if "quantity" in df.columns:
        df = df[df["quantity"] >= 0]

    return df


# Remove extra whitespace from text columns
# This keeps product names and categories consistent.
def strip_whitespace(df):

    text_columns = ["product_name", "category"]

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    return df


if __name__ == "__main__":

    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)

    df_clean = clean_column_names(df_raw)
    df_clean = strip_whitespace(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
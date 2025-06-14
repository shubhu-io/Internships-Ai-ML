#Clean_Preprocess_Dataset_AIML
#!/usr/bin/env python3
"""
Clean & preprocess CSV for ML-ready🪄
import argparse
import warnings
import os
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")


def load_data(path: str) -> pd.DataFrame:
    """Load CSV file into DataFrame."""
    df = pd.read_csv(path)
    print(f"📦 Loaded {df.shape[0]} rows × {df.shape[1]} columns")
    print(df.head())
    print(df.info())
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Drop exact duplicate rows."""
    before = df.shape[0]
    df = df.drop_duplicates()
    print(f"🧹 Removed {before - df.shape[0]} duplicate rows")
    return df


def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert object columns that can be numeric to numeric."""
    obj_cols = df.select_dtypes(include=["object"]).columns
    for col in obj_cols:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    return df


def impute_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Impute NaNs: median for numeric, mode for categorical."""
    num_cols = df.select_dtypes(include=["number"]).columns
    cat_cols = df.select_dtypes(exclude=["number"]).columns

    for col in num_cols:
        if df[col].isna().any():
            median = df[col].median()
            df[col].fillna(median, inplace=True)
            print(f"🔧 Filled NaNs in numeric {col} with median {median}")

    for col in cat_cols:
        if df[col].isna().any():
            mode = df[col].mode().iat[0]
            df[col].fillna(mode, inplace=True)
            print(f"🔧 Filled NaNs in categorical {col} with mode '{mode}'")
    return df


def transform_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Log‑transform skewed numerics & standard‑scale all numerics."""
    num_cols = df.select_dtypes(include=["number"]).columns
    skewness = df[num_cols].skew().abs()
    skewed_cols = skewness[skewness > 2].index
    if skewed_cols.any():
        df[skewed_cols] = np.log1p(df[skewed_cols])
        print(f"🚀 Applied log1p to {len(skewed_cols)} skewed numeric column(s): {list(skewed_cols)}")

    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    print("📏 Standard‑scaled numeric features")
    return df


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """One‑hot encode categorical columns (drop first)."""
    cat_cols = df.select_dtypes(exclude=["number"]).columns
    if len(cat_cols):
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
        print(f"🎨 One‑hot encoded {len(cat_cols)} categorical column(s): {list(cat_cols)}")
    return df


def save_data(df: pd.DataFrame, out_path: str) -> None:
    """Save DataFrame to CSV without index."""
    df.to_csv(out_path, index=False)
    print(f"✅ Cleaned data saved to {out_path}")


def preprocess(path_in: str, path_out: str) -> None:
    df = load_data(path_in)
    df = drop_duplicates(df)
    df = convert_types(df)
    df = impute_missing(df)
    df = transform_numeric(df)
    df = encode_categorical(df)
    save_data(df, path_out)


def main():
    parser = argparse.ArgumentParser(
        description="Clean & preprocess CSV for ML‑ready vibes 🪄",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--input", required=True, help="Path to raw CSV file")
    parser.add_argument("--output", help="Path to save cleaned CSV (default adds _cleaned)")
    args = parser.parse_args()

    # Derive default output path if not provided
    if args.output is None:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_cleaned{ext}"

    preprocess(args.input, args.output)


if __name__ == "__main__":
    main()

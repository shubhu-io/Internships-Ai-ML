Clean_Preprocess_Dataset_AIML.py

Quick‑fire data‑cleanup pipeline for Netflix/ IPL or any spicy CSV you toss at it.

Usage:
    python Clean_Preprocess_Dataset_AIML.py --input raw_data.csv --output cleaned_data.csv

Steps handled
-------------
1. Load dataset with pandas.
2. Peek at shape & dtypes.
3. Drop duplicate rows.
4. Auto‑convert numeric‑looking object columns to proper numerics.
5. Impute missing values:
   • numeric → median
   • categorical → mode
6. Nuke extreme skew (>2) with log1p transform.
7. Standard‑scale all numeric columns.
8. One‑hot encode categoricals (drop_first to dodge dummy trap).
9. Save the cleaned DataFrame to CSV.

Feel free to remix/improve — it’s your data party!
"""

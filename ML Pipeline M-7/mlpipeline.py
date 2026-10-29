# ML Pipeline - load ecommerce dataset (xlsx) from Google Drive with pandas
#
# Setup (once):
#   py -m pip install pandas openpyxl gdown
#
# Google Drive e file ta share korun: Share -> General access -> "Anyone with the link"
# Tarpor link ta niche DRIVE_URL e paste korun.

import os

import gdown
import pandas as pd

# Google Drive share link, e.g.
# https://drive.google.com/file/d/<FILE_ID>/view?usp=sharing
DRIVE_URL = "PASTE_YOUR_GOOGLE_DRIVE_LINK_HERE"
FILE_PATH = "ecommerce_dataset_updated.xlsx"


def load_data(url=DRIVE_URL, path=FILE_PATH):
    # Download from Drive only if the file isn't already here
    if not os.path.exists(path):
        gdown.download(url, path, quiet=False, fuzzy=True)
    return pd.read_excel(path, sheet_name=0)


if __name__ == "__main__":
    df = load_data()

    print("Shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nInfo:")
    df.info()
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nSummary statistics:")
    print(df.describe())

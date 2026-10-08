"""
Unemployment in India - Data Preparation & Preprocessing Pipeline
=================================================================
Role: Data Cleaning and Preprocessing (Maharudra)
Dataset Source: https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india
"""

import sys
import logging
import shutil
from pathlib import Path
from typing import Dict, Tuple, Any
import pandas as pd
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("DataPreparationPipeline")


def preserve_raw_dataset(source_path: Path, raw_backup_path: Path) -> None:
    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found at: {source_path}")
    if not raw_backup_path.exists() or source_path.resolve() != raw_backup_path.resolve():
        shutil.copyfile(source_path, raw_backup_path)
        logger.info(f"Preserved raw dataset copy at: {raw_backup_path}")


def load_dataset(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    logger.info(f"Loaded {df.shape[0]} rows x {df.shape[1]} columns.")
    return df


def clean_and_preprocess(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = df_raw.copy()
    
    # 1. Strip column headers
    df.columns = df.columns.str.strip()
    
    # 2. Drop completely empty rows
    df = df.dropna(how="all")
    
    # 3. Rename columns to snake_case
    rename_dict = {
        'Region': 'state',
        'Date': 'date',
        'Frequency': 'frequency',
        'Estimated Unemployment Rate (%)': 'unemployment_rate_pct',
        'Estimated Employed': 'estimated_employed',
        'Estimated Labour Participation Rate (%)': 'labour_participation_rate_pct',
        'Area': 'area_type'
    }
    df = df.rename(columns=rename_dict)
    
    # 4. Text normalization
    for col in ['state', 'frequency', 'area_type', 'date']:
        df[col] = df[col].astype(str).str.strip()
        
    # 5. Datetime conversion
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    
    # 6. Cast headcount to int64
    df['estimated_employed'] = df['estimated_employed'].astype('int64')
    
    # 7. Sort chronologically
    df = df.sort_values(by=['date', 'state', 'area_type']).reset_index(drop=True)
    
    return df


def validate_dataset(df: pd.DataFrame) -> None:
    assert df.isnull().sum().sum() == 0, "Null values remain!"
    assert ((df['unemployment_rate_pct'] >= 0) & (df['unemployment_rate_pct'] <= 100)).all()
    assert ((df['labour_participation_rate_pct'] >= 0) & (df['labour_participation_rate_pct'] <= 100)).all()
    assert (df['estimated_employed'] >= 0).all()
    assert df.duplicated(subset=['state', 'area_type', 'date']).sum() == 0
    logger.info("All data assertions passed successfully.")


def main():
    base_dir = Path(__file__).resolve().parent
    source_file = base_dir / "Unemployment in India.csv"
    raw_file = base_dir / "raw_data.csv"
    cleaned_file = base_dir / "cleaned_data.csv"
    
    preserve_raw_dataset(source_file, raw_file)
    raw_df = load_dataset(raw_file)
    cleaned_df = clean_and_preprocess(raw_df)
    validate_dataset(cleaned_df)
    cleaned_df.to_csv(cleaned_file, index=False)
    logger.info(f"Cleaned dataset saved to {cleaned_file} ({cleaned_df.shape[0]} rows).")


if __name__ == "__main__":
    main()

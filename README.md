# 📊 Unemployment in India Analysis — Data Preparation & Cleaning

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-3.0%2B-150458.svg)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Pipeline-Production--Ready-brightgreen.svg)](#)

A dedicated data engineering pipeline focusing strictly on the **Data Preparation and Preprocessing** phase for the [Unemployment in India Dataset](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india).

---

## 📌 1. Project Definition & Overview

Unemployment rates and labour participation dynamics are vital indicators of regional and macroeconomic health. This project focuses on ingesting, auditing, cleaning, and structuring monthly employment observations across 28 Indian States and Union Territories stratified by Rural and Urban areas (May 2019 – June 2020).

This module delivers the preprocessed, validated baseline required for downstream Exploratory Data Analysis (EDA), visualization, and economic modeling.

---

## 📊 2. Dataset Description & Use Cases

- **Source:** Kaggle ([Unemployment in India](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india))
- **Observation Period:** May 31, 2019 – June 30, 2020 (Monthly)
- **Geographic Coverage:** 28 States and Union Territories in India
- **Stratification:** Rural vs Urban areas

### Use Cases:
1. Evaluating temporal shifts in unemployment during pre-lockdown vs lockdown periods (COVID-19 impact).
2. Comparing labour participation and employment disparities between rural and urban sectors.
3. Supplying clean, standardized data for state-level macroeconomic dashboards and forecasting models.

---

## 📖 3. Data Dictionary

| Original Column Header | Cleaned Standard Header (`snake_case`) | Target Data Type | Nullable | Measurement Scale | Business Definition & Domain Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Region` | `state` | `string` / `object` | No | Nominal Categorical | Name of the Indian State or Union Territory (28 unique entities). |
| ` Date` | `date` | `datetime64[ns]` | No | Temporal (Date) | Observation month reference date (`YYYY-MM-DD`). Converted from raw string `DD-MM-YYYY`. |
| ` Frequency` | `frequency` | `string` / `object` | No | Nominal Categorical | Survey collection frequency (`Monthly`). Sanitized from whitespace anomalies. |
| ` Estimated Unemployment Rate (%)` | `unemployment_rate_pct` | `float64` | No | Continuous Ratio (%) | Proportion of the civilian labour force actively seeking employment during the reference month. |
| ` Estimated Employed` | `estimated_employed` | `int64` | No | Discrete Count | Estimated total headcount of individuals actively employed in the given state and area type. |
| ` Estimated Labour Participation Rate (%)` | `labour_participation_rate_pct` | `float64` | No | Continuous Ratio (%) | Proportion of the working-age population (15+ years) actively engaged in the labour force. |
| `Area` | `area_type` | `string` / `object` | No | Nominal Binary | Geographic stratification within each state: `Rural` or `Urban`. |

---

## ⚙️ 4. Data Cleaning Methodology & Preprocessing Decisions

1. **Raw Data Immutability (`raw_data.csv`):**
   - The source dataset is preserved without in-place modification to maintain an immutable audit trail.
2. **Standardized Column Naming (`snake_case`):**
   - Stripped irregular whitespace padding from raw headers (e.g., `' Date'` $\rightarrow$ `'date'`, `' Estimated Unemployment Rate (%)'` $\rightarrow$ `'unemployment_rate_pct'`).
3. **Handling Missing Values (`dropna(how='all')`):**
   - File diagnostics confirmed that all 28 missing entries in each column stemmed from trailing empty CSV delimiter artifacts (`,,,,,,`). Dropping these completely blank rows restored 100% data completeness without synthesizing artificial data through imputation.
4. **Duplicate Detection & Audit:**
   - Raw duplicates (27 instances) were entirely due to the trailing all-null rows. Valid observational records contain **zero duplicate observations** across the composite key `(state, area_type, date)`.
5. **Text Normalization:**
   - Stripped leading/trailing whitespace across `state`, `frequency`, and `area_type`, consolidating duplicate categories in `frequency` (unifying `' Monthly'` and `'Monthly'` into `'Monthly'`).
6. **Temporal Standardization (`datetime64[ns]`):**
   - Parsed date strings using explicit day-first format `%d-%m-%Y` into ISO 8601 timestamps (`YYYY-MM-DD`).
7. **Numeric Headcount Casting (`estimated_employed` $\rightarrow$ `int64`):**
   - Cast `.00` floating-point headcounts to 64-bit integers to accurately represent discrete counts of individuals.
8. **Deterministic Chronological Sorting:**
   - Sorted rows by `['date', 'state', 'area_type']` and reset index for reproducible downstream ETL ingestion.

---

## 🛠️ 5. Technologies & Libraries Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.10+** | Core programming language |
| **pandas** | Data ingestion, transformation, schema manipulation, and export |
| **numpy** | Numerical operations and array assertions |
| **jupyter / ipykernel** | Interactive notebook development and execution runtime |

---

## 📂 6. Current Project Structure

```text
Unemployment-in-India/
│
├── data_cleaning.ipynb        # Interactive Jupyter Notebook with rich markdown & execution outputs
├── raw_data.csv               # Immutable raw source dataset (768 rows × 7 cols)
├── cleaned_data.csv           # Cleaned, standardized, production-ready dataset (740 rows × 7 cols)
├── requirements.txt           # Python dependencies (pandas, numpy, jupyter, ipykernel)
├── .gitignore                 # Standard Python/Jupyter ignore rules
└── README.md                  # Project documentation & team contribution
```

---

## 👥 7. Team Member Contributions

| Member | Role | Key Contributions |
| :--- | :--- | :--- |
| **Maharudra** | **Data Cleaning & Preprocessing** | • Raw dataset preparation & preservation (`raw_data.csv`)<br>• Missing-value audit & artifact remediation<br>• Whitespace sanitization & `snake_case` normalization<br>• Datetime conversions & headcount type casting (`int64`)<br>• Generation and verification of `cleaned_data.csv` & `data_cleaning.ipynb` |
| **Bhavya** | **EDA & Analytics** | • Exploratory Data Analysis & statistical distributions<br>• Data visualization (trends, regional disparities, COVID-19 impact)<br>• Analytical findings & insights extraction<br>• Final project report and summary presentation |

---

## 🚀 8. Execution & Reproduction

```bash
# Install dependencies
pip install -r requirements.txt

# Run the notebook in Jupyter
jupyter notebook data_cleaning.ipynb
```

# Exploratory Data Analysis of Unemployment in India

---

## 1. Header Block

* **Student 1:** Maharudrasinh (Enrollment No: IU2541231882)
* **Student 2:** Bhavya (Enrollment No: IU2441230676)
* **Course:** Programming for Scientific Computing (Python) (CE0525), Semester 5, Section G
* **University:** INDUS University
* **Dataset Name & Link:** Unemployment in India (https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)
* **GitHub Repository:** https://github.com/MaharudrasinhRathore/Unemployment-in-India

---

## 2. Project Definition

This project is a descriptive and exploratory data analysis of the Indian labour market using Python. It has two parts:

* **Part 1 (Data Cleaning):** turns the raw Kaggle file into a clean, validated dataset (`cleaned_data.csv`).
* **Part 2 (Data Visualization):** uses the cleaned dataset to make 7 charts, with insights based only on the numbers printed by the code.

This study is strictly descriptive. No machine learning models, statistical forecasts, or predictive algorithms are used. Any observed pattern is an association, not a direct cause.

All findings are for academic purposes only and must not be used for economic planning or policy decisions.

---

## 3. Dataset

The dataset has historical employment indicators for Indian states and union territories. Each row is the estimated employment and unemployment figures for one state, on one date, in one area (Rural or Urban).

* **Raw data:** 768 rows, 7 columns
* **Cleaned data:** 740 rows, 7 columns, no missing values

| Raw column | Cleaned column | Meaning |
| :--- | :--- | :--- |
| `Region` | `state` | State or union territory |
| `Date` | `date` | Month-end date of the record |
| `Frequency` | `frequency` | Survey cadence (Monthly) |
| `Estimated Unemployment Rate (%)` | `unemployment_rate_pct` | Estimated unemployment rate (%) |
| `Estimated Employed` | `estimated_employed` | Estimated number of employed people |
| `Estimated Labour Participation Rate (%)` | `labour_participation_rate_pct` | Estimated labour participation rate (%) |
| `Area` | `area_type` | Rural or Urban |

**Main column studied:** `unemployment_rate_pct`

---

## 4. Part 1: Data Cleaning Procedure

1. **Raw backup:** an untouched copy of the original file is saved as `raw_data.csv`.
2. **Headers:** extra spaces are removed from the column names.
3. **Empty rows:** the 28 rows that are completely empty are dropped (768 rows become 740). No other missing values were found, so no imputation was needed.
4. **Renaming:** columns are renamed to snake_case names (see the table above).
5. **Text cleaning:** extra spaces are trimmed from the text columns.
6. **Date conversion:** `date` is converted from text to a real date (day-month-year format).
7. **Type casting:** `estimated_employed` is converted to whole numbers (`int64`).
8. **Sorting:** rows are sorted by date, state and area type.
9. **Validation checks before saving:**
   * no missing values remain
   * unemployment rate and participation rate are between 0 and 100
   * estimated employed is never negative
   * no duplicate rows for the same state, area type and date
10. **Outliers:** very high unemployment values are kept. They reflect real economic conditions and are not data errors.

---

## 5. Part 2: Visualizations and Results

All charts are made with pandas, matplotlib and seaborn, and saved in the `plots/` folder. Every insight uses only numbers printed by the code.

| # | Plot | Type | Result (from printed numbers) |
| :---: | :--- | :--- | :--- |
| 1 | Records per state | Count plot | 20 of 28 states have 28 records each, while Chandigarh has only 12 and Sikkim 17. |
| 2 | Distribution of unemployment rate | Histogram | The median is 8.35% but the mean is 11.79%. 129 records are above 20%, and the highest value is 76.74%. |
| 3 | Unemployment rate by area | Box plot | The median is 9.97% in Urban areas and 6.76% in Rural areas. |
| 4 | Average unemployment rate by state | Bar plot | Tripura is highest (28.35%) and Meghalaya is lowest (4.80%). |
| 5 | Average unemployment rate by month | Bar plot | The average is 10.70% in March 2020, then 23.64% in April and 24.88% in May 2020. |
| 6 | Participation rate vs unemployment rate | Scatter plot | The correlation is 0.0, so there is no straight-line pattern. |
| 7 | Correlation of the 3 numeric columns | Heatmap | The strongest pair is unemployment rate and estimated employed (-0.22). |

### Changes from the proposal
The 7 charts in the proposal were adjusted when the visualization part was built. The histogram has no KDE line. The two box plots for participation rate by area and employed workforce by area were replaced by the monthly bar plot (chart 5) and the correlation heatmap (chart 7).

---

## 6. Work Division

| Deliverable / Task | Maharudrasinh (IU2541231882) | Bhavya (IU2441230676) | Joint Collaboration |
| :--- | :---: | :---: | :---: |
| Data Loading, String Cleaning & Type Conversion | **Primary** | Review | Method sign-off |
| Missing Value Treatment & Validation | **Primary** | Review | Verification of dropped rows |
| Plot Implementations (Seaborn & Matplotlib) | Review | **Primary** | Aesthetic & layout selection |
| GitHub Repository Management & Documentation | Review | **Primary** | Regular repository commits |
| Scope, Limitations & Final Interpretation Synthesis | Contributor | Contributor | **Jointly Authored** |

---

## 7. Python Libraries and Tools Used

* **pandas:** importing the CSV, cleaning columns, parsing dates, grouping and summary tables.
* **NumPy:** numeric calculations in the cleaning script.
* **Matplotlib (`pyplot`):** figure sizing, titles, axis labels and saving charts.
* **Seaborn:** count plot, histogram, box plot, bar plot, scatter plot and heatmap.
* **Google Colab:** shared cloud runtime for the notebooks.
* **Git & GitHub:** version control and hosting the project.
* `os` and `shutil` (built into Python) are used only to create and zip the `plots` folder.

---

## 8. Repository Files and How to Run

| File | Description |
| :--- | :--- |
| `Unemployment in India.csv` | Original downloaded dataset |
| `raw_data.csv` | Untouched backup copy of the raw data |
| `data_cleaning.py` | Part 1 cleaning script |
| `data_cleaning.ipynb` | Part 1 cleaning notebook |
| `cleaned_data.csv` | Cleaned dataset (output of Part 1, input of Part 2) |
| `unemployment_visualization.ipynb` | Part 2 Colab notebook (7 charts and insights) |
| `plots/` | The 7 saved chart images |
| `Unemployment_in_IND_Proposal.docx` | Project proposal |

**Part 1:** run `data_cleaning.py` (or `data_cleaning.ipynb`) with `Unemployment in India.csv` in the same folder. It creates `raw_data.csv` and `cleaned_data.csv`.

**Part 2:**
1. Open `unemployment_visualization.ipynb` in Google Colab.
2. Click **Runtime → Run all**.
3. If the data link fails, the notebook asks you to upload `cleaned_data.csv`.
4. The last cell zips the `plots` folder and downloads it as `plots.zip`.

---

## 9. Limitations

* These charts show links and patterns, not causes. For example, the jump in April and May 2020 does not tell us why it happened.
* States have different numbers of records (from 12 to 28), so state comparisons should be read carefully.
* Correlation only measures straight-line links between columns.
* The data covers only 14 months (May 2019 to June 2020), so long-term trends cannot be judged.

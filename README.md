# PROJECT PROPOSAL: EXPLORATORY DATA ANALYSIS OF UNEMPLOYMENT IN INDIA

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

This project is a descriptive and exploratory data analysis of the Indian labor market using Python. The objective is to systematically clean raw historical metrics and generate visualizations that illustrate how unemployment rates, employment numbers, and labor participation rates vary across regions, areas, and time.

This study is strictly descriptive. No machine learning models, statistical forecasts, or predictive algorithms are used. Any observed patterns represent empirical associations, not direct causal links.

Project success is defined by:
1. Complete reproducibility of all cleaning routines and charts in Google Colab.
2. Clear justification documented for every decision (handling missing data, string sanitization, and outlier treatment).
3. Transparent documentation regarding the limitations of the data.

All findings are intended exclusively for academic purposes and must not be used for actual economic planning or policy implementation.

---

## 3. Dataset Use Case

The dataset provides historical employment indicators across Indian states and union territories, containing 768 entries and 7 columns prior to cleaning. Each individual row represents the estimated employment and unemployment figures for a specific region, on a specific date, within a designated area (Rural or Urban).

The dataset features the following exact columns:
* **`Region`:** Name of the state or union territory in India (text/categorical).
* **`Date`:** Reporting date of the survey record (originally text/object).
* **`Frequency`:** Survey observation cadence (e.g., Monthly).
* **`Estimated Unemployment Rate (%)`:** Estimated percentage of the active labor force that is unemployed (numeric float).
* **`Estimated Employed`:** Estimated absolute number of employed persons (numeric float).
* **`Estimated Labour Participation Rate (%)`:** Estimated percentage of the eligible population engaged in the labor force (numeric float).
* **`Area`:** Geographic demographic zone, categorized as "Rural" or "Urban" (text/categorical).

This data is used to analyze structural differences in employment between rural and urban workforces, observe macro-level economic shifts over time, and compare relative labor trends across regional states.

---

## 4. Planned Procedure

1. **Loading and Inspection:** The CSV file will be loaded into pandas. Column labels will be trimmed using `.str.strip()` to remove leading/trailing whitespace present in the raw headers.
2. **Duplicate Handling:** Duplicates will be identified using `df.duplicated().sum()` and removed via `df.drop_duplicates()` if redundant records are found.
3. **Data Type Casting:** The `Date` column will be converted to datetime format using `pd.to_datetime(dayfirst=True)`, and numeric indicators will be verified as floating-point values.
4. **Outlier Detection:** Outliers will be flagged using the standard Interquartile Range (IQR) rule:
   $$\text{IQR} = Q_3 - Q_1$$
   Points falling outside $[Q_1 - 1.5 \times \text{IQR},\; Q_3 + 1.5 \times \text{IQR}]$ will be tagged. Because rapid spikes in unemployment and wide demographic differences in total employment reflect real-world economic conditions rather than data collection errors, these records will be kept rather than clipped or dropped.
5. **Missing Values Plan:** As shown in `df.info()`, 740 rows contain valid data, and 28 rows are completely null across all columns.

| Columns | Planned Treatment | Justification |
| :--- | :--- | :--- |
| **All columns (completely empty rows)** | Drop via `df.dropna(how='all')` | The 28 missing entries represent fully empty trailing rows that carry no information. |
| **`Estimated Unemployment Rate (%)`** | Median imputation (if isolated nulls remain) | Continuous skewed indicator; median avoids distortion from extreme rates. |
| **`Estimated Employed`** | Median imputation grouped by `Region` | Employment totals scale heavily by regional population; regional grouping preserves scale. |
| **`Estimated Labour Participation Rate (%)`** | Median imputation (if isolated nulls remain) | Stable percentage distribution where the median represents central tendency safely. |
| **`Region` & `Area`** | Mode imputation or assign `"Unknown"` | Categorical fields; explicit classification prevents false attribution. |
| **`Date` & `Frequency`** | Forward-fill (`ffill`) or drop invalid row | Preserves temporal consistency without fabricating arbitrary survey periods. |

---

## 5. Visualizations and Planned Questions

| Fig. | Plot Name | Type | Question It Answers |
| :---: | :--- | :--- | :--- |
| **1** | Distribution of Unemployment Rate | Histogram with KDE | How are unemployment percentages distributed across all recorded periods, and is there skewness? |
| **2** | Unemployment Rate by Area | Box Plot | How do median values, spreads, and extreme spikes in unemployment compare between Rural and Urban areas? |
| **3** | Record Count by Region | Count Plot | How evenly distributed are survey records across the different states and territories? |
| **4** | Mean Unemployment Rate by Region | Bar Chart | Which states exhibit higher or lower average estimated unemployment rates over the observation window? |
| **5** | Unemployment Rate vs. Participation Rate | Scatter Plot | Is there an apparent correlation or pattern between labor participation rates and unemployment rates? |
| **6** | Labour Participation Rate by Area | Box Plot | How do labor force participation levels and dispersion compare between Rural and Urban sectors? |
| **7** | Employed Workforce Distribution by Area | Box Plot | How does the scale and dispersion of the total employed workforce differ between Rural and Urban sectors? |

---

## 6. Expected Outcomes

* **Figure 1 (Histogram):** Expected to be right-skewed, with most measurements clustering at lower-to-moderate percentages alongside an extended tail of higher values.
* **Figure 2 (Box Plot):** Expected to show higher variability and slightly higher median unemployment rates in Urban areas relative to Rural areas.
* **Figure 3 (Count Plot):** Expected to display uniform record frequencies across most states, highlighting any regions with missing survey intervals.
* **Figure 4 (Bar Chart):** Expected to show regional disparities, with select northern and eastern states recording higher average unemployment figures.
* **Figure 5 (Scatter Plot):** No strong prior assumption of a strict linear relationship; points are expected to show broad dispersion across participation brackets.
* **Figure 6 (Box Plot):** Expected to show relatively comparable labor participation medians across both areas, with potential variation in range and spread.
* **Figure 7 (Box Plot):** Expected to reflect higher median absolute employment figures in Rural areas due to the scale of the agrarian workforce.

---

## 7. Work Division

| Deliverable / Task | Maharudrasinh (IU2541231882) | Bhavya (IU2441230676) | Joint Collaboration |
| :--- | :---: | :---: | :---: |
| Data Loading, String Cleaning & Type Conversion | **Primary** | Review | Method sign-off |
| Missing Value Treatment & Outlier Flagging (IQR) | **Primary** | Review | Verification of dropped rows |
| Plot Implementations (Seaborn & Matplotlib) | Review | **Primary** | Aesthetic & layout selection |
| GitHub Repository Management & Documentation | Review | **Primary** | Regular repository commits |
| Scope, Limitations & Final Interpretation Synthesis | Contributor | Contributor | **Jointly Authored** |

---

## 8. Python Libraries and Tools Used

* **pandas:** Used for importing the CSV file, standardizing column strings, parsing dates, handling missing values, and generating summary tables.
* **NumPy:** Used for vectorized numerical calculations and evaluating quartile thresholds for the IQR rule.
* **Matplotlib (`pyplot`):** Used for base canvas styling, figure sizing, axis labels, legends, and export parameters.
* **Seaborn:** Used for rendering statistical graphics including distribution plots, box plots, count plots, and scatter charts.
* **Google Colab:** Used as the shared cloud runtime environment for collaborative notebook development and verification.
* **Git & GitHub:** Used for distributed version control, tracking code modifications, and hosting the project documentation repository.

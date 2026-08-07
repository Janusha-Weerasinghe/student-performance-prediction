# Exploratory Data Analysis Report

## Dataset Overview

...

## Missing Values

...

## Duplicate Rows

...

## Target Variable
# 4. Target Variable Analysis

## 4.1 Objective

The objective of this analysis is to understand the characteristics and distribution of the target variable (`Exam_Score`). Since this project focuses on predicting students' examination scores using regression models, it is essential to analyze the target variable before model development.

The analysis includes:

- Summary statistics
- Histogram
- Kernel Density Estimation (KDE)
- Boxplot
- Skewness
- Kurtosis

---

## 4.2 Target Variable

| Property | Value |
|----------|-------|
| Target Variable | `Exam_Score` |
| Data Type | Numeric (Float64) |
| Machine Learning Task | Regression |

---

## 4.3 Summary Statistics

| Statistic | Value |
|-----------|------:|
| Count | 6,607 |
| Mean | 67.24 |
| Standard Deviation | 3.89 |
| Minimum | 55.00 |
| 25th Percentile (Q1) | 65.00 |
| Median (50%) | 67.00 |
| 75th Percentile (Q3) | 69.00 |
| Maximum | 101.00 |

### Interpretation

The dataset contains **6,607 student records** with an average examination score of **67.24**.

The standard deviation of **3.89** indicates relatively low variation in student scores, suggesting that most students achieved scores close to the average.

The minimum recorded score is **55**, while the highest score is **101**, indicating the presence of several exceptionally high scores.

The median score (**67**) is very close to the mean (**67.24**), indicating that the central tendency is relatively stable.

---

## 4.4 Histogram Analysis

**Figure**

`reports/figures/target_variable/exam_score_histogram.png`

### Observation

The histogram shows that:

- Most students scored between **63 and 71 marks**.
- The distribution has a single dominant peak (unimodal).
- The majority of observations are concentrated around **67 marks**.
- A small number of observations extend beyond **80 marks**, creating a long right tail.

### Interpretation

The histogram indicates that the majority of students achieved average examination scores, while only a limited number of students obtained exceptionally high marks. This suggests that high-performing students are comparatively rare within the dataset.

---

## 4.5 Kernel Density Estimation (KDE)

**Figure**

`reports/figures/target_variable/exam_score_kde.png`

### Observation

The KDE curve shows:

- A single smooth peak around **67 marks**.
- The distribution is **positively (right) skewed**.
- Most probability density is concentrated between **63 and 71 marks**.
- A long right tail extends towards higher examination scores.

### Interpretation

The KDE plot confirms that the target variable does not perfectly follow a normal distribution. Instead, it exhibits a moderate positive skew caused by a relatively small number of students with exceptionally high examination scores.

---

## 4.6 Boxplot Analysis

**Figure**

`reports/figures/target_variable/exam_score_boxplot.png`

### Observation

The boxplot indicates:

- Median score is approximately **67**.
- First Quartile (Q1) = **65**
- Third Quartile (Q3) = **69**
- Interquartile Range (IQR) = **4**
- Several upper outliers are present between **75 and 101 marks**.
- A few lower outliers appear around **55–58 marks**.

### Interpretation

The majority of examination scores fall within a relatively narrow range, indicating consistent student performance. However, multiple outliers are visible, particularly on the upper end of the distribution. These values are likely to represent genuinely high-performing students rather than data entry errors and should be retained unless domain knowledge suggests otherwise.

---

## 4.7 Skewness Analysis

| Metric | Value |
|--------|------:|
| Skewness | **1.6448** |

### Interpretation

A skewness value greater than zero indicates a **positively skewed (right-skewed)** distribution.

The calculated skewness value of **1.6448** suggests a noticeable right skew, meaning that a relatively small number of students achieved exceptionally high examination scores.

---

## 4.8 Kurtosis Analysis

| Metric | Value |
|--------|------:|
| Kurtosis | **10.5754** |

### Interpretation

The kurtosis value is substantially greater than **3**, indicating a **leptokurtic distribution**.

This suggests that the dataset contains heavier tails and more extreme values than a normal distribution, which aligns with the outliers observed in the boxplot.

---

## 4.9 Key Findings

- The target variable (`Exam_Score`) is continuous, confirming that this is a **regression problem**.
- The average examination score is **67.24**, with relatively low variability.
- The distribution is **positively skewed**, indicating that exceptionally high scores occur less frequently.
- Most students scored between **63 and 71 marks**.
- Several upper-end outliers are present, extending to **101 marks**.
- The high kurtosis value indicates heavier tails than a normal distribution.
- Despite the presence of outliers, the target variable remains suitable for regression modelling.

---

## 4.10 Conclusion

The target variable (`Exam_Score`) was analyzed using descriptive statistics, histogram, KDE, boxplot, skewness, and kurtosis.

The analysis reveals that student examination scores are concentrated around the mean of **67.24**, with relatively low variability. The distribution exhibits a **positive skew** and contains several legitimate high-score outliers, resulting in a **leptokurtic distribution**.

Overall, the target variable is appropriate for regression modelling. The observed distribution characteristics will be considered during feature engineering, model selection, and evaluation in subsequent stages of the project.
...

### Business Insight

The majority of students achieve average examination scores, while only a small proportion attain exceptionally high marks. This suggests that predictive models should focus on accurately estimating the performance of average students while remaining robust enough to handle high-performing outliers. Educational institutions could use such predictions to identify students who may benefit from additional academic support before final examinations.

---

## Numerical Feature Analysis

### Features Analysed

- Hours Studied
- Attendance
- Previous Scores
- Sleep Hours
- Physical Activity
- Tutoring Sessions
- Exam Score

---

### Summary

The numerical variables were analysed using descriptive statistics and visualizations.

For each feature, the following statistics were examined:

- Mean
- Median
- Standard Deviation
- Minimum
- Maximum

Histograms were used to understand the distribution of each feature, while boxplots were used to identify potential outliers and evaluate the spread of the data.

---

## Observations

### 1. Hours Studied

- The distribution is approximately bell-shaped and close to a normal distribution.
- Most students studied around the middle range of hours.
- A few students studied significantly fewer or significantly more hours than the majority.
- The boxplot shows several outliers on both the lower and upper ends, but they appear to represent genuine observations rather than obvious data errors.

---

### 2. Attendance

- Attendance values are distributed fairly evenly between approximately 60% and 100%.
- No strong skewness is observed.
- The boxplot does not indicate any significant outliers.
- This feature appears to have consistent data quality.

---

### 3. Previous Scores

- Previous scores are spread relatively evenly across the available range.
- The histogram does not indicate strong skewness.
- No significant outliers are visible in the boxplot.
- The feature appears well distributed and should provide useful predictive information.

---

### 4. Sleep Hours

- Sleep hours are concentrated between approximately 6 and 8 hours.
- The variable is discrete, producing visible peaks at integer values.
- No significant outliers are observed.
- The distribution suggests most students maintain similar sleeping habits.

---

### 5. Physical Activity

- Physical activity is an ordinal/discrete feature with values concentrated around levels 2, 3, and 4.
- Level 3 appears to be the most common activity level.
- No abnormal observations or outliers are present.
- Since the variable contains integer categories, it may later be treated as either numerical or ordinal depending on the modelling approach.

---

### 6. Tutoring Sessions

- Most students attended between 0 and 2 tutoring sessions.
- The distribution is strongly right-skewed.
- A small number of students attended four or more tutoring sessions, which appear as outliers in the boxplot.
- These observations likely represent valid student behaviour rather than incorrect data and should not be removed without further investigation.

---

### 7. Exam Score (Target Variable)

- Exam scores are concentrated around the mid-to-high 60s.
- The histogram shows an approximately normal distribution with a slight positive skew.
- Several high-score observations appear as outliers in the boxplot, extending toward 100.
- These values are realistic for academic performance and should be retained.

---

## Overall Findings

- Most numerical variables exhibit acceptable distributions for machine learning.
- Hours Studied and Exam Score are approximately normally distributed.
- Attendance and Previous Scores are broadly and evenly distributed.
- Sleep Hours, Physical Activity, and Tutoring Sessions are discrete numerical variables.
- Tutoring Sessions displays noticeable right skew with several high-value observations.
- No evidence of severe data quality issues is visible from the numerical feature analysis.
- Outliers identified in Hours Studied, Tutoring Sessions, and Exam Score appear to be natural observations rather than obvious errors.


...

## Categorical Features

...

## Correlation Analysis

...

## Outlier Analysis

...

## Key Findings

...

## Recommended Preprocessing

...
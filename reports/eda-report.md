# 📊 Exploratory Data Analysis (EDA) Report

**Project:** Student Performance Prediction

**Project Number:** 001

**Author:** Janusha Weerasinghe

**Date:** 06-Aug-2026

---

# 1. Objective

The objective of Exploratory Data Analysis (EDA) is to understand the dataset before building machine learning models. This analysis helps identify data quality issues, understand feature distributions, detect missing values, identify outliers, and discover relationships between variables.

---
# 2. Dataset Overview

| Item | Value |
|------|------|
| Dataset Name | Student Performance Factors |
| Total Records | 6,607 |
| Total Features | 20 |
| Target Variable | Exam_Score |
| Machine Learning Task | Regression |

---

# 3. Dataset Shape

## Rows

6,607

## Columns

20 Features + 1 Target Variable

### Observation

- The dataset contains a sufficient number of records for regression analysis.
- The dataset size is appropriate for training and evaluating multiple machine learning models.

---

# 4. Dataset Information

### Data Types

| Data Type | Count |
|-----------|------:|
| Integer | (Update after df.info()) |
| Float | (Update after df.info()) |
| Object | 13 |

### Observation

- The dataset contains both numerical and categorical variables.
- Categorical variables will require encoding before model training.

---

# 6. Missing Values Analysis

## Missing Values

| Feature | Missing Values |
|---------|---------------:|
| Teacher_Quality | 78 |
| Parental_Education_Level | 90 |
| Distance_from_Home | 67 |

### Observation

- Only three categorical features contain missing values.
- The percentage of missing values is relatively low.
- Missing values will be handled during preprocessing.

---

# 7. Duplicate Records

### Result

0 Duplicate Rows

### Observation

No duplicate records were found.

---


# 8. Target Variable Analysis

## 8.1 Objective

The objective of this analysis is to understand the characteristics and distribution of the target variable (`Exam_Score`). Since this project focuses on predicting students' examination scores using regression models, it is essential to analyze the target variable before model development.

The analysis includes:

- Summary statistics
- Histogram
- Kernel Density Estimation (KDE)
- Boxplot
- Skewness
- Kurtosis

---

## 8.2 Target Variable

| Property | Value |
|----------|-------|
| Target Variable | `Exam_Score` |
| Data Type | Numeric (Float64) |
| Machine Learning Task | Regression |

---

## 8.3 Summary Statistics

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

## 8.4 Histogram Analysis

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

## 8.5 Kernel Density Estimation (KDE)

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

## 8.6 Boxplot Analysis

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

## 8.7 Skewness Analysis

| Metric | Value |
|--------|------:|
| Skewness | **1.6448** |

### Interpretation

A skewness value greater than zero indicates a **positively skewed (right-skewed)** distribution.

The calculated skewness value of **1.6448** suggests a noticeable right skew, meaning that a relatively small number of students achieved exceptionally high examination scores.

---

## 8.8 Kurtosis Analysis

| Metric | Value |
|--------|------:|
| Kurtosis | **10.5754** |

### Interpretation

The kurtosis value is substantially greater than **3**, indicating a **leptokurtic distribution**.

This suggests that the dataset contains heavier tails and more extreme values than a normal distribution, which aligns with the outliers observed in the boxplot.

---

## 8.9 Key Findings

- The target variable (`Exam_Score`) is continuous, confirming that this is a **regression problem**.
- The average examination score is **67.24**, with relatively low variability.
- The distribution is **positively skewed**, indicating that exceptionally high scores occur less frequently.
- Most students scored between **63 and 71 marks**.
- Several upper-end outliers are present, extending to **101 marks**.
- The high kurtosis value indicates heavier tails than a normal distribution.
- Despite the presence of outliers, the target variable remains suitable for regression modelling.

---

## 8.10 Conclusion

The target variable (`Exam_Score`) was analyzed using descriptive statistics, histogram, KDE, boxplot, skewness, and kurtosis.

The analysis reveals that student examination scores are concentrated around the mean of **67.24**, with relatively low variability. The distribution exhibits a **positive skew** and contains several legitimate high-score outliers, resulting in a **leptokurtic distribution**.

Overall, the target variable is appropriate for regression modelling. The observed distribution characteristics will be considered during feature engineering, model selection, and evaluation in subsequent stages of the project.
...

### Business Insight

The majority of students achieve average examination scores, while only a small proportion attain exceptionally high marks. This suggests that predictive models should focus on accurately estimating the performance of average students while remaining robust enough to handle high-performing outliers. Educational institutions could use such predictions to identify students who may benefit from additional academic support before final examinations.

---

## 9. Numerical Feature Analysis

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

# 10. Categorical Feature Analysis

## Total Categorical Features

13

### Summary

| Feature | Unique Values | Missing Values | Most Common Category | Frequency |
|---------|--------------:|---------------:|----------------------|----------:|
| Parental_Involvement | 3 | 0 | Medium | 3362 |
| Access_to_Resources | 3 | 0 | Medium | 3319 |
| Extracurricular_Activities | 2 | 0 | Yes | 3938 |
| Motivation_Level | 3 | 0 | Medium | 3351 |
| Internet_Access | 2 | 0 | Yes | 6108 |
| Family_Income | 3 | 0 | Low | 2672 |
| Teacher_Quality | 3 | 78 | Medium | 3925 |
| School_Type | 2 | 0 | Public | 4598 |
| Peer_Influence | 3 | 0 | Positive | 2638 |
| Learning_Disabilities | 2 | 0 | No | 5912 |
| Parental_Education_Level | 3 | 90 | High School | 3223 |
| Distance_from_Home | 3 | 67 | Near | 3884 |
| Gender | 2 | 0 | Male | 3814 |


### Key Findings

- The dataset contains 13 categorical features.
- Three categorical features contain missing values.
- Most features have only two or three categories.
- Internet_Access is highly imbalanced toward "Yes".
- School_Type is dominated by Public schools.
- Gender distribution is reasonably balanced.

---
# 11. Correlation Analysis

## Objective

The objective of correlation analysis is to measure the strength and direction of the linear relationship between numerical features and the target variable (`Exam_Score`). This helps identify the most influential predictors, detect multicollinearity, and support feature selection for machine learning.

---

## Methodology

Pearson Correlation Coefficient was calculated for all numerical features using:

```python
corr = df.corr(numeric_only=True)
```

The results were visualized using a correlation heatmap.

---

## Correlation Matrix

The numerical features included in the analysis were:

- Hours_Studied
- Attendance
- Sleep_Hours
- Previous_Scores
- Tutoring_Sessions
- Physical_Activity
- Exam_Score

---

## Correlation with Target Variable (Exam_Score)

| Feature | Correlation | Interpretation |
|---------|------------:|---------------|
| Attendance | **0.5811** | Moderate Positive |
| Hours_Studied | **0.4455** | Moderate Positive |
| Previous_Scores | **0.1751** | Weak Positive |
| Tutoring_Sessions | **0.1565** | Weak Positive |
| Physical_Activity | **0.0278** | Very Weak Positive |
| Sleep_Hours | **-0.0170** | Very Weak Negative |

---

## Key Findings

### 1. Attendance

Attendance has the strongest positive correlation with Exam_Score (0.581).

This suggests that students with higher attendance generally achieve better examination scores.

---

### 2. Hours Studied

Hours_Studied has the second strongest correlation (0.446).

This indicates that spending more time studying is associated with improved academic performance.

---

### 3. Previous Scores

Previous_Scores has a weak positive relationship (0.175).

Although previous academic performance contributes to predicting exam scores, its influence is relatively smaller compared to attendance and study hours.

---

### 4. Tutoring Sessions

Tutoring_Sessions has a weak positive correlation (0.157).

Students attending tutoring sessions tend to perform slightly better, but tutoring alone is not a strong predictor.

---

### 5. Physical Activity

Physical_Activity shows an almost negligible positive correlation (0.028).

Based on this dataset, physical activity appears to have minimal direct influence on examination performance.

---

### 6. Sleep Hours

Sleep_Hours has a very weak negative correlation (-0.017).

The relationship is extremely close to zero, suggesting that sleep duration alone does not significantly influence exam scores in this dataset.

---

## Feature Relationships

The strongest predictors of Exam_Score are:

1. Attendance
2. Hours_Studied
3. Previous_Scores
4. Tutoring_Sessions

These variables are expected to contribute the most during model training.

---

## Multicollinearity Analysis

No pair of independent numerical variables exhibits a strong correlation (greater than ±0.80).

This indicates that multicollinearity is not a significant concern for the numerical features in this dataset.

---

## Business Interpretation

The analysis suggests that academic engagement plays a greater role in predicting examination performance than lifestyle-related factors.

Students who attend classes regularly and spend more time studying are generally more likely to achieve higher examination scores.

Educational institutions may therefore improve student outcomes by promoting regular attendance and effective study habits.

---

## Conclusion

The correlation analysis reveals that **Attendance** and **Hours_Studied** are the most influential numerical predictors of student examination performance.

The remaining numerical variables show weak or negligible correlations with the target variable. However, these features may still improve prediction accuracy when combined with categorical variables in machine learning models.

No evidence of severe multicollinearity was observed, indicating that all numerical features can be retained for the preprocessing and model development stages.

---


## Outlier Analysis

Outlier detection was performed using boxplots and the Interquartile Range (IQR) method for all numerical features.

### Results

| Feature | Outliers |
|---------|----------|
| Hours_Studied | 43 |
| Attendance | 0 |
| Sleep_Hours | 0 |
| Previous_Scores | 0 |
| Tutoring_Sessions | 430 |
| Physical_Activity | 0 |
| Exam_Score | 104 |

### Observations

- Hours_Studied contains a small number of extreme observations.
- Attendance, Sleep_Hours, Previous_Scores, and Physical_Activity do not contain significant outliers.
- Tutoring_Sessions contains a large number of statistical outliers due to its right-skewed distribution.
- Exam_Score includes several unusually high and low values that are likely valid student performances.

### Conclusion

The detected outliers appear to represent genuine observations rather than data entry errors. Therefore, no outliers were removed during the exploratory data analysis stage.

The impact of these observations will be evaluated during model training. If necessary, robust algorithms or feature transformations may be considered instead of removing valid data.

## Key Findings

...

## Recommended Preprocessing

...
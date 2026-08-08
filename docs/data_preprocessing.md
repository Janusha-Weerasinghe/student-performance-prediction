

# 🚀 Project 001 — Student Performance Prediction

## Milestone 4 — Data Preprocessing

### Exact goal

Take:

```text
Raw CSV
   ↓
Clean data
   ↓
Handle missing values
   ↓
Separate X / y
   ↓
Train/Test Split
   ↓
Feature Engineering
   ↓
Numerical preprocessing
   ↓
Categorical preprocessing
   ↓
Combine transformations
   ↓
Validate
   ↓
Save preprocessing pipeline
```

At the end, we should have a **reusable preprocessing pipeline**, not just a modified notebook.

---

# 1. What You Need to Create

Inside repository, we're going to create/update these files:

```text
student-performance-prediction/
│
├── data/
│   ├── raw/
│   │   └── StudentPerformanceFactors.csv
│   │
│   └── processed/
│       └── .gitkeep
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_preprocessing.ipynb        ← CREATE
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py              ← CREATE
│   └── feature_engineering.py        ← CREATE
│
├── models/
│   └── .gitkeep
│
├── reports/
│   └── figures/
│
├── tests/
│   └── test_preprocessing.py         ← CREATE
│
├── docs/
│   └── preprocessing.md              ← CREATE
│
├── .gitignore
├── README.md
└── requirements.txt
```

### Important

Don't create unnecessary files such as:

```text
processed.csv
encoded_data.csv
scaled_data.csv
final_data.csv
```

just for the sake of having files.

We'll create the necessary artifacts deliberately.

---

# 2. Before Coding — Check Your Raw Dataset

Your raw dataset should be here:

```text
data/raw/StudentPerformanceFactors.csv
```

The filename can be different if that's what you already have.

For example:

```text
data/raw/StudentPerformanceFactors.csv
```

Make sure the dataset is **inside `data/raw/`**.

---

# 3. Important GitHub Rule — Don't Upload the Dataset

Because datasets can have licensing/distribution restrictions and can be large, we should **not automatically push the raw dataset to GitHub**.

Your `.gitignore` should contain:

```gitignore
data/raw/*
data/processed/*
```

But we can keep the folders using:

```text
data/raw/.gitkeep
data/processed/.gitkeep
```

Your README will explain where the dataset came from and how to obtain it.

---

# 4. Create `src/data_loader.py`

This file is responsible only for **loading the dataset**.

Create:

```text
src/data_loader.py
```

Add:

```python
from pathlib import Path

import pandas as pd


def load_data(file_path: str | Path) -> pd.DataFrame:
    """
    Load the student performance dataset from a CSV file.

    Parameters
    ----------
    file_path : str | Path
        Path to the CSV dataset.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    if file_path.suffix.lower() != ".csv":
        raise ValueError(
            "Expected a CSV file."
        )

    return pd.read_csv(file_path)
```

---

# 5. Why Do We Have `data_loader.py`?

Instead of repeatedly writing:

```python
pd.read_csv(...)
```

throughout the project, we create one reusable function.

Later:

```python
from src.data_loader import load_data

df = load_data("data/raw/StudentPerformanceFactors.csv")
```

This is **modular programming**.

---

# 6. Create `src/feature_engineering.py`

Now create:

```text
src/feature_engineering.py
```

For this project, we're going to keep feature engineering **simple and explainable**.

Start with:

```python
import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create additional features from the raw dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.

    Returns
    -------
    pd.DataFrame
        Dataset containing engineered features.
    """

    df = df.copy()

    # Interaction between study time and attendance.
    df["Study_Attendance_Interaction"] = (
        df["Hours_Studied"] * df["Attendance"]
    )

    return df
```

---

# 7. Why This Feature?

We already discovered:

```text
Hours_Studied → positive relationship
Attendance → positive relationship
```

So we're testing whether their interaction contains useful predictive information.

But remember:

> Creating a feature does NOT mean the feature is automatically useful.

Later, model evaluation will tell us whether it improves performance.

---

# 8. Important: Feature Engineering and Data Leakage

We must not accidentally use:

```text
Exam_Score
```

to create predictors.

For example, this would be WRONG:

```python
df["Performance_Level"] = df["Exam_Score"] * 2
```

because `Exam_Score` is our target.

That would cause **target leakage**.

---

# 9. Create `src/preprocessing.py`

This is the most important file in Milestone 4.

Create:

```text
src/preprocessing.py
```

Add:

```python
from typing import List

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def create_preprocessor(
    numerical_features: List[str],
    categorical_features: List[str],
) -> ColumnTransformer:
    """
    Create a preprocessing pipeline for numerical
    and categorical features.

    Parameters
    ----------
    numerical_features : List[str]
        Names of numerical columns.

    categorical_features : List[str]
        Names of categorical columns.

    Returns
    -------
    ColumnTransformer
        Configured preprocessing pipeline.
    """

    numerical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(
                    strategy="most_frequent"
                ),
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False,
                ),
            ),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                numerical_pipeline,
                numerical_features,
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features,
            ),
        ]
    )

    return preprocessor
```

---

# 10. What This Code Is Doing

This is the architecture:

```text
                    DATA
                      │
          ┌───────────┴───────────┐
          │                       │
      Numerical               Categorical
          │                       │
          ▼                       ▼
     Median Imputer        Most-Frequent Imputer
          │                       │
          ▼                       ▼
    StandardScaler          One-Hot Encoder
          │                       │
          └───────────┬───────────┘
                      ▼
               Transformed X
```

This is what makes the project a proper ML pipeline rather than a collection of notebook operations.

---

# 11. Why Median Imputation?

For numerical columns:

```python
SimpleImputer(strategy="median")
```

Suppose:

```text
Hours_Studied

5
6
7
NaN
8
9
```

The missing value is replaced by the median.

We prefer median because it is more robust to outliers than the mean.

---

# 12. Why Most-Frequent Imputation?

Your missing values are in:

```text
Teacher_Quality
Parental_Education_Level
Distance_from_Home
```

These are categorical.

Therefore:

```python
SimpleImputer(strategy="most_frequent")
```

uses the most common category.

---

# 13. Why StandardScaler?

For numerical variables:

```text
Hours_Studied
Attendance
Previous_Scores
Sleep_Hours
...
```

their scales are different.

For example:

```text
Hours_Studied → 1–10
Attendance → 60–100
Previous_Scores → 50–100
```

StandardScaler puts them on a comparable standardized scale.

It transforms values approximately to:

```text
mean = 0
standard deviation = 1
```

---

# 14. Why OneHotEncoder?

Suppose:

```text
Gender

Male
Female
```

After encoding, it becomes something like:

```text
Gender_Female
Gender_Male
```

Similarly:

```text
Family_Income

Low
Medium
High
```

becomes:

```text
Family_Income_High
Family_Income_Low
Family_Income_Medium
```

The model can then work with numerical representations.

---

# 15. Why `handle_unknown="ignore"`?

This is **very important for production**.

Imagine training data contains:

```text
School_Type

Public
Private
```

Later, production data contains:

```text
School_Type = International
```

Without proper handling, the encoder could fail.

With:

```python
handle_unknown="ignore"
```

the pipeline safely handles an unseen category.

---

# 16. Why `ColumnTransformer`?

Because different columns require different preprocessing.

```text
Numerical
    ↓
Imputer
    ↓
Scaler
```

while:

```text
Categorical
    ↓
Imputer
    ↓
Encoder
```

`ColumnTransformer` combines both workflows.

---

# 17. Now Create the Notebook

Create:

```text
notebooks/02_preprocessing.ipynb
```

This notebook is where we'll **experiment, inspect, and validate** the preprocessing.

The actual reusable logic remains inside `src/`.

That's an important professional distinction:

```text
Notebook
→ Experimentation / visualization / validation

src/
→ Reusable production code
```

---

# 18. Notebook Structure

Your notebook should contain these sections.

```text
02_preprocessing.ipynb

1. Imports
2. Configuration
3. Load Dataset
4. Initial Validation
5. Separate Features and Target
6. Feature Engineering
7. Define Feature Groups
8. Train-Test Split
9. Create Preprocessor
10. Fit on Training Data
11. Transform Training Data
12. Transform Test Data
13. Validate Results
14. Inspect Feature Names
15. Save Pipeline
16. Summary
```

---

# 19. Notebook — Section 1

### Markdown cell

```markdown
# Student Performance Prediction
## Milestone 4 — Data Preprocessing

This notebook implements and validates the preprocessing pipeline
for the Student Performance Prediction project.

### Objectives

- Load and validate the raw dataset
- Separate features and target
- Perform feature engineering
- Handle missing values
- Encode categorical variables
- Scale numerical variables
- Split data into training and testing sets
- Build a reusable preprocessing pipeline
- Validate transformed data
- Save the preprocessing pipeline
```

---

# 20. Notebook — Section 2: Imports

```python
from pathlib import Path
import sys

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

# Add project root to Python path
PROJECT_ROOT = Path.cwd().parent
sys.path.append(str(PROJECT_ROOT))

from src.data_loader import load_data
from src.feature_engineering import create_features
from src.preprocessing import create_preprocessor
```

If your notebook location causes a path problem, we'll adjust it based on your VS Code/Jupyter working directory rather than randomly changing the code.

---

# 21. Configuration

Create a configuration cell:

```python
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "StudentPerformanceFactors.csv"
MODEL_DIR = PROJECT_ROOT / "models"

TARGET_COLUMN = "Exam_Score"

RANDOM_STATE = 42
TEST_SIZE = 0.20
```

---

# 22. Load Dataset

```python
df = load_data(DATA_PATH)

df.head()
```

Then:

```python
df.shape
```

Expected approximately:

```text
(6607, 20)
```

**Important:** Your EDA wording says 20 features + target, but your actual dataset shape needs to be verified. Don't hard-code assumptions from the report.

---

# 23. Validate Columns

Run:

```python
df.columns.tolist()
```

Then:

```python
df.info()
```

And:

```python
df.isna().sum()
```

We should confirm that the current raw dataset matches the dataset used for your EDA.

---

# 24. Separate X and y

```python
X = df.drop(columns=[TARGET_COLUMN])
y = df[TARGET_COLUMN]
```

Check:

```python
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
```

---

# 25. Feature Engineering

Now:

```python
X = create_features(X)
```

Check:

```python
X.head()
```

And:

```python
"Study_Attendance_Interaction" in X.columns
```

Expected:

```text
True
```

---

# 26. Define Numerical Features

Use:

```python
numerical_features = [
    "Hours_Studied",
    "Attendance",
    "Previous_Scores",
    "Sleep_Hours",
    "Tutoring_Sessions",
    "Physical_Activity",
    "Study_Attendance_Interaction",
]
```

Notice something important:

The engineered feature is numerical.

---

# 27. Define Categorical Features

```python
categorical_features = [
    "Parental_Involvement",
    "Access_to_Resources",
    "Extracurricular_Activities",
    "Motivation_Level",
    "Internet_Access",
    "Family_Income",
    "Teacher_Quality",
    "School_Type",
    "Peer_Influence",
    "Learning_Disabilities",
    "Parental_Education_Level",
    "Distance_from_Home",
    "Gender",
]
```

---

# 28. Validate Feature Lists

This is a very good engineering habit.

```python
all_features = numerical_features + categorical_features

missing_columns = set(all_features) - set(X.columns)

if missing_columns:
    raise ValueError(
        f"Missing expected columns: {missing_columns}"
    )

print("All expected features are present.")
```

---

# 29. Train-Test Split

Now:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
)
```

Check:

```python
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)
```

---

# 30. Why Do We Split Here?

This is critical.

We want:

```text
Training data
       ↓
Learn preprocessing parameters
       ↓
Transform training data
```

Then:

```text
Testing data
       ↓
Use already learned parameters
       ↓
Transform testing data
```

The test data must remain unseen during fitting.

---

# 31. Create the Preprocessor

```python
preprocessor = create_preprocessor(
    numerical_features=numerical_features,
    categorical_features=categorical_features,
)
```

---

# 32. Fit Only on Training Data

```python
X_train_processed = preprocessor.fit_transform(X_train)
```

Then:

```python
X_test_processed = preprocessor.transform(X_test)
```

### Notice the difference:

Training:

```python
fit_transform()
```

Testing:

```python
transform()
```

**Never:**

```python
preprocessor.fit_transform(X_test)
```

That would allow information from the test set to influence preprocessing.

---

# 33. Check Processed Shapes

```python
print(
    "Processed training shape:",
    X_train_processed.shape
)

print(
    "Processed testing shape:",
    X_test_processed.shape
)
```

The number of columns will be larger than the original 20-ish features because categorical features are one-hot encoded.

---

# 34. Check for Missing Values

Convert temporarily to DataFrame:

```python
X_train_processed_df = pd.DataFrame(
    X_train_processed
)

X_train_processed_df.isna().sum().sum()
```

Expected:

```text
0
```

Do the same for test:

```python
X_test_processed_df = pd.DataFrame(
    X_test_processed
)

X_test_processed_df.isna().sum().sum()
```

Expected:

```text
0
```

---

# 35. Inspect Feature Names

This is very useful.

```python
feature_names = preprocessor.get_feature_names_out()

print(feature_names)
```

You'll see names similar to:

```text
numerical__Hours_Studied
numerical__Attendance
numerical__Previous_Scores
...
categorical__Gender_Female
categorical__Gender_Male
...
```

This lets us understand exactly what the model receives.

---

# 36. Create a Readable Processed DataFrame

```python
X_train_processed_df = pd.DataFrame(
    X_train_processed,
    columns=feature_names,
    index=X_train.index,
)

X_test_processed_df = pd.DataFrame(
    X_test_processed,
    columns=feature_names,
    index=X_test.index,
)
```

Then:

```python
X_train_processed_df.head()
```

---

# 37. Save the Processed Dataset

For inspection/documentation purposes:

```python
processed_dir = PROJECT_ROOT / "data" / "processed"
processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

X_train_processed_df.to_csv(
    processed_dir / "X_train_processed.csv",
    index=False,
)

X_test_processed_df.to_csv(
    processed_dir / "X_test_processed.csv",
    index=False,
)
```

However, remember:

**These processed CSV files should normally remain out of GitHub** because they are generated artifacts.

---

# 38. Save the Preprocessing Pipeline

Create the models directory:

```python
MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)
```

Then:

```python
pipeline_path = (
    MODEL_DIR / "preprocessing_pipeline.joblib"
)

joblib.dump(
    preprocessor,
    pipeline_path
)

print(
    f"Preprocessing pipeline saved to: {pipeline_path}"
)
```

Now we have:

```text
models/
└── preprocessing_pipeline.joblib
```

---

# 39. Test Loading the Pipeline

Never assume that saving worked.

Test it:

```python
loaded_preprocessor = joblib.load(
    pipeline_path
)
```

Then:

```python
X_test_reloaded = loaded_preprocessor.transform(
    X_test
)
```

Check:

```python
X_test_reloaded.shape
```

It should match:

```python
X_test_processed.shape
```

---

# 40. Validate Reproducibility

You can check:

```python
import numpy as np

np.allclose(
    X_test_processed,
    X_test_reloaded
)
```

Expected:

```text
True
```

That's a nice little engineering validation.

---

# 41. What NOT to Do

Don't do this:

```python
X = pd.get_dummies(X)
X = (X - X.mean()) / X.std()
X_train, X_test = train_test_split(X)
```

Why?

Because you're manually preprocessing before splitting.

That can introduce leakage and makes production inference harder.

Instead:

```text
Raw X
 ↓
Split
 ↓
Pipeline
 ↓
Fit on train
 ↓
Transform train/test
```

---

# 42. Create `docs/preprocessing.md`

This document explains the decisions we made.

Structure:

```markdown
# Data Preprocessing

## 1. Objective

## 2. Feature Groups

### Numerical Features

### Categorical Features

## 3. Missing Value Handling

## 4. Outlier Strategy

## 5. Feature Engineering

## 6. Train-Test Split

## 7. Numerical Scaling

## 8. Categorical Encoding

## 9. Pipeline Architecture

## 10. Data Leakage Prevention

## 11. Output Artifacts

## 12. Validation

## 13. Limitations
```

We'll fill this properly after the code works.

---

# 43. Create `tests/test_preprocessing.py`

Don't make complicated tests yet.

Start with:

```python
import pandas as pd

from src.preprocessing import create_preprocessor


def test_preprocessor_creation():
    numerical_features = [
        "Hours_Studied",
        "Attendance",
    ]

    categorical_features = [
        "Gender",
    ]

    preprocessor = create_preprocessor(
        numerical_features,
        categorical_features,
    )

    assert preprocessor is not None
```

Later we'll add stronger tests.

---

# 44. Your Final Milestone 4 Structure

After everything is complete:

```text
student-performance-prediction/
│
├── data/
│   ├── raw/
│   │   └── StudentPerformanceFactors.csv
│   │
│   └── processed/
│       ├── X_train_processed.csv
│       └── X_test_processed.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_preprocessing.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   └── preprocessing.py
│
├── models/
│   └── preprocessing_pipeline.joblib
│
├── reports/
│   └── figures/
│
├── tests/
│   └── test_preprocessing.py
│
├── docs/
│   └── preprocessing.md
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# 45. What Goes to GitHub?

### ✅ Commit

```text
src/
notebooks/
tests/
docs/
README.md
requirements.txt
.gitignore
LICENSE
```

### ❌ Don't commit

```text
.venv/
data/raw/*.csv
data/processed/*.csv
models/*.joblib
```


---

# 46. Git Commit Strategy

### Commit 1

```bash
git add src/data_loader.py
git commit -m "Add dataset loading utility"
```

### Commit 2

```bash
git add src/feature_engineering.py
git commit -m "Add feature engineering pipeline"
```

### Commit 3

```bash
git add src/preprocessing.py
git commit -m "Add preprocessing pipeline"
```

### Commit 4

```bash
git add notebooks/02_preprocessing.ipynb
git commit -m "Add preprocessing notebook"
```

### Commit 5

```bash
git add tests/test_preprocessing.py docs/preprocessing.md
git commit -m "Add preprocessing tests and documentation"
```

This gives you a much better Git history than:

```text
initial commit
↓
everything project done
```

---

# 🧠 The Most Important Concept

I want you to understand the difference between these three things:

### Notebook

```text
02_preprocessing.ipynb
```

Used for:

**Experimentation + inspection + learning**

### Python module

```text
src/preprocessing.py
```

Used for:

**Reusable production logic**

### Saved artifact

```text
models/preprocessing_pipeline.joblib
```

Used for:

**Applying the exact learned transformations later**

That's the pattern we'll repeatedly use throughout your AI Engineer portfolio.

---

# 🔥 Final Architecture for This Milestone

```text
                    RAW CSV
                       │
                       ▼
                data_loader.py
                       │
                       ▼
                  Raw DataFrame
                       │
                       ▼
             Feature Engineering
                       │
                       ▼
             Separate X and y
                       │
                       ▼
               Train/Test Split
                  /          \
                 /            \
              TRAIN           TEST
                │               │
                ▼               │
        ┌────────────────┐     │
        │ PREPROCESSOR   │     │
        │                │     │
        │ Numerical:     │     │
        │ Imputer        │     │
        │ Scaler         │     │
        │                │     │
        │ Categorical:   │     │
        │ Imputer        │     │
        │ OneHotEncoder  │     │
        └───────┬────────┘     │
                │              │
          fit_transform        │
                │              │
                ▼              ▼
          X_train_processed  transform
                │              │
                └──────┬───────┘
                       ▼
                ML-READY DATA
                       │
                       ▼
        preprocessing_pipeline.joblib
```

---


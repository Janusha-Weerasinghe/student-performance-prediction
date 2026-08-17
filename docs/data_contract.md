# Data Contract

## Dataset

Student Performance Dataset

## Shape

- Rows: 6607
- Columns: 20

## Target

`Exam_Score`

## Numerical Features

- Hours_Studied
- Attendance
- Sleep_Hours
- Previous_Scores
- Tutoring_Sessions
- Physical_Activity

## Categorical Features

- Parental_Involvement
- Access_to_Resources
- Extracurricular_Activities
- Motivation_Level
- Internet_Access
- Family_Income
- Teacher_Quality
- School_Type
- Peer_Influence
- Learning_Disabilities
- Parental_Education_Level
- Distance_from_Home
- Gender

X
│
├── Numerical: 6
│
│   ├── Hours_Studied
│   ├── Attendance
│   ├── Sleep_Hours
│   ├── Previous_Scores
│   ├── Tutoring_Sessions
│   └── Physical_Activity
│
└── Categorical: 13
    │
    ├── Parental_Involvement
    ├── Access_to_Resources
    ├── Extracurricular_Activities
    ├── Motivation_Level
    ├── Internet_Access
    ├── Family_Income
    ├── Teacher_Quality
    ├── School_Type
    ├── Peer_Influence
    ├── Learning_Disabilities
    ├── Parental_Education_Level
    ├── Distance_from_Home
    └── Gender

y
│
└── Exam_Score

## Missing Values

| Feature | Missing |
|---|---:|
| Teacher_Quality | 78 |
| Parental_Education_Level | 90 |
| Distance_from_Home | 67 |

## Duplicates

0 duplicate rows detected.

## Preprocessing Strategy

To be implemented in M4:

- Numerical missing-value handling
- Numerical scaling
- Categorical missing-value handling
- Categorical encoding
- Train/test leakage prevention

# part 02

Yes bro. 🔥 **Next = we finish the numerical/data-quality part of the Data Contract before writing the validator.**

I checked the actual `student_performance.csv`, so we're going to distinguish **observed ranges** from **rules we are willing to enforce**. That distinction is important.

---

# 🔵 STAGE 2.1 — Numerical Data Contract

Our dataset has:

* **6,607 rows**
* **20 columns**
* **6 numerical input features**
* **13 categorical input features**
* **1 target**
---

# 1. Let's inspect each numerical feature

From the actual CSV:

| Feature             | Observed Min | Observed Max | Meaning / role              |
| ------------------- | -----------: | -----------: | --------------------------- |
| `Hours_Studied`     |            1 |           44 | Study hours                 |
| `Attendance`        |           60 |          100 | Attendance percentage       |
| `Sleep_Hours`       |            4 |           10 | Sleep hours                 |
| `Previous_Scores`   |           50 |          100 | Previous score              |
| `Tutoring_Sessions` |            0 |            8 | Number of tutoring sessions |
| `Physical_Activity` |            0 |            6 | Physical activity measure   |
| `Exam_Score`        |           55 |      **101** | Target                      |

These are **observed ranges**, meaning:

> "These are the values that actually occur in our current dataset."

They are **not automatically our validation rules**.

That's a very important distinction.

---

# 2. `Attendance`

Observed:

```text
60 → 100
```

This one is straightforward because the dataset represents attendance as a percentage.

A reasonable domain constraint is:

```text
0 <= Attendance <= 100
```

But our dataset happens to start at 60.

So:

```python
"Attendance": (0, 100)
```

is a **domain rule**, whereas:

```text
60 → 100
```

is only the **observed dataset range**.

We should not say that `Attendance = 50` is invalid simply because our current dataset doesn't contain it.

---

# 3. `Sleep_Hours`

Observed:

```text
4 → 10
```

We shouldn't blindly say:

```python
Sleep_Hours = 4..10
```

because that would encode the current dataset distribution as a universal business rule.

For example, someone sleeping 3 hours is unhealthy, but it is still a possible data value.

So for now:

```text
Type: integer
Missing: no
Observed range: 4–10
Validation: numeric/type validation
```

We can discuss domain constraints separately.

---

# 4. `Previous_Scores`

Observed:

```text
50 → 100
```

This appears to represent a score/percentage.

A sensible domain constraint could be:

```text
0 <= Previous_Scores <= 100
```

But again, we'll document that as a **domain assumption**, not pretend the CSV itself proves it.

---

# 5. `Tutoring_Sessions`

Observed:

```text
0 → 8
```

This is a count.

So:

```text
Tutoring_Sessions >= 0
```

makes sense.

It should also be an integer.

Therefore:

```text
Type: integer
Constraint: non-negative
Observed: 0–8
```

---

# 6. `Physical_Activity`

Observed:

```text
0 → 6
```

This one requires more caution.

We know the column is numeric, but the CSV alone doesn't tell us exactly what the scale means.

It could represent:

```text
days per week
```

or another activity measure.

Therefore **we should not invent a semantic range** yet.

Our contract can safely say:

```text
Type: integer
Observed: 0–6
```

and we'll investigate the dataset documentation before deciding whether:

```python
0 <= Physical_Activity <= 6
```

should become a hard validation rule.

---

# 7. 🚨 `Exam_Score` — the interesting one

The target has:

```text
Min = 55
Max = 101
```

At first glance, `101` looks suspicious.

And there is exactly **one row** with:

```text
Exam_Score = 101
```

The row is:

```text
Hours_Studied = 27
Attendance = 98
Previous_Scores = 93
...
Exam_Score = 101
```

So we have discovered something important.

---

# ❌ Should we immediately delete the 101?

**NO.**

This is exactly the kind of decision I don't want you making blindly.

We don't yet have enough evidence to say:

> "101 is definitely a bad record."

It could be:

1. a dataset generation artifact,
2. an incorrect value,
3. a data-entry issue,
4. an intentional outlier,
5. something documented by the dataset source.

Therefore:

```text
101 ≠ automatically delete
```

Instead:

```text
101
 ↓
Data-quality flag
 ↓
Investigate
 ↓
Document decision
```

That's a much more professional approach.

---

# 🧠 This is an important ML concept

There are three different concepts:

### 1. Invalid value

Example:

```text
Attendance = 250%
```

Clearly violates the domain.

### 2. Outlier

Example:

```text
Hours_Studied = 44
```

Unusual, but not necessarily invalid.

### 3. Suspicious value

Example:

```text
Exam_Score = 101
```

Requires investigation.

These are **not interchangeable**.

---

# 8. Our current contract should therefore be conservative

I'm proposing this first version:

```python
TARGET_COLUMN = "Exam_Score"

NUMERICAL_FEATURES = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Scores",
    "Tutoring_Sessions",
    "Physical_Activity",
]

CATEGORICAL_FEATURES = [
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

Then our **initial validation rules** are:

```text
Schema
  ├── Required columns exist
  ├── No target missing
  └── Expected feature groups exist

Numerical
  ├── Expected numeric dtype
  ├── No unexpected missing values
  └── Domain checks where justified

Categorical
  ├── Expected categorical/string values
  └── Missing values allowed for selected columns

Target
  ├── Numeric
  ├── Not missing
  └── Investigate suspicious values such as 101
```

---

# 9. Categorical contract

We already discovered the allowed observed categories.

For example:

### `Motivation_Level`

```text
Low
Medium
High
```

### `Gender`

```text
Male
Female
```

### `Internet_Access`

```text
Yes
No
```

### `School_Type`

```text
Public
Private
```

And:

### `Distance_from_Home`

```text
Near
Moderate
Far
```

But remember:

**Observed categories are not necessarily the complete future domain.**

For example, if tomorrow production receives:

```text
Unknown
```

our preprocessing pipeline should not simply crash.

That's why later we'll use an encoder configuration that can handle previously unseen categories appropriately.

---

# 10. Missing-value contract

We found:

```text
Teacher_Quality             78
Parental_Education_Level    90
Distance_from_Home          67
```

Total:

```text
235 missing cells
```

The missing values are **categorical**, not numerical.

So our planned preprocessing is:

```text
Categorical
       │
       ▼
SimpleImputer(strategy="most_frequent")
       │
       ▼
OneHotEncoder(...)
```

But **we won't implement this yet**.

First we're defining the contract.

---

# 11. What should happen to duplicates?

We found:

```text
Duplicate rows = 0
```

But that doesn't mean our pipeline doesn't need duplicate checking.

Our validation layer should be capable of reporting:

```text
duplicate_count
```

rather than silently deleting records.

Why?

Because duplicate removal is a **data policy decision**, not merely a technical operation.

For example:

```text
10 identical rows
```

could mean:

* duplicate ingestion,
* legitimate repeated observations,
* or an actual data-generation issue.

So initially:

```text
Validator → report duplicates
```

rather than:

```text
Validator → automatically delete duplicates
```

---

# 12. 🏗️ Our Data Contract v1

This is what I want you to understand before we code.

```text
┌──────────────────────────────────────┐
│          DATA CONTRACT v1            │
├──────────────────────────────────────┤
│ Dataset shape: 6607 × 20             │
│                                      │
│ Target: Exam_Score                   │
│                                      │
│ Numerical features: 6                │
│ Categorical features: 13             │
│                                      │
│ Required checks:                     │
│                                      │
│ ✓ Required columns                   │
│ ✓ Data types                         │
│ ✓ Missing target                     │
│ ✓ Missing feature values             │
│ ✓ Duplicate records                  │
│ ✓ Categorical values                 │
│ ✓ Numeric values                     │
│ ✓ Suspicious target values           │
│                                      │
│ No automatic row deletion yet        │
└──────────────────────────────────────┘
```

---

# 13.Now we move from theory → engineering

We're finally ready to write actual code.

But I want to do it **in small steps**.

## Next file:

```text
src/validation.py
```

Currently it is basically just:

```python
"""Dataset validation utilities."""
```

We're going to turn that into a proper validation module.

But first, I want to understand the design.

We'll have something conceptually like:

```python
def validate_schema(df):
    ...
```

and eventually:

```python
def validate_dataset(df):
    ...
```

The flow will be:

```text
DataFrame
    │
    ▼
validate_schema()
    │
    ├── columns?
    ├── target?
    ├── numerical types?
    └── categorical fields?
    │
    ▼
validate_quality()
    │
    ├── missing values
    ├── duplicates
    └── suspicious values
    │
    ▼
Validation Result
```

---

# learning checkpoint

### Q1.

What's the difference between:

```text
observed range
```

and:

```text
validation constraint
```

### Q2.

Why shouldn't we automatically delete `Exam_Score = 101`?

### Q3.

Why are missing values in `Teacher_Quality` going to be handled later by the preprocessing pipeline rather than simply deleting those rows?

### Q4.

Why shouldn't we automatically delete duplicate rows?

### Q5.

Why is `Exam_Score` excluded from `NUMERICAL_FEATURES` even though its dtype is `int64`?

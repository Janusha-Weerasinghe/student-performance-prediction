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
"""Dataset validation utilities."""

import pandas as pd #Because our validator receives a Pandas:


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
#df is expected to be a Pandas DataFrame.
# -> None is If validation succeeds, this function doesn't return a value.

EXPECTED_COLUMNS = (
    NUMERICAL_FEATURES
    + CATEGORICAL_FEATURES
    + [TARGET_COLUMN]
)


def validate_required_columns(df: pd.DataFrame) -> None:
    """Validate that all required project columns are present."""
    missing_columns = [
        column
        for column in EXPECTED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


def validate_target(df: pd.DataFrame) -> None:
    """Validate the target column."""
    if df[TARGET_COLUMN].isna().any():
        raise ValueError(
            f"Target column '{TARGET_COLUMN}' contains missing values."
        )

    if not pd.api.types.is_numeric_dtype(df[TARGET_COLUMN]):
        raise TypeError(
            f"Target column '{TARGET_COLUMN}' must be numeric."
        )


def validate_numerical_features(df: pd.DataFrame) -> None:
    """Validate numerical feature data types."""
    invalid_features = [
        column
        for column in NUMERICAL_FEATURES
        if not pd.api.types.is_numeric_dtype(df[column])
    ]

    if invalid_features:
        raise TypeError(
            f"Numerical features with invalid dtypes: {invalid_features}"
        )


def validate_duplicates(df: pd.DataFrame) -> None:
    """Validate that the dataset does not contain duplicate rows."""
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        raise ValueError(
            f"Dataset contains {duplicate_count} duplicate rows."
        )


def validate_dataset(df: pd.DataFrame) -> None:
    """Run all dataset validation checks."""
    validate_required_columns(df)
    validate_target(df)
    validate_numerical_features(df)
    validate_duplicates(df)
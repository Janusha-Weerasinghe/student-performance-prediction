"""Data preprocessing utilities for the student performance project."""

import pandas as pd
from sklearn.model_selection import train_test_split

from src.validation import TARGET_COLUMN

#04.3.1 — Numerical preprocessing
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def split_features_target(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Separate input features from the target variable.

    Args:
        df: Validated student performance DataFrame.

    Returns:
        A tuple containing:
        - X: Feature DataFrame.
        - y: Target Series.
    """
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    return X, y


def split_train_test(
    X: pd.DataFrame,
    y: pd.Series,
) -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.Series,
    pd.Series,
]:
    """
    Split features and target into training and testing sets.

    Args:
        X: Feature DataFrame.
        y: Target Series.

    Returns:
        A tuple containing:
        - X_train: Training features.
        - X_test: Testing features.
        - y_train: Training targets.
        - y_test: Testing targets.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    return X_train, X_test, y_train, y_test

def create_numerical_pipeline() -> Pipeline:
    """Create the preprocessing pipeline for numerical features."""
    return Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
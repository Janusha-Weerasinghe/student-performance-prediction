"""Data preprocessing utilities for the student performance project."""

import pandas as pd

from src.validation import TARGET_COLUMN


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
"""Tests for preprocessing utilities."""

import pandas as pd

from src.preprocessing import split_features_target
from src.validation import (
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
    TARGET_COLUMN,
)


def create_valid_dataframe() -> pd.DataFrame:
    """Create a minimal valid DataFrame for preprocessing tests."""
    data = {}

    for column in NUMERICAL_FEATURES:
        data[column] = [10, 20]

    for column in CATEGORICAL_FEATURES:
        data[column] = ["Low", "High"]

    data[TARGET_COLUMN] = [70, 80]

    return pd.DataFrame(data)


def test_split_features_target() -> None:
    """Verify that features and target are separated correctly."""
    df = create_valid_dataframe()

    X, y = split_features_target(df)

    assert TARGET_COLUMN not in X.columns
    assert y.name == TARGET_COLUMN
    assert len(X) == len(y)
    assert len(X.columns) == 19
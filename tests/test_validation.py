"""Tests for dataset validation utilities."""

import pandas as pd
import pytest

from src.validation import (
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
    TARGET_COLUMN,
    validate_dataset,
)


def create_valid_dataframe() -> pd.DataFrame:
    """Create a minimal valid DataFrame for validation tests."""
    data = {}

    for column in NUMERICAL_FEATURES:
        data[column] = [10, 20]

    for column in CATEGORICAL_FEATURES:
        data[column] = ["Low", "High"]

    data[TARGET_COLUMN] = [70, 80]

    return pd.DataFrame(data)


def test_validate_dataset_accepts_valid_data() -> None:
    """Valid data should pass all validation checks."""
    df = create_valid_dataframe()

    validate_dataset(df)


def test_validate_dataset_rejects_missing_column() -> None:
    """A missing required column should raise ValueError."""
    df = create_valid_dataframe()

    df = df.drop(columns=[TARGET_COLUMN])

    with pytest.raises(
        ValueError,
        match="Missing required columns",
    ):
        validate_dataset(df)


def test_validate_dataset_rejects_missing_target() -> None:
    """A missing target value should raise ValueError."""
    df = create_valid_dataframe()

    df.loc[0, TARGET_COLUMN] = None

    with pytest.raises(
        ValueError,
        match="contains missing values",
    ):
        validate_dataset(df)


def test_validate_dataset_rejects_invalid_numerical_dtype() -> None:
    """A numerical feature with a non-numeric dtype should raise TypeError."""
    df = create_valid_dataframe()

    df["Hours_Studied"] = ["ten", "twenty"]

    with pytest.raises(
        TypeError,
        match="invalid dtypes",
    ):
        validate_dataset(df)


def test_validate_dataset_rejects_duplicates() -> None:
    """Duplicate rows should raise ValueError."""
    df = create_valid_dataframe()

    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

    with pytest.raises(
        ValueError,
        match="duplicate rows",
    ):
        validate_dataset(df)
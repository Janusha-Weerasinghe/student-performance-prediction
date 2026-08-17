"""Utilities for loading project datasets."""

from pathlib import Path

import pandas as pd


def load_dataset(file_path: str | Path) -> pd.DataFrame:
    """
    Load the student performance dataset from a CSV file.

    Args:
        file_path: Path to the CSV dataset.

    Returns:
        A pandas DataFrame containing the dataset.

    Raises:
        FileNotFoundError: If the dataset does not exist.
        ValueError: If the loaded dataset is empty.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("Dataset is empty.")

    return df
"""Tests for the dataset loading utility."""

from pathlib import Path

import pandas as pd
import pytest

from src.data_loader import load_dataset


def test_load_dataset(tmp_path: Path) -> None:
    """Verify that a valid CSV file can be loaded."""
    file_path = tmp_path / "test.csv"

    pd.DataFrame(
        {
            "Exam_Score": [70, 80, 90],
        }
    ).to_csv(file_path, index=False)

    df = load_dataset(file_path)

    assert len(df) == 3
    assert "Exam_Score" in df.columns


def test_load_dataset_missing_file() -> None:
    """Verify that a missing dataset raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_dataset("does-not-exist.csv")
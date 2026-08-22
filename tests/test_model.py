"""Tests for machine learning model utilities."""

from sklearn.linear_model import LinearRegression

from src.model import create_baseline_model


def test_create_baseline_model() -> None:
    """Verify that the baseline model is created correctly."""
    model = create_baseline_model()

    assert isinstance(model, LinearRegression)
"""Tests for machine learning model utilities."""

import numpy as np

from sklearn.linear_model import LinearRegression

from src.model import create_baseline_model, train_model


def test_create_baseline_model() -> None:
    """Verify that the baseline model is created correctly."""
    model = create_baseline_model()

    assert isinstance(model, LinearRegression)

def test_train_model() -> None:
    """Verify that the baseline model can be trained."""
    model = create_baseline_model()

    X_train = np.array(
        [
            [1.0],
            [2.0],
            [3.0],
            [4.0],
        ]
    )

    y_train = np.array(
        [2.0, 4.0, 6.0, 8.0]
    )

    trained_model = train_model(
        model,
        X_train,
        y_train,
    )

    assert trained_model is model
    assert hasattr(trained_model, "coef_")
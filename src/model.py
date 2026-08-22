"""Machine learning model utilities."""

from typing import Any

from sklearn.linear_model import LinearRegression

def create_baseline_model() -> LinearRegression:
    """Create the baseline linear regression model."""
    
    return LinearRegression()

def train_model(
    model: Any,
    X_train: Any,
    y_train: Any,
) -> Any:
    """
    Train the model using the training data.

    Args:
        model: Machine learning estimator.
        X_train: Training feature matrix.
        y_train: Training target values.

    Returns:
        The trained machine learning model.
    """
    model.fit(X_train, y_train)

    return model
"""Machine learning model utilities."""

from sklearn.linear_model import LinearRegression

def create_baseline_model() -> LinearRegression:
    """Create the baseline linear regression model."""
    return LinearRegression()
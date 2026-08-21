"""Tests for preprocessing utilities."""

import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.compose import ColumnTransformer

#from src.preprocessing import split_features_target

# from src.preprocessing import (
#     split_features_target,
#     split_train_test,
# )
from src.validation import (
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
    TARGET_COLUMN,
)

# from src.preprocessing import (
#     create_numerical_pipeline,
#     split_features_target,
#     split_train_test,
# )

# from src.preprocessing import (
#     create_categorical_pipeline,
#     create_numerical_pipeline,
#     split_features_target,
#     split_train_test,
# )

# from src.preprocessing import (
#     create_categorical_pipeline,
#     create_numerical_pipeline,
#     create_preprocessor,
#     split_features_target,
#     split_train_test,
# )

# 04.3.4.2 — Test it
from src.preprocessing import (
    create_categorical_pipeline,
    create_numerical_pipeline,
    create_preprocessor,
    fit_preprocessor,
    split_features_target,
    split_train_test,
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

def test_split_train_test() -> None:
    """Verify that the dataset is split into training and testing sets."""
    df = create_valid_dataframe()

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = split_train_test(X, y)

    assert len(X_train) == 1
    assert len(X_test) == 1
    assert len(y_train) == 1
    assert len(y_test) == 1

    assert len(X_train) + len(X_test) == len(X)
    assert len(y_train) + len(y_test) == len(y)

def test_split_train_test_is_reproducible() -> None:
    """Verify that the same random state produces the same split."""
    df = create_valid_dataframe()

    X, y = split_features_target(df)

    first_split = split_train_test(X, y)
    second_split = split_train_test(X, y)

    for first, second in zip(first_split, second_split):
        pd.testing.assert_frame_equal(
            first,
            second,
        ) if isinstance(first, pd.DataFrame) else pd.testing.assert_series_equal(
            first,
            second,
        )

def test_split_train_test_is_reproducible() -> None:
    """Verify that the same random state produces the same split."""
    df = create_valid_dataframe()

    X, y = split_features_target(df)

    first_split = split_train_test(X, y)
    second_split = split_train_test(X, y)

    X_train_1, X_test_1, y_train_1, y_test_1 = first_split
    X_train_2, X_test_2, y_train_2, y_test_2 = second_split

    pd.testing.assert_frame_equal(X_train_1, X_train_2)
    pd.testing.assert_frame_equal(X_test_1, X_test_2)
    pd.testing.assert_series_equal(y_train_1, y_train_2)
    pd.testing.assert_series_equal(y_test_1, y_test_2)

def test_create_numerical_pipeline() -> None:
    """Verify that the numerical preprocessing pipeline is configured correctly."""
    pipeline = create_numerical_pipeline()

    assert list(pipeline.named_steps.keys()) == [
        "imputer",
        "scaler",
    ]

    assert isinstance(
        pipeline.named_steps["imputer"],
        SimpleImputer,
    )

    assert pipeline.named_steps["imputer"].strategy == "median"

    assert isinstance(
        pipeline.named_steps["scaler"],
        StandardScaler,
    )

def test_create_categorical_pipeline() -> None:
    """Verify that the categorical preprocessing pipeline is configured correctly."""
    pipeline = create_categorical_pipeline()

    assert list(pipeline.named_steps.keys()) == [
        "imputer",
        "encoder",
    ]

    assert isinstance(
        pipeline.named_steps["imputer"],
        SimpleImputer,
    )

    assert pipeline.named_steps["imputer"].strategy == "most_frequent"

    assert isinstance(
        pipeline.named_steps["encoder"],
        OneHotEncoder,
    )

    assert pipeline.named_steps["encoder"].handle_unknown == "ignore"

def test_create_preprocessor() -> None:
    """Verify that numerical and categorical pipelines are combined correctly."""
    preprocessor = create_preprocessor()

    assert isinstance(
        preprocessor,
        ColumnTransformer,
    )

    assert len(preprocessor.transformers) == 2

    transformer_names = [
        name
        for name, _, _ in preprocessor.transformers
    ]

    assert transformer_names == [
        "numerical",
        "categorical",
    ]

def test_preprocessor_uses_correct_feature_groups() -> None:
    """Verify that each pipeline receives the correct feature columns."""
    preprocessor = create_preprocessor()

    numerical_columns = preprocessor.transformers[0][2]
    categorical_columns = preprocessor.transformers[1][2]

    assert numerical_columns == NUMERICAL_FEATURES
    assert categorical_columns == CATEGORICAL_FEATURES

def test_fit_preprocessor() -> None:
    """Verify that the preprocessor can fit and transform train/test data."""
    df = create_valid_dataframe()

    X, y = split_features_target(df)

    X_train, X_test, _, _ = split_train_test(X, y)

    preprocessor = create_preprocessor()

    X_train_processed, X_test_processed = fit_preprocessor(
        preprocessor,
        X_train,
        X_test,
    )

    assert X_train_processed.shape[0] == len(X_train)
    assert X_test_processed.shape[0] == len(X_test)

def test_fit_preprocessor_handles_missing_values() -> None:
    """Verify that preprocessing handles missing values."""
    df = create_valid_dataframe()

    df = pd.concat([df] * 10, ignore_index=True)

    df.loc[0, "Hours_Studied"] = None
    df.loc[1, "Gender"] = None

    X, y = split_features_target(df)

    X_train, X_test, _, _ = split_train_test(X, y)

    preprocessor = create_preprocessor()

    X_train_processed, X_test_processed = fit_preprocessor(
        preprocessor,
        X_train,
        X_test,
    )

    assert X_train_processed.shape[0] == len(X_train)
    assert X_test_processed.shape[0] == len(X_test)
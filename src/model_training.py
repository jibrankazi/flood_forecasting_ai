"""
model_training.py
=================

This module encapsulates training and evaluation of machine
learning models for flood prediction.  It provides simple
wrappers around scikit‑learn’s API so that model training can be
performed programmatically outside of notebooks.

The default model implemented here is a RandomForestClassifier,
which performs well on tabular datasets and handles nonlinear
relationships and interactions.  Additional models can be added as
needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, roc_auc_score)
from sklearn.model_selection import train_test_split


@dataclass
class ModelResults:
    model: RandomForestClassifier
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series
    y_pred: np.ndarray
    accuracy: float
    roc_auc: float
    confusion: np.ndarray
    report: str


def train_random_forest(features: pd.DataFrame, target: pd.Series) -> ModelResults:
    """Train a RandomForest classifier on the given features and target.

    The data is split into training and testing sets using a
    chronological 80/20 split to avoid data leakage when working
    with time series.  A basic set of hyperparameters is used to
    balance class imbalance and encourage generalisation.

    Parameters
    ----------
    features : pandas.DataFrame
        Feature matrix with numeric predictor variables.
    target : pandas.Series
        Binary target variable.

    Returns
    -------
    ModelResults
        Dataclass containing the fitted model and various
        performance metrics on the test set.
    """
    # Ensure numeric data types
    X = features.astype(float)
    y = target.astype(int)
    # Chronological split based on index order
    split_idx = int(len(X) * 0.8)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
    # Train model
    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        class_weight='balanced',
        random_state=42,
        n_jobs=-1,
    )
    clf.fit(X_train, y_train)
    # Predict
    y_pred = clf.predict(X_test)
    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    # Compute ROC AUC only if both classes present
    roc_auc = 0.0
    try:
        y_prob = clf.predict_proba(X_test)[:, 1]
        roc_auc = roc_auc_score(y_test, y_prob)
    except Exception:
        pass
    conf_mat = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return ModelResults(
        model=clf,
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        y_pred=y_pred,
        accuracy=accuracy,
        roc_auc=roc_auc,
        confusion=conf_mat,
        report=report,
    )
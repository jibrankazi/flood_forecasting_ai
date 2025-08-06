"""
visualization.py
================

Utilities for generating plots and other visual outputs used in the
flood forecasting project.  These functions rely on matplotlib and
seaborn to produce static images that can be saved to disk and
uploaded to the `visualizations/` directory in the repository.

While the blueprint mentions proprietary tools like PowerBI or
Tableau, the current environment does not support these.  Instead
we use open‑source libraries to produce comparable plots.  Users
can import the saved PNG files into their preferred BI platform if
desired.
"""

from __future__ import annotations

import os
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_time_series(df: pd.DataFrame, date_col: str, value_col: str,
                     title: str, output_path: Optional[str] = None) -> None:
    """Plot a simple time series of a single variable.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the data to plot.
    date_col : str
        Name of the column containing datetime objects.
    value_col : str
        Name of the column to plot on the y‑axis.
    title : str
        Title for the chart.
    output_path : str, optional
        Path where the PNG file should be saved.  If None the plot
        is displayed but not saved.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df[date_col], df[value_col], color='steelblue')
    plt.xlabel('Date')
    plt.ylabel(value_col)
    plt.title(title)
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, dpi=300)
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame, output_path: Optional[str] = None) -> None:
    """Plot a correlation heatmap of numeric features in a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing numeric variables for correlation analysis.
    output_path : str, optional
        Path where the PNG file should be saved.  If None the plot
        is displayed but not saved.
    """
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, cmap='coolwarm', center=0, annot=False)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, dpi=300)
    plt.close()


def plot_predicted_flood_events(dates: pd.Series, preds: pd.Series,
                                title: str, output_path: Optional[str] = None) -> None:
    """Plot a binary sequence of predicted flood events over time.

    Parameters
    ----------
    dates : pandas.Series
        Series of datetime objects representing each observation.
    preds : pandas.Series
        Binary predictions (0 or 1) indicating flood/no flood.
    title : str
        Chart title.
    output_path : str, optional
        Path where the PNG file should be saved.  If None the plot
        is displayed but not saved.
    """
    plt.figure(figsize=(10, 2))
    plt.scatter(dates, preds, c=preds, cmap='Reds', marker='|', s=100)
    plt.yticks([0, 1], ['No Flood', 'Flood'])
    plt.xlabel('Date')
    plt.title(title)
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, dpi=300)
    plt.close()
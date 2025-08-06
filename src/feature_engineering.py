"""
feature_engineering.py
======================

This module defines utilities to transform raw environmental data
into a richer set of features suitable for machine learning models.
Functions in this file mirror the transformations applied in the
feature engineering notebook but are written as pure Python
functions to facilitate reproducible pipelines.

Example
-------

>>> from data_ingestion import download_weather_data
>>> from feature_engineering import engineer_weather_features
>>> df_raw = download_weather_data(31688, [2019, 2020])
>>> df_features = engineer_weather_features(df_raw)
>>> print(df_features.columns)

The resulting DataFrame will include lagged precipitation values,
cumulative rainfall totals and cyclic encodings of the day and
month.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def engineer_weather_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create derived features from a raw weather DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw weather observations.  Must include a `Date/Time` column,
        `Total Precip (mm)` and `Mean Temp (°C)`.

    Returns
    -------
    pandas.DataFrame
        DataFrame augmented with engineered features including lagged
        precipitation, rolling sums and cyclical encodings.
    """
    data = df.copy()
    # Ensure date column is datetime and sorted
    data['Date'] = pd.to_datetime(data['Date/Time'])
    data = data.sort_values('Date').reset_index(drop=True)
    # Rename columns to easier names
    if 'Total Precip (mm)' in data.columns:
        data.rename(columns={'Total Precip (mm)': 'Precipitation'}, inplace=True)
    if 'Mean Temp (°C)' in data.columns:
        data.rename(columns={'Mean Temp (°C)': 'Mean_Temp'}, inplace=True)
    # Fill missing values
    data['Precipitation'] = data['Precipitation'].fillna(0)
    data['Mean_Temp'] = data['Mean_Temp'].fillna(method='ffill').fillna(method='bfill')
    # Lagged features
    data['Precip_Last_Day'] = data['Precipitation'].shift(1).fillna(0)
    data['Mean_Temp_Last_Day'] = data['Mean_Temp'].shift(1).fillna(data['Mean_Temp'])
    # Rolling sums of precipitation
    data['Precip_3d_Sum'] = data['Precipitation'].rolling(window=3, min_periods=1).sum()
    data['Precip_7d_Sum'] = data['Precipitation'].rolling(window=7, min_periods=1).sum()
    # Cyclical encodings for day of year and month of year
    data['DayOfYear'] = data['Date'].dt.dayofyear
    data['Month'] = data['Date'].dt.month
    data['DayOfYear_sin'] = np.sin(2 * np.pi * data['DayOfYear'] / 365.25)
    data['DayOfYear_cos'] = np.cos(2 * np.pi * data['DayOfYear'] / 365.25)
    data['Month_sin'] = np.sin(2 * np.pi * data['Month'] / 12.0)
    data['Month_cos'] = np.cos(2 * np.pi * data['Month'] / 12.0)
    # Drop original string date columns
    data = data.drop(columns=['Date/Time'])
    return data


def create_target(data: pd.DataFrame, threshold_mm: float = 10.0) -> pd.DataFrame:
    """Add a binary flood risk target column to the feature DataFrame.

    Parameters
    ----------
    data : pandas.DataFrame
        Feature DataFrame returned by `engineer_weather_features`.
    threshold_mm : float, optional
        Precipitation threshold (in mm) above which the next day is
        considered a potential flood event.  Default is 10 mm.

    Returns
    -------
    pandas.DataFrame
        DataFrame with an additional `Flood_Event_Imminent` column
        indicating whether the precipitation on the following day
        exceeds the given threshold.
    """
    df = data.copy()
    # Define target as precipitation for next day exceeding threshold
    df['Precip_Next_Day'] = df['Precipitation'].shift(-1).fillna(0)
    df['Flood_Event_Imminent'] = (df['Precip_Next_Day'] >= threshold_mm).astype(int)
    df = df.drop(columns=['Precip_Next_Day'])
    return df
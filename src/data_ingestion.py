"""
data_ingestion.py
===================

This module contains functions for programmatically downloading and
loading environmental datasets required for the flood forecasting
project.  Functions are designed to be reusable and to encapsulate
data‑acquisition logic separate from notebooks or model code.

At present the primary source implemented here is Environment and
Climate Change Canada’s bulk weather API, which provides historical
weather data for Canadian weather stations as CSV files.  The
`download_weather_data` function fetches daily weather data for a
given station and range of years, returning a pandas DataFrame.

Example
-------

>>> from data_ingestion import download_weather_data
>>> df = download_weather_data(station_id=31688, years=[2019, 2020])
>>> print(df.head())

The returned DataFrame includes columns such as `Date/Time`,
`Mean Temp (°C)`, `Total Precip (mm)` and others.

Note: For additional data sources (hydrometric, topographic, etc.)
similar functions can be added here following the same pattern.
"""

from __future__ import annotations

import io
import logging
from typing import Iterable, List

import pandas as pd
import requests

logger = logging.getLogger(__name__)


def download_weather_data(station_id: int, years: Iterable[int]) -> pd.DataFrame:
    """Download daily weather data for a given station and years.

    Parameters
    ----------
    station_id : int
        The Environment Canada station ID (e.g. 31688 for Toronto City Centre).
    years : Iterable[int]
        Years for which to download data.  Each year will be requested
        separately and concatenated into a single DataFrame.

    Returns
    -------
    pandas.DataFrame
        Combined weather data across all requested years.

    Notes
    -----
    The bulk data download service requires constructing a URL with
    query parameters specifying the station and date range.  If the
    service is unavailable or returns a non‑200 status code the
    function will raise an HTTPError.
    """
    frames: List[pd.DataFrame] = []
    for year in years:
        url = (
            "https://climate-data.canada.ca/doc/cron_download/download"
            f"?stationID={station_id}&Year={year}&Month=1&Day=1&format=csv&timeframe=2&submit=Download+Data"
        )
        logger.info("Downloading data for year %s", year)
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        # The CSV is returned in the response body
        df_year = pd.read_csv(io.StringIO(response.text))
        frames.append(df_year)
    # Concatenate all years together
    combined = pd.concat(frames, ignore_index=True)
    return combined
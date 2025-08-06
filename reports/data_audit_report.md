# Data Audit Report

## Dataset Shape

Total rows: 731

Total columns: 32

## Column Types

- **Longitude (x)**: float64
- **Latitude (y)**: float64
- **Station Name**: object
- **Climate ID**: int64
- **Date/Time**: object
- **Year**: int64
- **Month**: int64
- **Day**: int64
- **Data Quality**: float64
- **Max Temp (°C)**: float64
- **Max Temp Flag**: object
- **Min Temp (°C)**: float64
- **Min Temp Flag**: object
- **Mean Temp (°C)**: float64
- **Mean Temp Flag**: object
- **Heat Deg Days (°C)**: float64
- **Heat Deg Days Flag**: object
- **Cool Deg Days (°C)**: float64
- **Cool Deg Days Flag**: object
- **Total Rain (mm)**: float64
- **Total Rain Flag**: float64
- **Total Snow (cm)**: float64
- **Total Snow Flag**: float64
- **Total Precip (mm)**: float64
- **Total Precip Flag**: object
- **Snow on Grnd (cm)**: float64
- **Snow on Grnd Flag**: float64
- **Dir of Max Gust (10s deg)**: float64
- **Dir of Max Gust Flag**: object
- **Spd of Max Gust (km/h)**: float64
- **Spd of Max Gust Flag**: object
- **DownloadYear**: int64

## Missing Values

- **Longitude (x)**: 0 missing (0.00%)
- **Latitude (y)**: 0 missing (0.00%)
- **Station Name**: 0 missing (0.00%)
- **Climate ID**: 0 missing (0.00%)
- **Date/Time**: 0 missing (0.00%)
- **Year**: 0 missing (0.00%)
- **Month**: 0 missing (0.00%)
- **Day**: 0 missing (0.00%)
- **Data Quality**: 731 missing (100.00%)
- **Max Temp (°C)**: 7 missing (0.96%)
- **Max Temp Flag**: 724 missing (99.04%)
- **Min Temp (°C)**: 7 missing (0.96%)
- **Min Temp Flag**: 724 missing (99.04%)
- **Mean Temp (°C)**: 7 missing (0.96%)
- **Mean Temp Flag**: 724 missing (99.04%)
- **Heat Deg Days (°C)**: 7 missing (0.96%)
- **Heat Deg Days Flag**: 724 missing (99.04%)
- **Cool Deg Days (°C)**: 7 missing (0.96%)
- **Cool Deg Days Flag**: 724 missing (99.04%)
- **Total Rain (mm)**: 731 missing (100.00%)
- **Total Rain Flag**: 731 missing (100.00%)
- **Total Snow (cm)**: 731 missing (100.00%)
- **Total Snow Flag**: 731 missing (100.00%)
- **Total Precip (mm)**: 7 missing (0.96%)
- **Total Precip Flag**: 724 missing (99.04%)
- **Snow on Grnd (cm)**: 489 missing (66.89%)
- **Snow on Grnd Flag**: 731 missing (100.00%)
- **Dir of Max Gust (10s deg)**: 731 missing (100.00%)
- **Dir of Max Gust Flag**: 0 missing (0.00%)
- **Spd of Max Gust (km/h)**: 731 missing (100.00%)
- **Spd of Max Gust Flag**: 0 missing (0.00%)
- **DownloadYear**: 0 missing (0.00%)

## Descriptive Statistics (Numeric Columns)

                           count          mean           std         min         25%         50%         75%         max
Longitude (x)              731.0 -7.940000e+01  1.422058e-14      -79.40      -79.40      -79.40      -79.40      -79.40
Latitude (y)               731.0  4.367000e+01  7.110292e-15       43.67       43.67       43.67       43.67       43.67
Climate ID                 731.0  6.158355e+06  0.000000e+00  6158355.00  6158355.00  6158355.00  6158355.00  6158355.00
Year                       731.0  2.019501e+03  5.003419e-01     2019.00     2019.00     2020.00     2020.00     2020.00
Month                      731.0  6.519836e+00  3.451913e+00        1.00        4.00        7.00       10.00       12.00
Day                        731.0  1.573871e+01  8.809949e+00        1.00        8.00       16.00       23.00       31.00
Data Quality                 0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
Max Temp (°C)              724.0  1.358881e+01  1.070923e+01      -14.20        4.50       12.80       23.40       35.50
Min Temp (°C)              724.0  5.901796e+00  9.643042e+00      -21.50       -0.90        5.50       14.30       23.80
Mean Temp (°C)             724.0  9.746271e+00  1.007982e+01      -17.90        2.00        8.95       19.00       29.40
Heat Deg Days (°C)         724.0  9.472790e+00  8.529360e+00        0.00        0.00        9.05       16.00       35.90
Cool Deg Days (°C)         724.0  1.219061e+00  2.392715e+00        0.00        0.00        0.00        1.00       11.40
Total Rain (mm)              0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
Total Rain Flag              0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
Total Snow (cm)              0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
Total Snow Flag              0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
Total Precip (mm)          724.0  2.379420e+00  5.330556e+00        0.00        0.00        0.30        1.50       55.30
Snow on Grnd (cm)          242.0  4.318182e+00  5.149427e+00        0.00        1.00        2.00        6.00       29.00
Snow on Grnd Flag            0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
Dir of Max Gust (10s deg)    0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
Spd of Max Gust (km/h)       0.0           NaN           NaN         NaN         NaN         NaN         NaN         NaN
DownloadYear               731.0  2.019501e+03  5.003419e-01     2019.00     2019.00     2020.00     2020.00     2020.00
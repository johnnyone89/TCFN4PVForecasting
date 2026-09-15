# Dataset placement and schema

The CSV files currently tracked in this directory are filename placeholders. Replace them locally with the study datasets before running the notebooks, or set `TRACE_DATA_DIR` to another directory containing the same filenames.

## Required filenames

- `Dangjin_Landfill_PV_Dataset.csv`
- `Gwangyang_Port_Site2_PV_Dataset.csv`

## Required columns

```text
Year, Month, Day, Hour,
AverageTemp, LowTemp, HighTemp,
RainFall, SteamPress, DewPoint, Sunshine, Insolation,
Cloudiness, GroundTemp, Temp, Wind, Press, Humi,
Solar_Power
```

The TRACE loader reconstructs an hourly timestamp from `Year`, `Month`, `Day`, and `Hour`, rejects duplicated timestamps, audits missing hours, and checks the complete required schema before feature construction.

## Expected study coverage

| Site | Study window | Expected note |
|---|---|---|
| Dangjin | 2015-01-01 through 2019-08-31 23:00 | Complete hourly series in the recorded experiment |
| Gwangyang | 2015-01-01 through 2019-08-31 23:00 | 24 missing source hours audited in the recorded experiment |

Do not commit private, restricted, or unlicensed data. If the datasets are redistributed publicly, include their authoritative source, license, and checksums here.

# ISM2411 Data Cleaning Copilot Project

This project cleans messy sales data using Python and pandas.

## Project Overview

The script reads a raw CSV sales dataset, cleans the data, and saves a processed version of the file.

The cleaning process includes:
- Standardizing column names
- Removing extra whitespace
- Handling missing values


## Project Structure

```text
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv
├── src/
│   └── data_cleaning.py
├── README.md
└── reflection.md
```

## Requirements

Install pandas before running the script:

```bash
pip install pandas
```

## How to Run

From the project folder, run:

```bash
python src/data_cleaning.py
```

## Output

The cleaned dataset will be saved to:

```text
data/processed/sales_data_clean.csv
```

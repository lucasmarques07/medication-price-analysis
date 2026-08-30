# FarmaGo - Data Analysis with Python

Small Python project created to practice data analysis concepts using Pandas, JSON, SQLite and Matplotlib, based on a fictional pharmacy and medicine comparison system.

The project processes structured medicine and pharmacy data to generate price, inventory and distance analyses, while also producing visualizations from the analyzed data.

## Concepts practiced

- Python functions and modules
- JSON data structures
- Pandas Series and DataFrames
- Boolean filtering
- Grouping and aggregation with Pandas
- JSON normalization with `pd.json_normalize()`
- Data analysis and basic indicators
- SQLite database integration
- Data persistence with `DataFrame.to_sql()`
- Data visualization with Matplotlib
- Basic exception handling
- Separation of responsibilities between modules

## Data flow

The project follows a simple data pipeline:

`JSON → Pandas → DataFrame → Analysis → SQLite / Visualization`

- **JSON** stores the original medicine and pharmacy data
- **Pandas** loads and normalizes the nested data
- **Analysis** processes the data and generates indicators
- **SQLite** stores the resulting DataFrame
- **Matplotlib** generates visual representations of the results

## Implemented features

- Average medicine price
- Average price per medicine
- Medicine with the highest average price
- Medicines below a specified price
- Medicine with the largest inventory
- Medicine with the highest price variation
- Pharmacies with below-average prices and below-average distance
- Export of processed data to SQLite
- Price comparison visualizations
- Price vs. distance visualization

## Architecture overview

The project is divided into modules according to their responsibilities:

- **`data_loader.py`** handles JSON loading and data normalization
- **`analysis.py`** contains the data analysis functions
- **`database.py`** handles SQLite database persistence
- **`visualization.py`** generates charts using Matplotlib
- **`main.py`** orchestrates the execution of the project

## Technologies

- Python
- Pandas
- Matplotlib
- SQLAlchemy
- SQLite
- JSON

## Project structure

```text
FarmaGoEmPython/
├── data/
│   └── farmago.json
├── src/
│   ├── analysis.py
│   ├── data_loader.py
│   ├── database.py
│   ├── main.py
│   └── visualization.py
├── .gitignore
├── README.md
└── requirements.txt
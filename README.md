NYC Taxi ETL Pipeline 🚖

This project demonstrates an ETL (Extract, Transform, Load) pipeline using the "NYC Green Taxi dataset".  
The pipeline extracts data from Parquet files, cleans and transforms it with "Pandas", and loads it into a "PostgreSQL" database.

---

Project Structure

```text
nyc_taxi_etl/
│
├── data/ # Input data (Parquet files)
├── ETL_Task1.ipynb # Jupyter notebook containing ETL steps
├── etl.py # (Optional) Python script version of ETL
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── venv/ # Virtual environment (ignored in git)


---
⚙️ Tools & Technologies

- Python 3.10
- Pandas – data cleaning & transformation
- SQLAlchemy + psycopg2– PostgreSQL connection
- PostgreSQL– target database
- Jupyter Notebook (optional, for data exploration)

---
1. Extract
- Load the NYC Taxi data from Parquet files into a Pandas DataFrame.

2. Transform
Clean data: drop rows with missing values in critical columns.
Convert datetime columns to datetime type.
Create new column: trip_duration_minutes.
Aggregate example: calculate daily trip stats.

3. Load
Connect to PostgreSQL using SQLAlchemy and psycopg2.
Load the cleaned/transformed data into table green_taxi_data.

Setup Instructions/How to run:

1. Clone the Repository
git clone https://github.com/harikabollineni/nyc_taxi_etl.git
cd nyc_taxi_etl

2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Database
Update the connection string in etl.py with your PostgreSQL username, password, and DB name:
engine = create_engine("postgresql+psycopg2://<username>:<password>@localhost:5432/nyc_taxi")

5. Run ETL Script
python etl.py

This will:

Extract NYC Taxi dataset from Parquet
Transform the data (cleaning, schema alignment)
Load into PostgreSQL table green_taxi_data

Future Enhancements

Automate pipeline with Apache Airflow
Add unit tests and data validation checks
Schedule ETL jobs for new data
Build dashboards for visualization

Dataset: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

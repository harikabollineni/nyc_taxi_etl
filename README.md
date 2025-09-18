NYC Taxi ETL Pipeline 🚖

This project demonstrates an ETL (Extract, Transform, Load) pipeline using the "NYC Green Taxi dataset".  
The pipeline extracts data from Parquet files, cleans and transforms it with "Pandas", and loads it into a "PostgreSQL" database.

---

Project Structure

nyc_taxi_etl/
│
├── data/ # Input data (Parquet files)
├── etl.py # Main ETL script
├── requirements.txt # Python dependencies
├── README.md # Documentation
└── venv/ # Virtual environment (ignored in git)


---

## ⚙️ Tools & Technologies

- **Python 3.10**
- **Pandas** – data cleaning & transformation
- **SQLAlchemy + psycopg2** – PostgreSQL connection
- **PostgreSQL** – target database
- **Jupyter Notebook** (optional, for data exploration)

---

Setup Instructions

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


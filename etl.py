# etl.py
import pandas as pd
from sqlalchemy import create_engine

# ----------------------------
# CONFIG
# ----------------------------
PARQUET_FILE = r"C:\nyc_taxi_etl\data\green_tripdata_2024-09.parquet"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "Ammu@0307"  # remember to URL-encode special chars when connecting
POSTGRES_DB = "nyc_taxi"
POSTGRES_HOST = "localhost"
TABLE_NAME = "green_taxi_data"

# ----------------------------
# EXTRACT
# ----------------------------
df = pd.read_parquet(PARQUET_FILE)
print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")

# ----------------------------
# TRANSFORM
# ----------------------------
# Drop rows with missing values in key columns
df = df.dropna(subset=["passenger_count", "trip_distance", "fare_amount", "tip_amount"])

# Convert datetime columns
df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])

# Add trip duration column
df["trip_duration_minutes"] = (
    (df["lpep_dropoff_datetime"] - df["lpep_pickup_datetime"]).dt.total_seconds() / 60
)

print("Transformation complete.")

# ----------------------------
# LOAD
# ----------------------------
# Encode password for special characters
from urllib.parse import quote_plus
password_encoded = quote_plus(POSTGRES_PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{password_encoded}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
)

df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)
print(f"Data loaded into PostgreSQL table '{TABLE_NAME}' successfully!")

"""
Case Study 6
AWS Cloud Automation & Serverless Data Processing

Author: Bojan Djordjevic

Description:
AWS Lambda function that reads multiple CSV files from Amazon S3,
combines the data, calculates artist statistics and uploads the
aggregated results back to Amazon S3.
"""

import boto3
import pandas as pd
import io
import os
from botocore.config import Config


# ----------------------------------------------------------
# AWS Configuration
# ----------------------------------------------------------

BUCKET_NAME = "bojan-music-toplists"
INPUT_PREFIX = "raw/"
OUTPUT_FILE = "final/top_artists_june_2025.csv"

config = Config(
    connect_timeout=5,
    read_timeout=30
)

s3 = boto3.client(
    "s3",
    config=config
)

# ----------------------------------------------------------
# Read all CSV files from S3
# ----------------------------------------------------------

def load_csv_files():

    objects = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=INPUT_PREFIX
    )

    csv_files = [
        obj["Key"]
        for obj in objects.get("Contents", [])
        if obj["Key"].endswith(".csv")
    ]

    all_data = []

    for key in csv_files:

        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=key
        )

        df = pd.read_csv(
            io.BytesIO(response["Body"].read())
        )

        df["source_file"] = key

        all_data.append(df)

    return pd.concat(all_data, ignore_index=True)


# ----------------------------------------------------------
# Data Preparation
# ----------------------------------------------------------

def prepare_data(df):

    df["platform"] = df["source_file"].str.extract(
        r"/(deezer|spotify|itunes)_"
    )[0]

    df["date"] = df["source_file"].str.extract(
        r"_(\d{4}-\d{2}-\d{2})\.csv$"
    )[0]

    return df


# ----------------------------------------------------------
# Aggregation
# ----------------------------------------------------------

def calculate_top_artists(df):

    agg_df = (
        df.groupby("artist")
        .agg(
            num_appearances=("track", "count"),
            num_unique_songs=("track", pd.Series.nunique),
            avg_position=("position", "mean"),
            best_position=("position", "min"),
            platforms=("platform", pd.Series.nunique)
        )
        .reset_index()
    )

    top_artists = agg_df.sort_values(
        by=[
            "num_appearances",
            "platforms",
            "best_position"
        ],
        ascending=[
            False,
            False,
            True
        ]
    ).head(20)

    return top_artists


# ----------------------------------------------------------
# Upload Result
# ----------------------------------------------------------

def upload_result(df):

    output_buffer = io.StringIO()

    df.to_csv(
        output_buffer,
        index=False
    )

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=OUTPUT_FILE,
        Body=output_buffer.getvalue()
    )


# ----------------------------------------------------------
# Lambda Entry Point
# ----------------------------------------------------------

def lambda_handler(event, context):

    try:

        print("Loading CSV files...")

        df = load_csv_files()

        print("Preparing data...")

        df = prepare_data(df)

        print("Calculating statistics...")

        top_artists = calculate_top_artists(df)

        print("Uploading results...")

        upload_result(top_artists)

        return {
            "statusCode": 200,
            "message": "Processing completed successfully."
        }

    except Exception as error:

        print(error)

        return {
            "statusCode": 500,
            "message": str(error)
        }
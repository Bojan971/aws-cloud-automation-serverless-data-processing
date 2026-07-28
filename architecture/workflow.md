# Data Processing Workflow

## Overview

This document describes the complete workflow implemented in this project.

---

## Step 1

CSV files are uploaded into the Amazon S3 bucket.

Location:

raw/

↓

## Step 2

AWS Lambda is triggered manually or automatically.

↓

## Step 3

Lambda retrieves all CSV files stored in the input folder.

↓

## Step 4

The datasets are merged into a single Pandas DataFrame.

↓

## Step 5

Additional metadata is extracted.

Examples:

- Platform
- Date
- Source file

↓

## Step 6

The data is aggregated by artist.

Calculated metrics include:

- Number of appearances
- Number of unique songs
- Average chart position
- Best chart position
- Number of platforms

↓

## Step 7

The Top 20 artists are selected.

↓

## Step 8

The result is exported as a CSV file.

↓

## Step 9

The generated CSV file is uploaded back to Amazon S3.

Location:

final/

↓

## Step 10

CloudWatch stores execution logs.

↓

## Step 11

EventBridge can trigger the workflow automatically according to a predefined schedule.

---

# Workflow Summary

Amazon S3

↓

AWS Lambda

↓

Read CSV Files

↓

Pandas Processing

↓

Aggregation

↓

Generate Report

↓

Upload Result

↓

CloudWatch Logs

↓

EventBridge Scheduler
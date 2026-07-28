# AWS Services Overview

## Overview

This project demonstrates a serverless data processing solution built on Amazon Web Services (AWS). The architecture combines multiple AWS services to automate CSV file processing and generate analytical results without managing servers.

---

# AWS Services Used

## Amazon S3

Amazon S3 is used as the central storage service.

Responsibilities:

- Store raw CSV files
- Store processed output files
- Trigger data processing workflows
- Provide scalable object storage

Example folders:

raw/
final/

---

## AWS Lambda

AWS Lambda executes the Python data processing code.

Responsibilities:

- Read CSV files from Amazon S3
- Merge datasets
- Process data using Pandas
- Generate aggregated statistics
- Save processed results back to Amazon S3

Benefits:

- No server management
- Automatic scaling
- Pay-per-use execution

---

## IAM (Identity and Access Management)

IAM controls permissions between AWS services.

Responsibilities:

- Grant Lambda access to Amazon S3
- Allow writing processed files
- Secure service communication

Typical permissions:

- s3:GetObject
- s3:PutObject
- CloudWatch Logs

---

## Amazon EventBridge

Amazon EventBridge enables scheduled execution.

Responsibilities:

- Run Lambda automatically
- Execute periodic data processing
- Support event-driven automation

---

## Amazon CloudWatch

CloudWatch provides monitoring and logging.

Responsibilities:

- Store Lambda execution logs
- Monitor execution status
- Record runtime errors
- Support troubleshooting

---

# Technologies

- AWS Lambda
- Amazon S3
- IAM
- EventBridge
- CloudWatch
- Python
- Pandas
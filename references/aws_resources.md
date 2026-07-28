# AWS Resources

## Overview

This document lists the primary AWS services used throughout this project.

---

# Amazon S3

Purpose:

Object storage service used for storing raw and processed CSV datasets.

Main Features:

- Highly scalable storage
- Event notifications
- Versioning support
- Secure object management

Documentation:

https://docs.aws.amazon.com/s3/

---

# AWS Lambda

Purpose:

Serverless compute service responsible for processing CSV datasets.

Main Features:

- Event-driven execution
- Automatic scaling
- No infrastructure management
- Pay-per-use pricing

Documentation:

https://docs.aws.amazon.com/lambda/

---

# AWS IAM

Purpose:

Identity and Access Management service used to control permissions.

Main Features:

- User management
- Roles
- Policies
- Secure access control

Documentation:

https://docs.aws.amazon.com/iam/

---

# Amazon EventBridge

Purpose:

Schedules automatic execution of AWS Lambda.

Main Features:

- Scheduled execution
- Event routing
- Automation

Documentation:

https://docs.aws.amazon.com/eventbridge/

---

# Amazon CloudWatch

Purpose:

Monitoring and logging service.

Main Features:

- Lambda logs
- Metrics
- Monitoring
- Alerts

Documentation:

https://docs.aws.amazon.com/cloudwatch/

---

# Python Libraries

The following Python libraries are used:

- boto3
- pandas
- io
- os

---

# Project Repository

This project demonstrates a practical implementation of serverless data processing using AWS cloud services and Python.
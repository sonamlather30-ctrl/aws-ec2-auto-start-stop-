# aws-ec2-auto-start-stop-

🧠 Problem Statement

Organizations often leave EC2 instances running 24/7, leading to unnecessary cloud costs.

🚀 Solution

This project automates:

✅ Starting EC2 instances in the morning
✅ Stopping EC2 instances at night

Using:

Boto3
AWS Lambda
Amazon EventBridge


🏗️ Architecture
EventBridge (Schedule)
        ↓
   AWS Lambda
        ↓
      EC2

      
⚙️ How It Works
Instances are controlled using tags:
AutoStart = True
AutoStop = True
Lambda functions:
lambda_start.py → starts stopped instances
lambda_stop.py → stops running instances







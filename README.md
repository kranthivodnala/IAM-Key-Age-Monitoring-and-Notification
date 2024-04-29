# IAM-Key-Age-Monitoring-and-Notification
Notify IAM keys older than 180 days for all IAM users to Slack using AWS Lambda, Python and Event Bridge

Step 1: Set up an AWS Lambda function using Python.
a) Login to AWS Account
b) Navigate to Lambda Service
c) Click on create function
d) Provide the required details in the fields ex: function name and runtime
e) Click on create function. This will automatically create a IAM role for the lambda function. Pls leverage the same IAM role and provide IAM read or full access policy
Step 2: Configure EventBridge to trigger the Lambda function on a schedule.
    a) Once the lambda function is created. Click on Add Trigger
    b) Select Event bridge Cloudwatch as a Trigger configuration
    c) Provide the required details in the fields like Rule name, Description and Schedule Expression. Pls use https://crontab.guru/ for cron schedule expressions
Step 2: Write Python code in the Lambda function to check for IAM keys older than 180 days and send notifications to Slack.
    a) Upload the python code and replace the values like slack webhook URL, IAM keys cut off date etc.
    b) Deploy the code
    c) Click on Test and provide the dummy test event.
    d) Once you the the 200 response code. Navigate to slack and check for the incoming message.

Outline of Python Code:
    a) In your Lambda function, use the Boto3 library to interact with AWS services.
    b) Check the creation date of each access key and compare it with the current date to determine if it's older than 180 days.
    c) If an access key is older than 180 days, send a notification to Slack.

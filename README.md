# IAM-Key-Age-Monitoring-and-Notification
Notify IAM keys older than 180 days for all IAM users to Slack using AWS Lambda, Python and Event Bridge

Step 1: Set up an AWS Lambda function using Python.<br />
    a) Login to AWS Account<br />
    b) Navigate to Lambda Service<br />
    c) Click on create function<br />
    d) Provide the required details in the fields ex: function name and runtime<br />
    e) Click on create function. This will automatically create a IAM role for the lambda function. Pls leverage the same IAM role and provide IAM read or full access policy<br />

Step 2: Configure EventBridge to trigger the Lambda function on a schedule.<br />
    a) Once the lambda function is created. Click on Add Trigger<br />
    b) Select Event bridge Cloudwatch as a Trigger configuration<br />
    c) Provide the required details in the fields like Rule name, Description and Schedule Expression. Pls use https://crontab.guru/ for cron schedule expressions<br />

Step 3: Write Python code in the Lambda function to check for IAM keys older than 180 days and send notifications to Slack.<br />
    a) Upload the python code and replace the values like slack webhook URL, IAM keys cut off date etc.<br />
    b) Deploy the code<br />
    c) Click on Test and provide the dummy test event.<br />
    d) Once you the the 200 response code. Navigate to slack and check for the incoming message.<br />

Outline of Python Code:<br />
    a) In your Lambda function, use the Boto3 library to interact with AWS services.<br />
    b) Check the creation date of each access key and compare it with the current date to determine if it's older than 180 days.<br />
    c) If an access key is older than 180 days, send a notification to Slack.<br />

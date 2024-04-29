import boto3
import datetime
import os
import requests

def lambda_handler(event, context):
    # Initialize AWS clients
    iam_client = boto3.client('iam')
    
    # Get Slack webhook URL from environment variable
    SLACK_WEBHOOK_URL = "" #Replace your Slack Webhook URL
    slack_webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    
    # Get current date
    current_date = datetime.datetime.now()

    # List IAM users
    users = iam_client.list_users()['Users']

    # Check each user's access keys
    for user in users:
        user_name = user['UserName']
        access_keys = iam_client.list_access_keys(UserName=user_name)['AccessKeyMetadata']
        
        for key in access_keys:
            key_id = key['AccessKeyId']
            creation_date = key['CreateDate'].replace(tzinfo=None)
            age = (current_date - creation_date).days
            
            if age > 0: #Mention the cut off days for IAM keys. Best practice is to mointor the keys older than 90 days
                message = f"{user_name} IAM access key for user is older than 0 days. Please rotate the keys and delete the old keys"
                send_slack_notification(slack_webhook_url, message)
            # return a response
    return {
        'statusCode': 200,
        'body': 'Slack notification sent successfully'
    }

def send_slack_notification(slack_webhook_url, message):
    payload = {
        "text": message
    }
    try:
        response = requests.post(slack_webhook_url, json=payload)
        response.raise_for_status()
        print("Slack notification sent successfully")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"Error sending Slack notification: {e}")
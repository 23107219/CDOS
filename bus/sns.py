import logging
import boto3
from botocore.exceptions import ClientError

#Class to create and delete a topic
REGION_NAME='us-east-1'

def create_topic(topic_name):
        
        try:
            sns_client = boto3.client('sns',region_name=REGION_NAME)
            print('\ncreating the topic {}...'.format(topic_name))
            response = sns_client.create_topic(Name=topic_name)
            return response['TopicArn']
        
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
def subscribe_to_topic(topic_name):
        try:
            sns_client = boto3.client('sns',region_name=REGION_NAME)
            # the create_topic() method returns that topic's ARN
            response = sns_client.create_topic(Name=topic_name)
            topic_arn = response['TopicArn']
            print('Subscriber is subscribing to topic {}...'.format(topic_name))
            sns_client.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint='x23107219@student.ncirl.ie')
           
        except ClientError as e:
            logging.error(e)
            return False
        return True

def delete_topic(topic_name):
        
        try:
            sns_client = boto3.client('sns',region_name=REGION_NAME)
            # if the topic already exists, the create_topic() method returns that topic's ARN
            response = sns_client.create_topic(Name=topic_name)
            topic_arn = response['TopicArn']
            print('\ndeleting the topic {}...'.format(topic_name))
            sns_client.delete_topic(TopicArn=topic_arn)
           
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
def sns_email(topic_response,a_subscriber,topic_arn,region):
        try:
            # Create an AWS SNS client
            sns = boto3.client('sns', region_name=region)
            
            # The email-like message t to send
            email_message = "Hello,\n\n Your expense report has been generated.Please login to view the report"
            
            # The subject of the email
            email_subject = "Personal Expense Report Generated"
            
            # The email address to send the message
            email_address = 'x23107219@student.ncirl.ie'  # Recipient's email address
            # Send the email-like message
            response = sns.publish(
                TopicArn=topic_arn,  #SNS topic ARN
                Subject=email_subject,
                Message=email_message,
                MessageStructure='string',
                MessageAttributes={
                    'email': {
                        'DataType': 'String',
                        'StringValue': email_address,
                    },
                }
            )
            return response
        except ClientError as e:
            logging.error(e)
            return False
        return True


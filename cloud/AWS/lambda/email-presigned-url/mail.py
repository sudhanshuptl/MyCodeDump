import boto3
import logging
from botocore.exceptions import ClientError

SENDER = "Sudhanshu Patel <sudhanshu@sender.com>"

RECIPIENT = ["sudhanshuptl13@gmail.com",
             "query.b2cs@gmail.com"]

# SES Region
AWS_REGION = "ap-south-1"

# The character encoding for the email.
CHARSET = "UTF-8"


def send_mail(signed_url: str):
    '''
    :param signed_url: signed url
    :return:
    '''
    subject = "Dummy Subject"

    # The email body for recipients with non-HTML email clients.
    body_text = ("Amazon SES Test (Python)\r\n"
                 "This is yesterdays report link."
                 )

    # The HTML body of the email.
    body_html = f"""<html>
    <head></head>
    <body>
      <h1>Amazon SES Test (SDK for Python)</h1>
      <p>This is yesterdays report
        <a href='{signed_url}'> link </a>
       .</p>
    </body>
    </html>
    """

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': RECIPIENT,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        logging.error(e.response['Error']['Message'])
        raise e
    else:
        logging.info(f"Email sent! Message ID: {response['MessageId']}")

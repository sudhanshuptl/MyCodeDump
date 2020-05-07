import json
import boto3
import logging
from botocore.exceptions import ClientError
from mail import send_mail

SIGNED_URL_EXPIRATION_TIME_SEC = 100
S3_CREATE_EVENT = 'ObjectCreated:Put'


def lambda_handler(event, context):
    '''
     trigger -> s3 object of type .zip creation event
     Generate pre-signed url and send mail to recipients
    :param event: s3 object create event
    :param context: context
    :return: status
    '''

    logging.info(f"Event : {event}")

    try:
        # fetch bucket & object key
        if event and event['Records']:
            event_name = event['Records'][0]['eventName']
            
            if event_name == S3_CREATE_EVENT:
                bucket = event['Records'][0]['s3']['bucket']['name']
                object_key = event['Records'][0]['s3']['object']['key']
            else:
                raise EnvironmentError('Invalid Event')
        else:
            logging.error(f"Event has missing data")
            raise EnvironmentError('Invalid event or missing data')
        
        object_path = f's3://{bucket}/{object_key}'
        logging.info(f'object_path : {object_path}')

        # Generating pre-signed url
        pre_signed_url = generate_pre_signed_url(bucket_name=bucket, key=object_key)

        # Sending Mail
        send_mail(pre_signed_url)

    except Exception as e:
        logging.critical(str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'status': 'failed', 'error': str(e)})
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'ok'})
        }


def generate_pre_signed_url(bucket_name, key):
    '''
    :param bucket_name: bucket name
    :param key: object key
    :return: pre_signed url
    '''
    s3_client = boto3.client('s3')

    try:
        pre_signed_url = s3_client.generate_presigned_url('get_object',
                                                          Params={'Bucket': bucket_name,
                                                                  'Key': key},
                                                          ExpiresIn=SIGNED_URL_EXPIRATION_TIME_SEC)
    except ClientError as e:
        logging.error(f'Error while generating pre-signed url : {e}')
        raise e
    else:
        return pre_signed_url

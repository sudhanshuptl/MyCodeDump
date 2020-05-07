# Introduction
This lambda function `lambda_function.lambda_handler` will create a pre-signed url
and send to the given recipients.

# Working
1. Trigger an event to evoke our lambda function when a file with given extension (`.csv`) is created at given path in `aws s3`.
2. Capture the `bucket` and `object key` information.
3. Generate pre-signed url.
4. Mail url to given recipients using amazon `SES`


# Configuration
* `lambda_function.SIGNED_URL_EXPIRATION_TIME_SEC` : Link expiration time in second
* `mail.SENDER` : Senders email, (need to verify with ses)
* `mail.RECIPIENT` : Recipients email addresses
* `mail.AWS_REGION` : SES region.

# Access
* lambda function need `s3 read only & ses:sendMail` access 

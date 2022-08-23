#List AWS IAM users

import boto3

client = boto3.client('iam',
	aws_access_key_id = "AKIAZWYPHV5U5GVI5SHR", 
	aws_secret_access_key = "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")

myuser = client.list_users()

for output in myuser['Users']:
	print(output['UserName'],
	output['UserId'],
	output['CreateDate'])

#{'Users': [{'Path': '/', 'UserName': 'karthick', 'UserId': 'AIDAZWYPHV5UZMBYU4ZUC', 'Arn': 'arn:aws:iam::667362504553:user/karthick', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 0, 14, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 23, 10, 8, 51, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'User1', 'UserId': 'AIDAZWYPHV5U4JNHTKSOQ', 'Arn': 'arn:aws:iam::667362504553:user/User1', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 50, 25, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'User2', 'UserId': 'AIDAZWYPHV5U7UZ2A23CI', 'Arn': 'arn:aws:iam::667362504553:user/User2', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 50, 25, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'Venkat', 'UserId': 'AIDAZWYPHV5UWICFRMELX', 'Arn': 'arn:aws:iam::667362504553:user/Venkat', 'CreateDate': datetime.datetime(2022, 5, 23, 11, 23, 28, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 23, 12, 46, 6, tzinfo=tzutc())}], 'IsTruncated': False, 'ResponseMetadata': {'RequestId': '8d86c299-cf43-4bba-80bf-3e593074721f', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '8d86c299-cf43-4bba-80bf-3e593074721f', 'content-type': 'text/xml', 'content-length': '1425', 'date': 'Mon, 23 May 2022 13:24:32 GMT'}, 'RetryAttempts': 0}}

#[{'Path': '/', 'UserName': 'karthick', 'UserId': 'AIDAZWYPHV5UZMBYU4ZUC', 'Arn': 'arn:aws:iam::667362504553:user/karthick', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 0, 14, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 23, 10, 8, 51, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'User1', 'UserId': 'AIDAZWYPHV5U4JNHTKSOQ', 'Arn': 'arn:aws:iam::667362504553:user/User1', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 50, 25, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'User2', 'UserId': 'AIDAZWYPHV5U7UZ2A23CI', 'Arn': 'arn:aws:iam::667362504553:user/User2', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 50, 25, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'Venkat', 'UserId': 'AIDAZWYPHV5UWICFRMELX', 'Arn': 'arn:aws:iam::667362504553:user/Venkat', 'CreateDate': datetime.datetime(2022, 5, 23, 11, 23, 28, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 23, 12, 46, 6, tzinfo=tzutc())}]

#{'Path': '/', 'UserName': 'karthick', 'UserId': 'AIDAZWYPHV5UZMBYU4ZUC', 'Arn': 'arn:aws:iam::667362504553:user/karthick', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 0, 14, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 23, 10, 8, 51, tzinfo=tzutc())}
#{'Path': '/', 'UserName': 'User1', 'UserId': 'AIDAZWYPHV5U4JNHTKSOQ', 'Arn': 'arn:aws:iam::667362504553:user/User1', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 50, 25, tzinfo=tzutc())}
#{'Path': '/', 'UserName': 'User2', 'UserId': 'AIDAZWYPHV5U7UZ2A23CI', 'Arn': 'arn:aws:iam::667362504553:user/User2', 'CreateDate': datetime.datetime(2022, 5, 23, 10, 50, 25, tzinfo=tzutc())}
#{'Path': '/', 'UserName': 'Venkat', 'UserId': 'AIDAZWYPHV5UWICFRMELX', 'Arn': 'arn:aws:iam::667362504553:user/Venkat', 'CreateDate': datetime.datetime(2022, 5, 23, 11, 23, 28, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 23, 12, 46, 6, tzinfo=tzutc())}


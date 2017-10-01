import boto3 import zipfile import StringIO import mimetypes def 
lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = 
sns.Topic('arn:aws:sns:us-east-1:686781582320:deployGarrisonTopic')
    try:
        s3 = boto3.resource('s3')
    
        garrison_bucket = s3.Bucket('garrison.cloud')
        
        build_bucket = s3.Bucket('garrisonbuild.garrisoncloud')
        
        garrison_zip = StringIO.StringIO()
        
        build_bucket.download_fileobj('garrisonbuild.zip', garrison_zip)
    
        with zipfile.ZipFile(garrison_zip) as myzip:
            for nm in myzip.namelist():
               obj = myzip.open(nm)
               garrison_bucket.upload_fileobj(obj, nm,
                 ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
               garrison_bucket.Object(nm).Acl().put(ACL='public-read')
               
        print "Garrison Deployed!"
        topic.publish(Subject = "Garrison Deployed", Message="Garrison 
deployed successfully")
    except:
        topic.publish(Subject="Garrison Deploy Failed", Message="The 
Garrison was not deployed successfully")
        raise
    return 'Hello from Lambda'
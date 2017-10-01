import boto3 import zipfile import StringIO import mimetypes def 
lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = 
sns.Topic('arn:aws:sns:us-east-1:686781582320:deployGarrisonTopic')
    
    location = {
        "bucketName": 'garrisonbuild.garrisoncloud',
        "objectKey": 'garrisonbuild.zip'
    }
    try:
        job = event.get("CodePipeline.job")
        
        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]
        
        print "Building garrison from " + str(location)
        s3 = boto3.resource('s3')
    
        garrison_bucket = s3.Bucket('garrison.cloud')
        
        build_bucket = s3.Bucket(location["bucketName"])
        
        garrison_zip = StringIO.StringIO()
        
        build_bucket.download_fileobj(location["objectKey"], 
garrison_zip)
    
        with zipfile.ZipFile(garrison_zip) as myzip:
            for nm in myzip.namelist():
               obj = myzip.open(nm)
               garrison_bucket.upload_fileobj(obj, nm,
                 ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
               garrison_bucket.Object(nm).Acl().put(ACL='public-read')
               
        print "Garrison Deployed!"
        topic.publish(Subject = "Garrison Deployed", Message="Garrison 
deployed successfully")
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
    except:
        topic.publish(Subject="Garrison Deploy Failed", Message="The 
Garrison was not deployed successfully")
        raise
    return 'Hello from Lambda'

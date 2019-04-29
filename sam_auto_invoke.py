import sys
from ruamel.yaml import YAML
import subprocess
from pathlib import Path


def s3invoke(function, path):
    subprocess.run("sam local generate-event s3 put|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event s3 delete|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def dbinvoke(function, path):
    subprocess.run("sam local generate-event dynamodb update|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def apiinvoke(function, path):
    subprocess.run("sam local generate-event apigateway authorizer|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event apigateway aws-proxy|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def cfninvoke(function, path):
    subprocess.run("sam local generate-event cloudformation create-request|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def cfinvoke(function, path):
    subprocess.run("sam local generate-event cloudfront ab-test|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront access-request-in-response|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront http-redirect|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront modify-querystring|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront modify-response-header|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront multiple-remote-calls-aggregate-response|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront normalize-querystring-to-improve-cache-hit|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront redirect-on-viewer-country|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront redirect-unauthenticated-users|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront response-generation|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront serve-object-on-viewer-device|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudfront simple-remote-call|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def cwinvoke(function, path):
    subprocess.run("sam local generate-event cloudwatch logs|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event cloudwatch scheduled-event|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def cognitoinvoke(function, path):
    subprocess.run("sam local generate-event cognito sync-trigger|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def rekinvoke(function, path):
    subprocess.run("sam local generate-event rekognition s3-request|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def lexinvoke(function, path):
    subprocess.run("sam local generate-event lex book-car|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event lex book-hotel|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event lex make-appointment|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event lex order-flowers|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def kinesisinvoke(function, path):
    subprocess.run("sam local generate-event kinesis analytics|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis analytics-compressed|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis analytics-dynamodb|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis analytics-kpl|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis apachelog|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis cloudwatch-logs-processor|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis get-records|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis kinesis-firehose|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis streams-as-source|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event kinesis syslog|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)



def configinvoke(function, path):
    subprocess.run("sam local generate-event config item-change-notification|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event config oversized-item-change-notification|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local generate-event config periodic-rule|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def sesinvoke(function, path):
    subprocess.run("sam local generate-event ses email-receiving|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def snsinvoke(function, path):
    subprocess.run("sam local generate-event sns notification|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def sqsinvoke(function, path):
    subprocess.run("sam local generate-event sqs receive-message|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def stepinvoke(function, path):
    subprocess.run("sam local generate-event stepfunctions error|sam local invoke {} -t {} >>logs.txt 2>&1".format(function, path), shell=True)


def noneinvoke(function, path):
    subprocess.run("sam local invoke {} -t {} --no-event >>logs.txt 2>&1".format(function, path), shell=True)
    subprocess.run("sam local invoke {} -t {} --no-event >>logs.txt 2>&1".format(function, path), shell=True)


def parse(file):
    output={}
    yaml = YAML()
    yaml.preserve_quotes = True
    with open(file, 'r') as stream:
        data = yaml.load(stream)
    for resource in data['Resources']:
        if data['Resources'][resource]['Type'] == 'AWS::Serverless::Function':
            #print(resource)
            if 'Description' in data:
                with open('logs.txt','a') as f:
                    f.write(data['Description'] + '\n')
                if 'rekognition' in data['Description']:
                    output.update({resource:'rekognition'})
                elif 'Events' in data['Resources'][resource]['Properties']:
                    for event in data['Resources'][resource]['Properties']['Events']:
                        output.update({resource:data['Resources'][resource]['Properties']['Events'][event]['Type']})
                elif 'API' in data['Description']:
                    output.update({resource:'Api'})
                elif 'CloudFormation' in data['Description']:
                    output.update({resource:'CloudFormation'})
                elif 'CloudWatch' in data['Description']:
                    output.update({resource:'CloudWatch'})
                elif 'Cognito' in data['Description']:
                    output.update({resource:'Cognito'})
                elif 'Config' in data['Description']:
                    output.update({resource:'Config'})
                elif 'CloudFront' in data['Description']:
                    output.update({resource:'CloudFront'})
                elif 'Kinesis' in data['Description']:
                    output.update({resource:'Kinesis'})
                elif 'Lex' in data['Description']:
                    output.update({resource:'Lex'})
                elif 'SES' in data['Description']:
                    output.update({resource:'SES'})
                elif 'SQS' in data['Description']:
                    output.update({resource:'SQS'})
                elif 'Step Functions' in data['Description']:
                    output.update({resource:'step'})
                else:
                    output.update({resource:'None'})
    with open('testdata.yaml', 'w') as outfile:
        yaml.dump(output, outfile)


def autorun(repo):
    if Path(repo + "/template.yaml").exists():
        try:
            parse(repo + '/template.yaml')
        except:
            with open('logs.txt','a') as f:
                f.write('Bad template' + '\n')
            return
        path = repo + '/template.yaml'
    elif Path(repo + "/template.yml").exists():
        try:
            parse(repo + '/template.yml')
        except:
            with open('logs.txt','a') as f:
                f.write('Bad template' + '\n')
            return
        path = repo + '/template.yml'
    else:
        with open('logs.txt','a') as f:
            f.write('No template' + '\n')
        return
        return
    yaml = YAML()
    yaml.preserve_quotes = True
    with open('testdata.yaml', 'r') as stream:
        data = yaml.load(stream)
    for function in data:
        if data[function] == 'S3':
            s3invoke(function, path)
        elif data[function] == 'DynamoDB':
            dbinvoke(function, path)
        elif data[function] == 'Api':
            apiinvoke(function, path)
        elif data[function] == 'CloudFormation':
            cfninvoke(function, path)
        elif data[function] == 'CloudFront':
            cfinvoke(function, path)
        elif data[function] == 'Kinesis':
            kinesisinvoke(function, path)
        elif data[function] == 'CloudWatch':
            cwinvoke(function, path)
        elif data[function] == 'Cognito':
            cognitoinvoke(function, path)
        elif data[function] == 'Config':
            configinvoke(function, path)
        elif data[function] == 'rekognition':
            rekinvoke(function, path)
        elif data[function] == 'Lex':
            lexinvoke(function, path)
        elif data[function] == 'SES':
            sesinvoke(function, path)
        elif data[function] == 'SNS':
            snsinvoke(function, path)
        elif data[function] == 'SQS':
            sqsinvoke(function, path)
        elif data[function] == 'step':
            stepinvoke(function, path)
        elif data[function] == 'None':
            noneinvoke(function, path)

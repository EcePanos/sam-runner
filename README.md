# sam-runner
A research-focused tool for automatically testing AWS SAM applications en masse.

## Pre-requisites
- python3 and pip
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- `pip install -r requirements.txt`

## Features
- This test attempts to automate the process of running hundreds of tests in the `sam local` environment, automatically choosing the correct triggers by examining the application template.
- At this stage the tool just dumps the application's `stderr` to a log file. Better formatting of the output will be implemented later.

## Usage
You can use the `run_all(diff_file)` function in `sar_mass_test` to test multiple AWS SAM applications. The input file should be in `.csv` format and conform to the format produced by a data dump from the AWS Serverless Application Repository. For compatibility's sake, this just means the 7th cell of each row should be the Github link to the source.  
## Limitations
- Only Applications with a public Github repository can be tested
- There needs to be a `template.yaml` or `template.yml` file in the root directory of the Github repo, as such the tool cannot test a Github repo that consists of a collection of applications (yet!)
- The tool uses the `sam local` environment to test the applications, so all limitations that apply to that also apply to this tool.
- The tool determines the type of event to use as a trigger by examining the template for event properties and metadata descriptions. Applications that require more complex setup or depend on backend resources will most likely fail to run.
- Though the tools tries to clean up after itself, some trash files are created that have to be deleted manually after each run.

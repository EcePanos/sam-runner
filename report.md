### 1st run (no recursion):  
- *Execution time: 32 minutes*
- 439 sar entries (Obtained using aws-sar-analysis)  
- 352 repositories cloned (Rest had no valid github links)  
- 108 functions invoked (Rest had no template file in root directory, common in repos consisting of a collection of applications instead of just one, possibly fixable, or non-parseable template)  
- 5 completed successfully
- 54 failed because the code was zipped this is supported by AWS but not SAM local
- 10 failed due to missing backend components
- 39 failed due to bad event structure
- 229 had no template in root folder
- 1 had bad template (duplicate keys)
- 14 failed to invoke with no output

### 2nd run (recursive search for template file):
- *Execution time: 50 minutes*
- 447 applications
- 514 function invocations
- 115 succeeded 22.37%
- 96 failed because the code was zipped
- 65 failed due to missing backend
- 4 had no template
- 3 had bad template

### Possible brute force Execution
- Ignore event-selecting logic and execute each application with all available Events
- Possibly higher success rate
- Potentially 15 times longer execution time (45 events per function instead of 3 on average with selection logic)
- Possibly add filter to avoid the AWS sample applications? (They amount to about 35% of the repository)

### 1st run:  
- *Execution time: 32 minutes*
- **439 sar entries** (Obtained using aws-sar-analysis)  
- **352 repositories cloned** (Rest had no valid github links)  
- **108 functions invoked** (Rest had no template file in root directory, common in repos consisting of a collection of applications instead of just one, possibly fixable, or non-parseable template)  
- **5 completed successfully**
- **54 failed because the code was zipped** this is supported by AWS but not SAM local
- **10 failed due to missing backend components**
- **39 failed due to bad event structure**
- **229 had no template in root folder**
- **1 had bad template** (duplicate keys)
- **14 failed to invoke with no output**

### 2nd run (terminated before completion)
- Cloned and invoked all applications with valid template
- Up until termination approx 25% success rate
- Estimated execution time ~2 hours
- May include duplicates in case some applications are listed more than once in the data dump

### Possible brute force Execution
- Ignore event-selecting logic and execute each application with all available Events
- Possibly higher success rate
- Potentially 15 times longer execution time (45 events per function instead of 3 on average with selection logic)

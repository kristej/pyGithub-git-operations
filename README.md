# A python library/script to automate cloning a repository. 
1. It will download/clone the public Github repository locally. 
2. It will remove the files LICENCE.txt and README.md and all the git history(and branches) 
3. It will create a new Github repository initialized with the input github repository

## You can run GitClone.py or install GitClone.exe and run via cmd using the arguments
* optional arguments:  
-h, --help     show this help message and exit
* required argument:  
-u USERNAME    Username  
-p PASSWORD    Password  
-i INPUTURL    Input repository(public) url like https://github.com/username/repository  
-o OUTPUTNAME  Output repository name

## Setup
### Instructions to run GitClone.py on cmd 
#### For argument help
```
C:\path\to\script> python GitClone.py --help
```
#### Sample parameters
```
C:\path\to\script>python GitClone.py -u somename -p somepassword -i https://github.com/username/repository -o newreponame
```
### Instructions to run GitClone.exe as an executable
Install GitClone.exe and run cmd in the same directory.
#### For argument help
```
C:\path\to\exe> .\GitClone.exe --help
```
#### Sample parameters
```
C:\path\to\script>.\GitClone.exe -u somename -p somepassword -i https://github.com/username/repository -o newreponame
```

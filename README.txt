A python library/script to atomate cloning a repository and 
1. It will download/clone the public Github repository locally. 
2. It will remove the files LICENCE.txt and README.md and all the git history(and branches) 
3. It will create a new Github repository initialized with the input github repository

optional arguments:
  -h, --help     show this help message and exit
required argument:
  -u USERNAME    Username
  -p PASSWORD    Password
  -i INPUTURL    Input repository(public) url like
                 https://github.com/username/repository
  -o OUTPUTNAME  Output repository name
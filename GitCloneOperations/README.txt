Input
The input to the code will be
1. Link to a public github repository (Any repository which has a LICENCE.txt and
README.md file will be sufficient for this assignment).
2. Github credentials (username/password) to authenticate the user
3. New Github repository name

Process
The code will do the following in order:
1. The library will download/clone the public Github repository locally.
2. The library will remove the files LICENCE.txt and README.md from the repository
and all the git history (and branches)
3. Use the Github API to create a new Github repository initialized with the input github
repository content that you downloaded locally. The new repository will be named
using name supplied.
import git,os,tempfile,fnmatch,argparse,sys,shutil,stat,github
from github import Github
from subprocess import call


def RepoDuplicate(username,password,input_repo_url,output_repo_name):

    tempdir,path,flag = clone_repo(input_repo_url)

    if flag == 1:
        #error in cloning
        shutil.rmtree(tempdir,ignore_errors=True)
        sys.exit(1)

    flag = delete_files(path)
    if flag == 1:
        #error deleting readme and license files
        sys.exit(1)
    
    print("Removing branches and all history....")
    flag = delete_git_file(path)
    if flag == 1:
        print("Error deleting history and branches.")
        sys.exit(1)
    elif flag == 0:
        print("Done")

    flag = git_operations(username,password,output_repo_name,path)
    if flag == 1:
        print("Reverting changes")
        delete_git_file(path)
        shutil.rmtree(tempdir,ignore_errors=True)
        print("Done")
        return 1
    elif flag == 0:
        print("Deleting local clone...")
        delete_git_file(path)
        shutil.rmtree(tempdir,ignore_errors=True)
        print("Done")
        return 0


def clone_repo(input_repo_url):

    try:
        tempdir = tempfile.mkdtemp(prefix="",suffix="")
        predictable_filename = 'clonedfile'
        saved_umask = os.umask(0o077)
        path = os.path.join(tempdir,predictable_filename)

        #Splitting the input url.
        url_user = input_repo_url.split('/')[3]
        url_repo = input_repo_url.split('/')[4]

        print("Begining tasks...")

        #Cloning a public repository to a temporary local directory
        print("Cloning the repository at "+path)

        #Check if repository is public else stop execution

        repo = git.Repo.clone_from(f'https://github.com/{url_user}/{url_repo}.git',path, branch="master",depth=1)
        print("Done")
        return tempdir,path,0

    except git.exc.GitError as err:
        #If there's an error cloning the repository
        print(f'ERROR! : https://github.com/{url_user}/{url_repo}.git maybe not a public repository,\n check url format [-h].')
        print(err)
        return tempdir,path,1


def delete_files(path):

    pattern1="LICENSE*"
    pattern2="README*"

    #Removing README and LICENSE files from the cloned repository
    print("Deleting README and LICENSE files....")
    try:
        for roots,dirs,files in os.walk(os.path.join(path,'')):
            for file in fnmatch.filter(files,pattern1):
                    os.remove(os.path.join(roots,file))
            for file in fnmatch.filter(files,pattern2):
                    os.remove(os.path.join(roots,file))
    except Exception as err:
        print("Error in deleting file:"+os.path.join(roots,file))
        print(err)
        return 1


    print("Done")
    return 0

def git_operations(username,password,output_repo_name,path):

	#Fetching the github user account and creating a github empty repository
    try:
        g = Github(username,password)
        user = g.get_user()
        repo1 = user.create_repo(output_repo_name)

        #creating target url to push cloned local repo using username and output_repo_name
        target_url = f'https://github.com/{username}/{output_repo_name}.git'
        print("Pushing the cloned repository to: "+target_url)

        #initialize the repo after deleting .git directory
        new_repo = git.Repo.init(path)
        new_repo.git.add(A=True)
        new_repo.create_remote("new",url=target_url)
        new_repo.git.commit(m='initial commit')
        new_repo.git.push('new','master')

    except github.GithubException as err:
        print(err)
        return 1
    except Exception as err:
        #delete repository if pushing fails
        repo1.delete()
        print(err)
        return 1

    print("Git operations done.")    
    return 0


def delete_git_file(path):

    

    def on_rm_error(func, dir, exc_info):
        os.chmod(dir, stat.S_IWRITE)
        os.unlink(dir)
    
    try:
        for i in os.listdir(path):
            if i.endswith('git'):
                tmp = os.path.join(path, i)
                # We want to unhide the .git folder before unlinking it.
                while True:
                    call(['attrib', '-H', tmp])
                    break
                shutil.rmtree(tmp, onerror=on_rm_error)
    except Exception as err:
        print(err)
        return 1

    return 0


def main():
    parser=argparse.ArgumentParser(description=" A python library/script to atomate cloning a repository and 1. It will download/clone the public Github repository locally. 2. It will remove the files LICENCE.txt and README.md and all the git history(and branches) 3. It will create a new Github repository initialized with the input github repository")
    parser.add_argument("-u",help="Username" ,dest="username", type=str, required=True)
    parser.add_argument("-p",help="Password" ,dest="password", type=str, required=True)
    parser.add_argument("-i",help="Input repository(public) url like https://github.com/username/repository " ,dest="inputurl", type=str, required=True)
    parser.add_argument("-o",help="Output repository name" ,dest="outputname", type=str, required=True)
    args=parser.parse_args()

    username = args.username
    password = args.password
    input_repo_url = args.inputurl
    output_repo_name = args.outputname

    flag = RepoDuplicate(username,password,input_repo_url,output_repo_name)

if __name__=="__main__":
    main()






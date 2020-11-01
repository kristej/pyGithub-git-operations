import unittest
import CloneGitRepo


#The username and passwords have been changed after testing

class TestRepo(unittest.TestCase):

    def test_RepoDuplicate(self):
        username = 'insert_USername'
        password = 'insert_password'
        input_repo_url = f"https://github.com/kristej/Uniform-Database-Management"
        output_repo_name = "wholesome"
        
        print("Dont authorize access when asked to login")
        flag  = CloneGitRepo.RepoDuplicate(username,password,input_repo_url,output_repo_name)
        self.assertEqual(flag,1)
        
        print("Authorize access/Login")
        flag  = CloneGitRepo.RepoDuplicate(username,password,input_repo_url,output_repo_name)
        self.assertEqual(flag,0)

    def test_clone_repo(self):
        url = f"https://github.com/kristej/Uniform-Database-Management"
        url1 = f"https://github.com/kristej/Uniform-Database-Mam"
        temp,path,flag = CloneGitRepo.clone_repo(url)
        self.assertIsNotNone(temp)
        self.assertIsNotNone(path)
        self.assertEqual(flag,0)

        temp,path,flag = CloneGitRepo.clone_repo(url1)
        self.assertIsNotNone(temp)
        self.assertIsNotNone(path)
        self.assertEqual(flag,1)

    def test_delete_files(self):
        path = r"testfiles"
        path1 = r"testfiles1"
        self.assertEqual(CloneGitRepo.delete_files(path),0)
        self.assertEqual(CloneGitRepo.delete_files(path1),1)

    def test_git_operations(self):
        #initialize a test repo in current directory

        #correct parameters
        username = 'insert_USername'
        password = 'insert_password'
        output_repo_name = "testrepo"
        path = r"testrepo"
        
        #wrong parameters
        username1 = 'insert_USername'
        password1 = 'insert_password'
        output_repo_name1 = "testrepo.git"
        path1 = r"testrepo"
	#For right credentials
        flag = CloneGitRepo.git_operations(username,password,output_repo_name,path)
        self.assertEqual(flag,0)
	#For bad credentials
        flag = CloneGitRepo.git_operations(username1,password1,output_repo_name1,path1)
        self.assertEqual(flag,1)

    def test_delete_git_file(self):
        path = r"testrepo"

        flag = CloneGitRepo.delete_git_file(path)
        self.assertEqual(flag,0)


if __name__ == '__main__':
	unittest.main()

import os
from github import Github
from github import Auth

#
# To test use # export REPO_KEY=??
#

def main():
    github_key = os.environ["REPO_KEY"]

    auth = Auth.Token(github_key)
    
    #g = Github(auth=auth)

    g = Github(base_url="https://github.com/1Bira/", auth=auth)
    g.get_user().login

    

if __name__ == "__main__":
    main()

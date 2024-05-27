import os
from github import Github
from github import Auth

#
# To test use # export REPO_KEY=??
#

def main():
    github_key = os.environ["REPO_KEY"]

    auth = Auth.Token(github_key)
    
    g = Github(auth=auth)

    #g = Github(base_url="https://github.com/1Bira/", auth=auth)
    repo = g.get_repo("1Bira/gitops-repo-poc-v1")
    repo.get_branch(branch="main")
    all_files = []
    contents = repo.get_contents("")

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))
    for file in allfiles:
        print(file)


    

if __name__ == "__main__":
    main()

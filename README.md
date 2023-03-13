

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### install pymongo
```
pip install pymongo
```
```
pip install pymongo[srv]
```

# To download your dataset

```
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```

This is changes made in neuro lab


Git commands

If you are starting a project and you want to use git in your project
```
git init
```
Note: This is going to initalize git in your source code.


OR

You can clone exiting github repo
```
git clone <github_url>
```
Note: Clone/ Downlaod github  repo in your system


Add your changes made in file to git stagging are
```
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to staging are


Create commits
```
git commit -m "message"
```

```
git push origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name 

To push your changes forcefully.
```
git push origin main -f
```


To pull  changes from github repo
```
git pull origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name

### Create .env file for urls
```
MONGO_DB_URL = "mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority"
```

## github - connect to your repository
```
git init    # initialise git to your project
git remote add origin <githublink>
cd .git/
cd logs/
ls
cat HEAD/
cd remotes/
ls
cd origin
ls
cat main
cd.. # back to main dir
```
## git push command
```
git add .              # add for all files to staging area
git add <file_name>    # add a specific file 
git status             # To check the staging files 
git commit -m "comment about your commit"
git push origin main   # push files to origin main
git push origin main -f  #  push files forcefully to origin main 

```
### check which repository connected 
```
git remote -ve
git remote remote origin
git log    # history of commits
```

```
### Deployment details 
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=ap-south-1
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME=sensor-fault
BUCKET_NAME=sensor-air-pressure
MONGO_DB_URL=
```

## EC2 commands 
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

```
docker images - check docker images 
docker ps - CHeck docker containers 
```

```
# Authentication


√ Connected to GitHub

# Runner Registration

Enter the name of the runner group to add this runner to: [press Enter for Default] 

Enter the name of runner: [press Enter for ip-172-31-13-4] self-hosted

This runner will have the following labels: 'self-hosted', 'Linux', 'X64' 
Enter any additional labels (ex. label-1,label-2): [press Enter to skip]     

√ Runner successfully added
√ Runner connection is good

# Runner settings

Enter name of work folder: [press Enter for _work] 

√ Settings Saved.
```
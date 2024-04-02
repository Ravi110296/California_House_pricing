# California_House_pricing
Predicting the House prices in California estate

## Softwares and tools requirement
1. [Github_Account](https://github.com)
2. [VS_Studio_Code](https://code.visualstudio.com/)
3. [Heroku_Account](https://heroku.com)
4. [Git_CLI](https://git-scm.com)

## Creating a vitual environment

command to create the vrtual environment

```
python -m venv environment name
```

command to activate the vrtual environment

```
venv\scripts\activate
```

command to install the requirements in the virtual environment

```
pip install -r requirement.txt
```
***Note: requirement.txt is nor originally created with the package, you have to create a txt file in directory with all the required libraries name***

## Pushing files on Github

to push files on github you first need to run the following codes

```
git config --global user.name "your_username"
```

```
git config --global user.email "your_emailid" 
```

these codes are to set the username and email id on git CLI to link it with github

after that use the code

**Adding files to git CLI for commiting**

```
git add .
```
to list all the files that will be pushed to github

***Note: You also can use the below code to add files one by one***
```
git add filename
```

we can use

```
git status
```
to check the status of the commit files

**Commiting files on github**

to commit files use the code below

```
git commit -m "commit reason"
```
git commit will create a snapshot as to what changes will happen in the files

**Pushing files on github**
After doing the commit commands we have upload the files locally and are now ready to push them on github
for that we need the command

```
git push <remote><branch>
```
here remote is the location where the commited files are present loacally origin in our case and branch is the branch on github where we want to push our data main in our case
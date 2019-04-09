# Git Workshop with Knowit, 8. april

##Running the application

#### Prerequisites

[Python3](https://www.python.org/downloads/) 

#### Download the application

1. Open a command line terminal 
 * In *Windows:* cmd, PowerShell or git Bash, *MacOS:* Terminal)
2. Navigate to a folder where you want to clone it into
3. Clone the repo, see code snippet under:

HTTPS:
```
git clone https://github.com/eddiman/git-kurs-april.git
```

SSH:
```
git clone git@github.com:eddiman/git-kurs-april.git
```
See bottom of this readme on how to use SSH

#### Running the application 

1. Open a command line terminal 
  * In *Windows:* cmd, PowerShell or git Bash, *MacOS:* Terminal)
2. Navigate to the folder where you cloned the repository.
3. Run ``` python3 -m pip install virtualenv```
4. When this is done, start the virtual environment: ```python3 -m virtualenv venv```
5. If Windows: ```. venv/Scripts/activate on Windows```, if MacOS/UNIX ```source venv/bin/activate```
6. Write ```pip install -r requirements.txt``` in the command line
7. Start the application by writing ```python main.py```
8. When it has started, navigate to ```localhost:6060``` using the web browser.


## Git commands

Most common commands for git:  

### git init

To create a git repo, enter ```git init```

### git status

Checks the status of the repo. Tells which branch you are working on, and the details about files that 
were added, changed, deleted and etc.

``` 
git status

On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

### git add
Adds a file or a folder to staging, it will then be included when commited. 

```git add <file.ext>```

### git commit
Creates a commit. Recommended to use -m followed by a message in quotation marks. If not used, most users will end up in vim,
if this happens and you don't know what to do, [see stackoverflow](https://stackoverflow.com/questions/9171356/how-do-i-exit-from-the-text-window-in-git)

```
git commit -m "your commmit message here"
```

### git log
Gives you a log of the commits in the repo. Can also display a basic branch visualization graph if --graph flag is used with it. 

```
git log --graph --all
```

### .gitignore

The .gitignore file tells git which files to not include at all in the commits. These files are typically 
local files that are not relevant for the project at all, such as IDE specific files or other development environment files.  

[Link to the projects .gitignore](.gitignore)

There exists a lot of templates for .gitignore, GitHub has a nice repo for this:
[Link to GitHub's .gitignore-template repo](https://github.com/github/gitignore)

____

#### Other useful links

There are also other git tools with UI that can be used instead of the CLI:

[GitKraken](https://www.gitkraken.com/git-client)

[SourceTree](https://www.sourcetreeapp.com)

In order to use GitHub and other hosting services using git, you will have to authenticate yourself using either HTTPS (username and password) or SSH.
While HTTPS is a viable solution for personal and smaller projects, SSH is generally more secure and only needs a setup one-time setup on each machine you are using.

[How to authenticate via SSH in GitHub](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Want to know more about Knowit and career opportunities? See more at [knowit.no/karriere](https://www.knowit.no/karriere/?city=10989)



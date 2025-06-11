# Installing and Using Git on Windows

![Alt Text](assets\githubWhite.jpg)

## Installing Git
- Go to this link: https://git-scm.com/downloads/win
- Download the latest version for windows

## Setting up Git
- Open a windows terminal
- Run 'git' to see if you have it downloaded, should show options
- Set cred's:

git config --global user.name "Your Name"
git config --global user.email "you@example.com"

## Cloning a Repo
- In VS Code or a terminal, navigate to where you want the repo to land
- Example clone:

git clone https://github.com/ashtontheanalyst/python-refresher.git

### Common Commands
git status  
git add .  
git commit -m "some message"  
git push origin main
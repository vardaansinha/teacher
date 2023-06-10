---
toc: true
comments: true
layout: post
title: Tools and Equipment
description: Tools and equipment have changed lives, look at the mobile phone.  Tools, equipment, with the addition of coding can make you immensely more successful in any field.
image: /images/tools.webp
courses: { csse: {week: 0}, csp: {week: 0}, csa: {week: 0} }
categories: [C4.3, C5.0]
type: devops
---

## Make Development Easy
Learning Development tools, working with Projects, is the key to a <mark>rapid entry into Code/Code/Coding</mark>.  A Computer, Git, and an Code Editor are the starting points for coding.  Add Jupyter Notebooks (computational documents) and you bridge a Computer with Data Science.  The beauty of Jupyter Notebooks is that it creates a computational narrative, a document that allows code and data with visual analysis, hypothesis, and conjecture.
- Computers using either MacOS, Windows, or Linux are requirements for the course.  
- <mark>GitHub</mark>, is Git hosted in the Cloud.  It is <mark>the defacto hosting platform for version control and collaboration</mark>. It lets you and others work together on projects from anywhere in the world.  Think of it as the Google Docs for Coders.
   - Version Control is the task of keeping a software system of many versions and configurations well organized.
   - <mark>Version Control History</mark> of files and changes in Version Control System (ie GitHub) is very important!  Ultimately, any Coder will break things or delete things! Looking at older versions and configurations at a microscopic detail is sometimes the only way to unwind bugs.
- <mark>Visual Studio Code</mark> (abbreviations VS Code, VSCode or VSC) is a powerful Code Editor.  VSCode performs a lot of magic and automation behind the scenes to make your Code/Code/Coding life easier.  There is a back-in-the-day story hear, but short version is VSCode qualifies, IMO, to be called and <mark>Integrated Development Environment (IDE)</mark>.  It allows you to Edit files, Build your Code, and Pull/Push Code from and to the GitHub.  FYI, VSCode is an IDE of choice by the instructor, in CompSci classes in the past we have used XCode, Eclipse, and IntelliJ.
- <mark>Jupyter Documents (.ipynb)</mark> is a document format for creating and sharing computational information.  These documents allow you to compute segments of Python, JavaScript or Java code as you are taking notes.  IMO, these documents are very powerful to gain a quick understanding of coding concepts.  Jupyter documents are often called "notebooks".


### Equipment, accounts and tools
- A laptop, <mark>bring a laptop to class every day with the Development Tools installed</mark> on it.  Preferred lapytos ar MacOS or Windows.   Computers issued by the School, ie Chromebook, are not as effective because of the restrictions placed on adding software by PUSD.  <mark>If you only have access to a school issued Chromeboo, we will provide an option to access a Linux machine on AWS.</mark>
- GitHub Account, VSCode will be used to clone/push/pull changes. GitHub is where we store and share code in the cloud, think of Google Docs but for Code.  Setup GitHub with a personal ID, not a school ID.
- GitHub Pages will be used to host your personal web site, notes, and experiences. <mark>Review GitHub concepts 2-min</mark> [https://www.youtube.com/watch?v=phGdqJB6ep0](https://www.youtube.com/watch?v=phGdqJB6ep0)
- Jupyter Documents will be used in conjunction with GitHub Pages to build running Java Code in to your Technical Notes. <mark>Review Jupyter basics 6-min</mark> [https://www.youtube.com/watch?v=3jZYC9rGrNg](https://www.youtube.com/watch?v=3jZYC9rGrNg)
- Slack Account, install App on Laptop, get used to reading announcements. Slack is a messaging tool similar to Discord, there will be daily messages in this class.
- VSCode is the code editor we will be using in this class.  VSCode is more than and editor, it is called and Interactive Development Environment (IDE). 
- Tools and Terminal Installs
   - Anaconda is the environment manager.  Conda is an open-source package and environment management system that runs on Windows, macOS, and Linux.  It helps you manage you tools in a controlled environment.
   - Homebrew (```brew install```) for MacOS will be used to install tools,  Apple's MacOS does not have these by default.
   - On Windows we will install Windows Subystem for Linux (WSL Ubuntu), then use ```sudo apt install` installs the packages (Java, Python) you need for Development that Ubuntu did not include.
   - On Linux machines we will use ```sudo apt install``` for tools installation. An AWS Account for cloud computing will be required.  , account access will be provided by Teacher.  AWS Cloud Computing and Electric Cloud Computing (EC2's) will be used to run Development Enviornment from the Internet.

### GitHub Account
- Follow instruction [https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account)  Use your own personal/permanent email... NOT SCHOOL!!! GitHub belong to you.

### MacOS 1st Time Developer
> VSCode install
- Install [VSCode](https://code.visualstudio.com/docs/setup/mac)

> Anaconda install
- Download for MacOS: [Anaconda](https://www.anaconda.com/products/distribution)
- Run Install: Answer yes to questions

> Homebrew install
- Copy and Paste to Install from Terminal [Homebrew](https://brew.sh)
    - Copy ```bash ... curl ...```  command using copy box on website
    - Launch ```terminal``` from search bar
    - Paste ```bash ... curl ...``` command into Terminal ... 
    - Make sure command starts, this should provide feedback/output in terminal and could take a long time, like 10-min, there could be a  prompt in the middle, at about 5-minutes.  Follow any on screen instructions provided in terminal output to finish.
- Homebrew installs a tool called "brew" which helps add and manage developer packages on MacOS.

> At this point, the next task is to prepare tools.  <mark>You must start a new Terminal</mark>.  Now the Terminal prompt should be <mark>prefixed with (base)</mark>.  If not, you need to go back to Anaconda install.
- Open new Terminal, your prompt should look like this...
```bash
(base) iMac:~ jmort1021$
```

> Key Packages needed on MacOS
- <mark>Close and Start a new terminal</mark>, run each command in Terminal
```bash
$ brew list # list packages
$ brew update # update package list
$ brew upgrade # upgrade packages
$ brew install git  # install latest git
$ brew install python # install python3 for development
$ python --version # version of python3 installed
```

### Windows 1st Time Developer
> VSCode install using WSL. Windows users have option to have best of Windows and Linux while developing within VSCode.
- Install [VSCode using WSL]({{site.baseurl}}/techtalk/vscode-wsl).
- Required review, become familiar with [Windows WSL development](https://code.visualstudio.com/docs/remote/wsl-tutorial)

> Anaconda install on WSL.
- Try the exact commands in WSL Command / Powershell.  
- Only if there is a wget error... To find the latest Linux-x86 distribution hover over ```64-Bit (x86) Installer``` of this page: https://www.anaconda.com/download#downloads.  Hover over  wget and Anaconda3 commands based on new link.
```bash
> PS C:\Users\UserName> wsl  # Windows prompt to WSL command
$ cd /tmp
$ wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
$ chmod +x Anaconda3-2023.03-1-Linux-x86_64.sh
# Answer yes to all the prompts
$ ./Anaconda3-2023.03-1-Linux-x86_64.sh
```

> At this point, the next task is to prepare for Packages, Jupyter Notebooks, and Kernels.  <mark>You must start a new WSL Command / Powershell</mark>.  Now the WSL prompt should be <mark>prefixed with (base)</mark> from Anaconda install.  If not, you need to go back to Anaconda install.
- Open Command / Powershell.  If you are not looking like this you need to back up.
```bash
> PS C:\Users\ShayM> wsl  # Windows prompt
(base) shay@MSI:/mnt/c/Users/ShayM$ cd ~ # WSL prompt
(base) shay@MSI:~$ # WSL home, best place to install files
```

> Key Packages needing update on WSL Ubuntu
- In a WSL Command / Powershell install Python3
```bash
$ sudo apt list # list packages
$ sudo apt update # update package list
$ sudo apt upgrade # upgrade packages
$ sudo apt install python3 python3-pip # install python3 and pip3 for development
$ python --version  # version of python3 should be shown


### Jupyter Install and Kernels (MacOs and WSL)

> Install Jupyter and check python kernel 
```bash
(base) id:~$ conda --version 
(base) id:~$ conda install jupyter # install jupyter
(base) id:~$ jupyter kernelspec list # list installed kernels
Available kernels:
  python3    /home/shay/.local/share/jupyter/kernels/python3
```

### VSCode Start GitHub Project
> Start Pages/Fastpages from [GitHub Setup Instructions](https://github.com/fastai/fastpages#setup-instructions)
- [Recommended Video - 27 minutes](https://www.youtube.com/watch?v=sepml4GLLSM)
- Verify GitHub pages is running
- Clone and Open project in VSCode
```bash
(base) id:~$ mkdir -p vscode # make a vscode directory
(base) id:~$ cd vscode # change to the directory
(base) id:~$ git clone https://github.com/nighthawkcoders/pages.git # change to your repo
(base) id:~$ code . # open VSCode projects in directory
```
- Push a minor "markdown" change and Verify on GitHub [https://code.visualstudio.com/docs/editor/versioncontrol#_git-support](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support)
- Verify "markdown" change on GitHub Pages
- Create a new Jupyter notebook and publish to _notebooks directory [https://code.visualstudio.com/docs/datascience/jupyter-notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
### VSCode Marketplace and Extensions

<div>
    <div style="float: left; margin: 0px 10px 10px 0px;">
        <a href="https://marketplace.visualstudio.com/vscode">
            <img atl="Roles and Agile" src="{{site.baseurl}}/images/extensions.png" title="VS Code Marketplace"
            width="250">
        </a>
    </div>
    <div>
        <hr>
        <p>
        Visual Studio Code claims to provide just the tools a developer needs for a quick code-build-debug and version control cycle.  It provides a Market Place for enhancements and more complex workflows.  <mark>Before adding extensions, clone projects</mark> and see what is requested or added.  Here are some extension that were added through that process or that I have added...
        </p>
        <ul>
            <li>
                <mark>In marketplace</mark> there are several extensions for Python, Python Intellisense, Python Extension Pack
            </li>
            <li>
                <mark>Jupyter</mark>: This supports build jupyter ipynb files from within VS Code
            </li>
            <li>
                <mark>Code Spell Checker</mark>: Got to have it when building documents, particularly if you spell and typo like the Teacher
            </li>
            <li>
                <mark>IntelliCode</mark>: Got to have it when creating a code file, it will sense type of code by extension.  Also, it help with syntax as you are coding.
            </li>
        </ul>
        <p>
        <mark>Review Details in Marketplace for better explanation of purpose of the things explained above</mark>. There is a lot more!  As you need Git help look at things like <mark>Git History and GitLens</mark>.  Or, perhaps you enjoy Vim and want Vim emulation for editing, their is an extension for that.  Later, there may be interest in AWS Toolkit or Deploy extensions.  We will learn more about Marketplace Extensions as we do more.
        </p>
        <hr>
    </div>
</div>

### VSCode for Python Extensions
- VS Code [https://code.visualstudio.com/docs/languages/python](https://code.visualstudio.com/docs/languages/python)
    - Install Python, Python Environment Manager, Python Extension Pack, Pylance
    - Install Jupyter, Jupyter Keymap
    - Install IntelliCode, IntelliCode API Usage Examples
    - Windows machines install WSL Remote Development


## Hacks
Students need to demonstrate all these tools running to Scrum Team and then the Teacher.  Problems need to be worked out quickly.  Before asking Teacher ask 3 other students.  <mark>Do not delay in Tool Setup task, there will be no late makeup for points!!!</mark>  Tool and Equipment setup is like attendance, without Tools and Equipment you are effectually absent.
- Provide a comment on this page to show Tool success
- Hint.  Make a simple comment "Working on it".  This can be edited by clicking on Time Stamp of post; at this point you will see triple dots (...); clicking dots provides an Edit option; clicking Edit takes you to a friendly "Markdown editor".  Enjoy this editor, my suggestion is build your entire message in thi editor and/or build personal message in Fastpages / GitHub pages  "_post" and share the following.
    - Share link to personal Fastpages / GitHub pages running on github.io.  My suggestion is to change index.html to show it is really yours.
    - Share link to a new page (_posts) in your Fastpages project show use of  Markdown and/or HTML fragments.  You will need to learn special date requirements of a file as well as a little Markdown or HTML.
    - Share link to your 1st Jupyter notebook (_notebooks) showing usage of Python: print ("Hello")
    - Capture image/screen capture of Fastpages project showing use of an Integrated Development Environment (VS Studio)
    - Share link showing your GitHub insights.  This is your personal activity of commit history.

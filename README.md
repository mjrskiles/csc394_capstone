## How to build the project

## Dependencies

### Required software

MySQL Server

Python3

### Required python modules

django

mysqlclient

### Things that you might need to do

If mysqlclient python module fails to install, try the following steps in this order:

These instructions are specific to macOS.

- Install homebrew (a package manager of macOS)
    - https://brew.sh/
      - Follow the instructions on that site to paste a command into your terminal
- Install mysql from homebrew
    - `$ brew install mysql`
    - Add mysql to your PATH
      - `$ export PATH=$PATH:/usr/local/mysql/bin`
    - Note that mysqlclient python module will fail to install without a proper installation of MySQL Server
- Install Xcode command line tools (to get updated libraries for clang if mysqlclient fails to build)
    - `$ xcode-select --install`

## Working with git

### Typical workflow

It's a good idea to pull often and use branches when working with git.

#### Simplified workflow (working on the master branch)

- Each time you start working on the project, first:
  - `$ git pull`
    - If there are merge errors, you need to fix them.
    - Merge errors look something like
    ```
    >>>>>>>>>>HEAD
    // some code from your local 
    // branch
    ==========
    // Some different code that was
    // pulled down from the git repo
    >>>>>>>>>> 08ab7298b7c (some hex number)
    ```
    - You need to either pick which version is correct and delete the other one
    OR sometimes you need to combine elements from both. The point is you need to make that section work.
    - Once you're done fixing the errors in your source files
      - `$ git commit -a -m "Type a message saying you fixed merge errors"`
      - Committing tells git that you fixed the errors. git will assume everything is fine after you commit.
  - After you pull and fix any errors, that's when you make changes to the code.
  - After you make some changes, and everything seems to be working:
    - `$ git commit -a -m "You type a commit message here explaining what you did"`
      - The -a flag means "all". Commits changes to all modified files.
      - The -m flag means "message". If you leave out the -m git will open a text editor (probably vi) and ask you to type a message.
        - Side note: If you do find yourself in vi, you can quit by typing `:q` and hitting enter.
          - To start typing in vi press `i`
          - To navigate press esc and use hjkl keys to move the cursor
          - When you're done typing your commit message, save and quit with esc, then `:wq`
    - `$ git pull`
      - Fix merge errors if there are any
      - The reason you pull right now is so that you don't push errors up to the github repo.
      It's better to fix them locally first.
    - `$ git push`
  - Repeat the process as necessary

#### Working with branches

Working with branches is extremely useful and safer than working on the master branch.

The basic idea is that the master branch should always be a functional version of the project that
builds correctly.

By creating a new branch and making/testing changes there first, you can 
- Maintain a stable master version of your project
- Break things without being afraid of not being able to revert your changes

To make a new branch

`$ git checkout -b <name>`
  - git checkout switches to a branch called `name`
  - the -b flag creates a new branch if it doesn't exist
  - git checkout -b combined creates a new branch called `name` and switches to it

To switch between branches

`$ git checkout <branch_name>`

Often you need to switch between the master branch and the one you're working on.

`$ git checkout master`

switches to the master branch.

Once you're ready to add your changes back into the master branch.

(Assuming you're on your branch that you made changes on named `dev_branch`)

- `$ git merge master`
  - This command compares the master branch the one you're on and tries to merge them.
  most of the time this works fine. Sometimes git can't merge them automatically and you need to 
  fix the errors as mentioned above.
  - The reason you merge the master _into_ your development branch is because you should always avoid
  making breaking changes to the master branch
- `$ git checkout master`
  - This switches back to the master branch
- `$ git merge dev_branch`
  - Since you already fixed the merge errors on the dev branch this should work fine.
- `$ git push`

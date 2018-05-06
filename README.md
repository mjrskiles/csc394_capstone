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
    - $ brew install mysql
    - Add mysql to your PATH
      - $ export PATH=$PATH:/usr/local/mysql/bin
    - Note that mysqlclient python module will fail to install without a proper installation of MySQL Server
- Install Xcode command line tools (to get updated libraries for clang if mysqlclient fails to build)
    - $ xcode-select --install

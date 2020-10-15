# Data Engineering 101

This repo is a how to guide on learning SQL and Python to get the first data engineering job.


## Create git repo

A repository is a project or place to keep your code, this area allows people to work together and collaborate through 'branching'.

Create a new directory (folder) somewhere on your machine.

    mkdir my-project

**Note:** Do not have any whitespace in the name.

Enter the new directory my-project

    cd my-project

Create a git repository:

    git init


Create your README which contains instruction of what your project does and how to use it.

After you've created the README.md file, stage it by `add`ing it.

    git add README.md

Attach a message to the commit to tell people what changes you've made.

    git commit -m "First commit, woo!! Added the README"

Then push (send) it to the central repo to be added in:

    git push origin master


## Branching

We use 'branches' to take a 'copy' of the code, make changes and then push (send) it back to the origin (central repository). Here we can then create a pull request, where someone can review your code and if accepted, merge it to the master/main branch.

    git checkout -b my-new-cool-feature

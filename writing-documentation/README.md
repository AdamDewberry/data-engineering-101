# README.md

## What?

A README contains all of the instructions needed to run and contribute to a project.

## Why?

If someone tried to run your project, how would they know how to do it? Where should they begin, what do they need to know?

If there was no documentation, the project may be near useless if it were to be run by another person or team, they wouldn't know how; a README solves this and transfers knowledge.

No single individual works on the same project forever, in the same team or company; if you were to inherit a project or join a team which has an established code base, write your README to a standard you'd expect to see an existing one in - clear, concise and informative.

## How?

Create a file called `README.md` in the root of your project and populate it with lots of lovely [markdown](./Markdown.md), in clear sections detailing all the relevant information to the project. There should never be domain knowledge of the code in your head, everything important should be documented.

In your project directory, you can run the following to create it:

    touch README.md

You should include sections such as:

- Introduction
- Getting started
- Dependencies
- Installation
- How to run this project
- Contributing
- License

Bearing in mind you may not need all of these, they are general guidelines of the sort of information you should include.

When writing a README, imagine that you're seeing the project for the first time, what information do you need to get it running? Is there any required knowledge in your head that a new user would need? What are the common points of failure, specific steps or edge cases?


The following are good examples of what a README should look like:  
- [Python](https://github.com/python/cpython/blob/master/README.rst)
- [AWS CLI](https://github.com/aws/aws-cli/blob/develop/README.rst)
- [Terraform](https://github.com/hashicorp/terraform/blob/master/README.md)

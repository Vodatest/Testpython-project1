# Testpython-project1

Github action project that triggers linter to run on each push

## Github Action using Pre-Commit, PyLint and Pytest

Github actions is the way that we have to apply CICD or run customized workflows

You can take a look at the https://pre-commit.com/#intro

The funniest thing is that pre-commit can be added to a workflow as an automated task, we can add unit testing, check the coverage, etc. All this task can be executed after push our code or create a pull request.

## Setting up Github workflow

Create a folder .github/workflows and in it copy the pylint.yml file to define the workflow. We have used the workflow to install the pylint instead of downloading it locally. 

OR 

You can even use Github provided configurations to define the workflow.

<img width="522" alt="image" src="https://user-images.githubusercontent.com/116036346/199461779-82478c5a-4531-4dea-8172-45fde19ca7ee.png">

The **pylint.yml** in **Testpython-project1/.github/workflows/** workflow will run the pytest suite in addition to running the pre-commit tests.

**For Plylint configuration**

.pylintrc can be used to configure pylint checks

## The documentation that I used to create this repository is:

https://pre-commit.com/#install

https://pre-commit.com/#usage

https://composed.blog/python/pre-commit

https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e

https://verdantfox.com/blog/view/how-to-use-git-pre-commit-hooks-the-hard-way-and-the-easy-way

Some hooks examples:

https://github.com/pre-commit/pre-commit-hooks

Information about Pytest:

https://docs.pytest.org/en/6.2.x/customize.html


test

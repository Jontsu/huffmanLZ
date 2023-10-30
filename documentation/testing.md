## Unit tests

Test and branch coverage stands at 100%.

Unit tests have been implemeneted using Python's unittest unit testing framework. Test coverage and branch coverage has been implemented using Python's coverage package. I have only written tests for the files that relate to the algorithms. I have not written tests for files that relate to the UI.

Unit tests and test coverage can be ran from terminal with commands

```bash
coverage run -m unittest discover
coverage html
```

![Test coverage](graph/testcoverage.png)

Unit tests and branch coverage can be ran from terminal with commands

```bash
coverage run --branch -m unittest discover
coverage html
```

![Branch coverage](graph/branchcoverage.png)

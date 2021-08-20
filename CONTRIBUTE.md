# Contributing to DFXML's Python code base


## Installable tools versus in-place scripts

The [`dfxml/bin/`](dfxml/bin/) directory contains scripts for interacting with DFXML.  Some of the tools are installed in the command-line `$PATH` when the `dfxml` package is installed.

If there is a request to add a tool to the package's installed-tools list, the tool should have these implemented:
1. A unit test suite that exercises the tool's command line features, such as flags, and `pytest` tests to confirm expected output.
2. A documentation page, preferably a README alongside the unit test suite.  The documentation should include command-line usage.
3. A row in [`dfxml/bin/README.md`](dfxml/bin/README.md)'s table of installed tools, linking to the documentation.


## Version management

**Note that DFXML 1.0.2 DOES NOT YET follow SEMVER practices.**

This project plans to adopt [SEMVER](https://semver.org/) to denote expected stability of its offered resources.  The project *has not yet* adopted SEMVER; when it does, a note will be added to the README.

Once a SEMVER-adherent major version is declared, backwards-incompatible commits will be merged into the `release-x.0.0` branch (where `x` is the next major version) instead of `develop`.

Following SEMVER's `major.minor.patch` version designation:
* The `major` version will increment on deploying changes that are backwards-incompatible with the prior major release.
* The `minor` version will increment on new functionality being added.
* The `patch` version will increment on new tests for existing functionality being added, or a bug being fixed, with some discretion to be used for any needed interface corrections.

The following are this repository's policies on backwards compatibility for this project's resources.


### Version of the DFXML Python code base

The overall package version of `dfxml` is stored in one location, the `__version__` variable of `dfxml/__init__.py`.

Other resources may track their own version independently.


### Package resources

The set of command-line tools offered in the package (defined in `setup.cfg`) is considered in-scope for backwards compatibility.


### Command-line functionality

Tests that illustrate expected command-line behavior are available under the [`tests/`](tests/) directory.  See the `Makefile`s under the directories named after the provided tools.  Recipes that include activating a virtual environment (e.g. `source $(tests_srcdir)/venv/bin/activate`) show command line execution patterns.

The command-line functionality demonstrated by the `Makefile`s under `tests/` is considered in-scope for backwards compatibility.


### Module functionality

This project uses the [`pytest`](https://docs.pytest.org) framework to run unit tests.  These tests encode the expected behaviors of command-line results, and of module functions.  Tests generally follow a "Ground-truth comparison" model, where an expected set of results is compared to a computed set of results (generally, as `expected_X == computed_X`).

The module functionality exercised by the `pytest` unit tests is considered in-scope for backwards compatibility.


## Merge model

On adoption of SEMVER, this project will follow the `git-flow` merge model.  In short:
* The `main` branch will contain tagged release commits only.
* The `develop` branch will be the target of Pull Requests for new features.
* `release-x.y.z` branches will be made off of `develop` when a new release is to be tagged , and merged into `main` and back into `develop`.

The above practice can be seen illustrated in the first figure on [this page](https://nvie.com/posts/a-successful-git-branching-model/).

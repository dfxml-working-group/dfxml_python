# DFXML
[![Build Status](https://github.com/dfxml-working-group/dfxml_python/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/dfxml-working-group/dfxml_python/actions/workflows/continuous-integration.yml/)

Welcome to the Digital Forensics XML (DFXML) git repository housing the Python codebase.

## Overview
DFXML is a file format designed to capture metadata and provenance information about the operation of software tools in a systematic fashion. The original motivation was to represent the output of digital forensics tools, and specifically the SleuthKit tools. DFXML was expanded to operate with the [`bulk_extractor`](https://github.com/simsong/bulk_extractor) digital forensics tool. DFXML was then expanded to cover the output of the [`tcpflow`](https://github.com/simsong/tcpflow) tool. With the lessons we learned form handling all of those programs, we were able to separate out use of DFXML for documenting runtime provenance of any program, and the use of DFXML to represent specific digital forensics artifacts like files and hash sets.

## Content of the repository
This repository contains original DFXML implementations in Python for writing DFXML files, as well as an assortment of tools for reading, generating, and processing DFXML files. The folder layout is as follows:

```
python/		- Python source files (dfxml-module and several tools)
python/dfxml/	   	- The Python DFXML module
python/dfxml/tests 	- Unit tests for the DFXML modules.
python/tests	   	- Unit tests for the DFXML tools.
samples/	   	- Exemplary .dfxml-files
schema/		- The DFXML schema.  Not directly tracked; run `make schema-init` to retrieve.
```

## Usage

### Installation
In order to install the dfxml-module for using it in your scripts, you can rely on Python's package manager `pip` to call `install` within the directory, where `setup.py` lives:

```shell
cd dfxml_python/python
pip3 install .
```
For an initial overview about the provided tools, please have a look at `python/README.md`

### Using this as a git submodule
This DFXML module can be used as a submodule inside another git module.

We've noticed that people will typically start development in these modules, and then want to push the changes back to the master. This causes a problem with git, because when you've done the development, you weren't at the head. If this happens to you, you will need to create a new branch for your current location, then checkout the master branch, and then merge your branch into the master. You can do that this this sequence of git commands:

Sometimes when working with DFXML as a submodule, you may get off the master and end up with a disconnected head. If so, use this to get back on the master:
```
$ git checkout -b newbranch
$ git checkout master
$ git merge newbranch
$ git branch -d newbranch
```

or, more succinctly:

```
$ git checkout -b tmp  ; git checkout master ; git merge tmp ; git branch -d tmp
```

### Usage with the DFXML Schema
The [DFXML schema](https://github.com/dfxml-working-group/dfxml_schema) is tracked here similarly to a Git submodule, but without using the Git submodule mechanism to avoid some operational deployment issues.  If you would like to check out the tracked schema version, run `make schema-init`.  It is only necessary to check this out if you are testing validation of DFXML content against the schema.

## Release Notes
- 2018-07-22 @simsong Significant redesign of the Python library.
  - Configure Python module with a module directory and moved most of `dfxml.py` to `__init__.py`.
  - Renamed `Objects.py` to be `objects.py` since Python3 naming conventions use only lower case filenames.
  - Moved tests to a `test/` subdirectory and redesigned most of them to work with py.test. The tests that require arguments on the python command line were not updated.
  - Removed calls to logging withing files and modules that are not tests, so that using DFXML doesn't inherently start emitting logging messages.
  - Removed calls to logging in Objects tests where the only thing that the test program was logging was the fact that it had run. py.test will provide similar logging now.

--- Simson Garfinkel, May 6, 2021

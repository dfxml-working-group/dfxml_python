#!/usr/bin/make -f

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

# Bash selection is described in the top-level Makefile.
ifeq ($(shell basename $(SHELL)),sh)
SHELL := $(shell which /bin/bash 2>/dev/null || which /usr/local/bin/bash)
endif

top_srcdir := $(shell cd .. ; pwd)

PYTHON3 ?= $(shell which python3.9 2>/dev/null || which python3.8 2>/dev/null || which python3.7 2>/dev/null || which python3.6 2>/dev/null || which python3)
ifeq ($(PYTHON3),)
$(error python3 not found)
endif

all: \
  all-make_differential_dfxml \
  all-walk_to_dfxml

.PHONY: \
  all-make_differential_dfxml \
  all-walk_to_dfxml \
  check-mypy \
  check-mypy-strict

all-make_differential_dfxml: \
  .venv.done.log
	$(MAKE) \
	  --directory make_differential_dfxml

all-walk_to_dfxml: \
  .venv.done.log
	$(MAKE) \
	  --directory walk_to_dfxml

.venv.done.log: \
  $(top_srcdir)/setup.cfg \
  $(top_srcdir)/setup.py \
  requirements.txt
	rm -rf venv
	$(PYTHON3) -m venv \
	  venv
	source venv/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools
	source venv/bin/activate \
	  && cd $(top_srcdir) \
	    && pip install \
	      --editable \
	      .
	source venv/bin/activate \
	  && pip install \
	    --requirement requirements.txt
	touch $@

check: \
  all-make_differential_dfxml \
  all-walk_to_dfxml \
  check-mypy
	source venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

#TODO - Type-checking would best be done against all of ../dfxml, when someone finds some time to do so.
check-mypy: \
  check-mypy-strict
	source venv/bin/activate \
	  && mypy \
	    ../dfxml/bin/idifference.py \
	    ../dfxml/bin/summarize_differential_dfxml.py \
	    ../dfxml/__init__.py \
	    ../dfxml/objects.py \
	    misc_bin_tests \
	    misc_object_tests
	@echo "INFO:tests/Makefile:mypy is currently run against a subset of the dfxml directory." >&2

#TODO - Strict type-checking is another long-term goal, likewise eventually done against all of ../dfxml.
check-mypy-strict: \
  .venv.done.log
	source venv/bin/activate \
	  && mypy \
	    --strict \
	    ../dfxml/bin/idifference2.py \
	    ../dfxml/bin/make_differential_dfxml.py \
	    ../dfxml/bin/walk_to_dfxml.py \
	    make_differential_dfxml \
	    walk_to_dfxml \
	    *.py

clean:
	@$(MAKE) \
	  --directory make_differential_dfxml \
	  clean
	@$(MAKE) \
	  --directory walk_to_dfxml \
	  clean
	@rm -f \
	  .venv.done.log
	@rm -rf \
	  venv

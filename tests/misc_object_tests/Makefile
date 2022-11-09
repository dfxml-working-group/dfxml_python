#!/usr/bin/make -f

# This software was developed at the National Institute of Standards
# and Technology in whole or in part by employees of the Federal
# Government in the course of their official duties. Pursuant to
# title 17 Section 105 of the United States Code portions of this
# software authored by NIST employees are not subject to copyright
# protection and are in the public domain. For portions not authored
# by NIST employees, NIST has been granted unlimited rights. NIST
# assumes no responsibility whatsoever for its use by other parties,
# and makes no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

# Bash selection is described in the top-level Makefile.
ifeq ($(shell basename $(SHELL)),sh)
SHELL := $(shell which /bin/bash 2>/dev/null || which /usr/local/bin/bash)
endif

top_srcdir := $(shell cd ../.. ; pwd)

PYTHON3 ?= python3

OBJECTS := $(top_srcdir)/dfxml/objects.py

SAMPLES_DIR := $(top_srcdir)/samples

TOOLS_DIR := $(top_srcdir)/dfxml/bin

all: \
  check

.PHONY: \
  check-diff_file_ignore-py3 \
  check-versioned

check: \
  check-diff_file_ignore-py3 \
  check-libraries-py3 \
  check-versioned
	source $(top_srcdir)/tests/venv/bin/activate \
	  && $(PYTHON3) "$(TOOLS_DIR)/cat_partitions.py" \
	    12345678:$(SAMPLES_DIR)/difference_test_0.xml \
	    87654321:$(SAMPLES_DIR)/difference_test_1.xml \
	    > __cat_patterns_test.sh.dfxml
	xmllint \
	  --format \
	  __cat_patterns_test.sh.dfxml \
	  > _cat_patterns_test.sh.dfxml
	rm \
	  __cat_patterns_test.sh.dfxml
	mv \
	  _cat_patterns_test.sh.dfxml \
	  cat_patterns_test.sh.dfxml

check-diff_file_ignore-py3: \
  diff_file_ignore_sample-py3.dfxml \
  diff_file_ignore_test.py
	source $(top_srcdir)/tests/venv/bin/activate \
	  && $(PYTHON3) diff_file_ignore_test.py --debug diff_file_ignore_sample-py3.dfxml

check-libraries-py3:
	source $(top_srcdir)/tests/venv/bin/activate \
	  && $(PYTHON3) LibraryObject_write_test.py LibraryObject_py3_test.dfxml
	source $(top_srcdir)/tests/venv/bin/activate \
	  && $(PYTHON3) LibraryObject_read_test.py LibraryObject_py3_test.dfxml

check-versioned:
	$(PYTHON3) $(OBJECTS)
	source $(top_srcdir)/tests/venv/bin/activate \
	  && $(PYTHON3) DFXMLObject_program_test.py \
	    $(SAMPLES_DIR)/difference_test_0.xml \
	    vi \
	    8.0

clean:
	rm -f difference_counts_test.py-d*
	rm -f cat_partitions_test.sh.dfxml
	rm -f diff_file_ignore_sample-py3.dfxml
	rm -f LibraryObject_py3_test.dfxml
	rm -f *~


diff_file_ignore_sample-py3.dfxml: \
  $(OBJECTS) \
  diff_file_ignore_sample_dfxml_test.py
	rm -f _$@
	source $(top_srcdir)/tests/venv/bin/activate \
	  && $(PYTHON3) diff_file_ignore_sample_dfxml_test.py --debug _$@
	mv _$@ $@

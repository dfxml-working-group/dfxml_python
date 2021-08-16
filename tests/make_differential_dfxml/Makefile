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

top_srcdir := $(shell cd ../.. ; pwd)

tests_srcdir := $(top_srcdir)/tests

all: \
  differential_dfxml_test_by_path_01.txt \
  differential_dfxml_test_by_path_23.txt \
  differential_dfxml_test_by_times_01.txt \
  differential_dfxml_test_by_times_23.txt

check: \
  differential_dfxml_test_by_path_01.txt \
  differential_dfxml_test_by_path_23.txt \
  differential_dfxml_test_by_times_01.txt \
  differential_dfxml_test_by_times_23.txt
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

clean:
	@rm -f \
	  *.dfxml \
	  *.txt
	@#Restore Git-tracked version of these files, so deletions aren't accidentally committed.
	@git checkout \
	  -- \
	  differential_dfxml_test_by_path_01.txt \
	  differential_dfxml_test_by_path_23.txt \
	  differential_dfxml_test_by_times_01.txt \
	  differential_dfxml_test_by_times_23.txt \
	  || true

differential_dfxml_test_01.dfxml: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/dfxml/make_differential_dfxml/__init__.py \
  $(top_srcdir)/samples/difference_test_0.xml \
  $(top_srcdir)/samples/difference_test_1.xml
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && make_differential_dfxml \
	    $(top_srcdir)/samples/difference_test_0.xml \
	    $(top_srcdir)/samples/difference_test_1.xml \
	    > __$@
	xmllint \
	  --format \
	  __$@ \
	  > _$@
	rm __$@
	mv _$@ $@

differential_dfxml_test_by_path_01.txt: \
  $(top_srcdir)/bin/summarize_differential_dfxml.py \
  differential_dfxml_test_01.dfxml
	source $(tests_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/bin/summarize_differential_dfxml.py \
	    --debug \
	    --sort-by path \
	    differential_dfxml_test_01.dfxml \
	    > _$@
	mv _$@ $@

differential_dfxml_test_by_times_01.txt: \
  $(top_srcdir)/bin/summarize_differential_dfxml.py \
  differential_dfxml_test_01.dfxml
	source $(tests_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/bin/summarize_differential_dfxml.py \
	    --debug \
	    --sort-by times \
	    differential_dfxml_test_01.dfxml \
	    > _$@
	mv _$@ $@

differential_dfxml_test_23.dfxml: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/dfxml/make_differential_dfxml/__init__.py \
  $(top_srcdir)/samples/difference_test_2.xml \
  $(top_srcdir)/samples/difference_test_3.xml
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && make_differential_dfxml \
	    $(top_srcdir)/samples/difference_test_2.xml \
	    $(top_srcdir)/samples/difference_test_3.xml \
	    > __$@
	xmllint \
	  --format \
	  __$@ \
	  > _$@
	rm __$@
	mv _$@ $@

differential_dfxml_test_by_path_23.txt: \
  $(top_srcdir)/bin/summarize_differential_dfxml.py \
  differential_dfxml_test_23.dfxml
	source $(tests_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/bin/summarize_differential_dfxml.py \
	    --debug \
	    --sort-by path \
	    differential_dfxml_test_23.dfxml \
	    > _$@
	mv _$@ $@

differential_dfxml_test_by_times_23.txt: \
  $(top_srcdir)/bin/summarize_differential_dfxml.py \
  differential_dfxml_test_23.dfxml
	source $(tests_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/bin/summarize_differential_dfxml.py \
	    --debug \
	    --sort-by times \
	    differential_dfxml_test_23.dfxml \
	    > _$@
	mv _$@ $@

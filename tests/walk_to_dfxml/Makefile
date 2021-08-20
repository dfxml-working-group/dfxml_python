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
  walk_ignore_genprops.dfxml \
  walk_ignore_hashes.dfxml

.scaffolding.done.log:
	rm -rf walk_ignore_test
	mkdir -p walk_ignore_test/foo/bar/baz
	echo 'contents c' > walk_ignore_test/foo/bar/baz/c
	echo 'contents b' > walk_ignore_test/foo/bar/b
	echo 'contents a' > walk_ignore_test/foo/a
	touch $@

check: \
  walk_ignore_genprops.dfxml \
  walk_ignore_hashes.dfxml
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

clean:
	@rm -f \
	  .scaffolding.done.log \
	  *.dfxml
	@rm -rf \
	  walk_ignore_test/

walk_ignore_genprops.dfxml: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/dfxml/bin/walk_to_dfxml.py \
  .scaffolding.done.log
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && cd walk_ignore_test \
	    && walk_to_dfxml \
	      -i atime \
	      -i ctime \
	      -i crtime \
	      -i gid \
	      -i inode \
	      -i mtime@d \
	      -i uid \
	      > ../__$@
	xmllint \
	  --format \
	  __$@ \
	  > _$@
	rm __$@
	mv _$@ $@

walk_ignore_hashes.dfxml: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/dfxml/bin/walk_to_dfxml.py \
  .scaffolding.done.log
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && cd walk_ignore_test \
	    && walk_to_dfxml \
	      --ignore-hashes \
	      > ../__$@
	xmllint \
	  --format \
	  __$@ \
	  > _$@
	rm __$@
	mv _$@ $@

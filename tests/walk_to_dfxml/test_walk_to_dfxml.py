#!/usr/bin/env python3

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

__version__ = "0.2.0"

import logging
import os

import pytest

import dfxml.objects as Objects

_logger = logging.getLogger(os.path.basename(__file__))

@pytest.fixture
def srcdir() -> str:
    retval = os.path.dirname(__file__)
    return retval

def test_walk_ignore_genprops(srcdir):
    files_encountered = 0
    for (event, obj) in Objects.iterparse(os.path.join(srcdir, "walk_ignore_genprops.dfxml")):
        if not isinstance(obj, Objects.FileObject):
            continue
        files_encountered += 1
        for propname in [ "atime", "ctime", "crtime", "gid", "inode", "mtime", "uid" ]:
            try:
                assert getattr(obj, propname) is None, "Found property that should have been ignored."
            except:
                if propname == "mtime" and obj.name_type != "d":
                    continue
                _logger.error("obj.filename = %r.", obj.filename)
                _logger.error("propname = %r.", propname)
                raise
    assert files_encountered > 0, "Encountered no files in walk_ignore_genprops.dfxml."

def test_walk_ignore_hashes(srcdir):
    files_encountered = 0
    for (event, obj) in Objects.iterparse(os.path.join(srcdir, "walk_ignore_hashes.dfxml")):
        if not isinstance(obj, Objects.FileObject):
            continue
        files_encountered += 1
        for propname in Objects.FileObject._hash_properties:
            try:
                assert getattr(obj, propname) is None, "Found hash property when none was expected."
            except:
                _logger.error("obj.filename = %r.", obj.filename)
                _logger.error("propname = %r.", propname)
                raise
    assert files_encountered > 0, "Encountered no files in walk_ignore_hashes.dfxml."

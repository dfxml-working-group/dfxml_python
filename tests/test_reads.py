#!/usr/bin/env python3

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

import os

import pytest

import dfxml
import dfxml.objects


def nop(x : object) -> None:
    pass

@pytest.fixture
def top_srcdir() -> str:
    srcdir = os.path.dirname(__file__)
    retval = os.path.join(srcdir, "..")
    assert os.path.isdir(os.path.join(retval, "samples")), "Hard-coded expected path not found, '${top_srcdir}/samples/'."
    return retval

@pytest.fixture
def difference_test_0_filepath(top_srcdir : str) -> str:
    retval = os.path.join(top_srcdir, "samples", "difference_test_0.xml")
    assert os.path.exists(retval), "Hard-coded path to file did not find expected file, '${top_srcdir}/samples/difference_test_0.xml'."
    return retval

def test_read_dfxml(difference_test_0_filepath : str) -> None:
    """
    This test confirms that the DFXML pip-managed packaging exposes the dfxml package and the objects.py module.
    """
    with open(difference_test_0_filepath, "rb") as fh:
        dfxml.read_dfxml(fh, callback=nop)


def test_objects_iterparse(difference_test_0_filepath : str) -> None:
    """
    This test confirms that the DFXML pip-managed packaging exposes the dfxml package's objects.py module.
    """
    for (event, obj) in dfxml.objects.iterparse(difference_test_0_filepath):
        pass

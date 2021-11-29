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

"""
Some of the fixtures in this test have a pattern to their names:

ddo_XY_from_Z

This pattern breaks down to:
* ddo: Differential DFXML in-memory Object (a type-hinting slug in the variable name)
* XY: A comparison of sample files /sample/difference_test_X.xml and ..._Y.xml.
* Z: How the in-memory object was loaded.
  - cli: Parsed from a command-line run of make_differential_dfxml.py
  - module: Created from a calling dfxml.bin.make_differential_dfxml.make_differential_dfxml().
  - serialization_1: A round-trip serialization from the "..._from_module" object, writing to a temporary file and calling Objects.parse().
  - serialization_2: A round-trip serialization from the "..._from_serialization" object, writing to a temporary file and calling Objects.parse().

The rounds of serialization are to affirm losslessness.
"""

__version__ = "0.2.2"

import argparse
import os
import logging
import sys
import tempfile
import typing

import pytest

import dfxml.bin.make_differential_dfxml
import dfxml.objects as Objects

_logger = logging.getLogger(os.path.basename(__file__))

@pytest.fixture
def srcdir() -> str:
    retval = os.path.dirname(__file__)
    return retval

@pytest.fixture
def top_srcdir(srcdir : str) -> str:
    retval = os.path.join(srcdir, "..", "..")
    assert os.path.exists(os.path.join(retval, "LICENSE.md")), "Hard-coded knowledge of file in top_srcdir is no longer correct."
    return retval

@pytest.fixture
def samples_srcdir(top_srcdir : str) -> str:
    return os.path.join(top_srcdir, "samples")

@pytest.fixture
def ddo_01_from_cli(srcdir : str) -> Objects.DFXMLObject:
    retval = Objects.parse(os.path.join(srcdir, "differential_dfxml_test_01.dfxml"))
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    return retval

@pytest.fixture
def ddo_01_from_module(samples_srcdir : str) -> Objects.DFXMLObject:
    retval = dfxml.bin.make_differential_dfxml.make_differential_dfxml(
      os.path.join(samples_srcdir, "difference_test_0.xml"),
      os.path.join(samples_srcdir, "difference_test_1.xml")
    )
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    return retval

@pytest.fixture
def ddo_01_from_serialization_1(ddo_01_from_module : Objects.DFXMLObject) -> Objects.DFXMLObject:
    filename = None
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".dfxml") as tmp_fh:
        filename = tmp_fh.name
        ddo_01_from_module.print_dfxml(output_fh=tmp_fh)
    retval = Objects.parse(filename)
    os.unlink(filename)
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    return retval

@pytest.fixture
def ddo_01_from_serialization_2(ddo_01_from_serialization_1 : Objects.DFXMLObject) -> Objects.DFXMLObject:
    filename = None
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".dfxml") as tmp_fh:
        filename = tmp_fh.name
        ddo_01_from_serialization_1.print_dfxml(output_fh=tmp_fh)
    retval = Objects.parse(filename)
    os.unlink(filename)
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    return retval

@pytest.fixture
def ddo_23_from_cli(srcdir : str) -> Objects.DFXMLObject:
    retval = Objects.parse(os.path.join(srcdir, "differential_dfxml_test_23.dfxml"))
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    assert len(retval.volumes) > 0, "Failed to record any Volumes."
    return retval

@pytest.fixture
def ddo_23_from_module(samples_srcdir : str) -> Objects.DFXMLObject:
    retval = dfxml.bin.make_differential_dfxml.make_differential_dfxml(
      os.path.join(samples_srcdir, "difference_test_2.xml"),
      os.path.join(samples_srcdir, "difference_test_3.xml")
    )
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    assert len(retval.volumes) > 0, "Failed to record any Volumes."
    return retval

@pytest.fixture
def ddo_23_from_serialization_1(ddo_23_from_module : Objects.DFXMLObject) -> typing.Generator[Objects.DFXMLObject, None, None]:
    filename = None
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".dfxml") as tmp_fh:
        filename = tmp_fh.name
        logging.debug("filename = %r." % filename)
        ddo_23_from_module.print_dfxml(output_fh=tmp_fh)
        logging.debug("os.stat(filename).st_size = %r." % os.stat(filename).st_size)
    logging.debug("Calling parse...")
    retval = Objects.parse(filename)
    logging.debug("Called parse.")
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    assert len(retval.volumes) > 0, "Failed to record any Volumes."
    yield retval
    #os.unlink(filename)

@pytest.fixture
def ddo_23_from_serialization_2(ddo_23_from_serialization_1 : Objects.DFXMLObject) -> typing.Generator[Objects.DFXMLObject, None, None]:
    filename = None
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".dfxml") as tmp_fh:
        filename = tmp_fh.name
        logging.debug("filename = %r." % filename)
        ddo_23_from_serialization_1.print_dfxml(output_fh=tmp_fh)
        logging.debug("os.stat(filename).st_size = %r." % os.stat(filename).st_size)
    retval = Objects.parse(filename)
    if not isinstance(retval, Objects.DFXMLObject):
        raise TypeError()
    assert len(retval.volumes) > 0, "Failed to record any Volumes."
    yield retval
    os.unlink(filename)

def _test_dfxml_object_01(
  dfxml_object : Objects.DFXMLObject
) -> None:
    expected_fileobject_diffs = {
      "i_am_new.txt": set([]),
      "i_will_be_deleted.txt": set([]),
      "i_will_be_modified.txt": set([
        "filesize",
        "mtime",
        "ctime",
        "atime",
        "data_brs",
        "md5",
        "sha1",
        "sha256"
      ]),
      "i_will_be_accessed.txt": set([
        "atime",
        "data_brs"
      ])
    }
    computed_fileobject_diffs = dict()

    for obj in dfxml_object:
        #_logger.debug(repr(o))
        if isinstance(obj, Objects.FileObject):
            if "deleted" in obj.annos:
                _name = obj.original_fileobject.filename
            else:
                _name = obj.filename

            computed_fileobject_diffs[_name] = obj.diffs

    assert expected_fileobject_diffs == computed_fileobject_diffs

def _test_dfxml_object_23(
  dfxml_object : Objects.DFXMLObject
) -> None:
    expected_partition_annos = {
      (1048576, "FAT16"): {"deleted"},
      (1073741824, "FAT32"): set(),
      (2147483648, "FAT32"): {"deleted"},
      (2147483648, "NTFS"): {"new"},
      (4294967296, "FAT32"): {"new"}
    }
    computed_partition_annos = dict()

    logging.debug("len(dfxml_object.volumes) = %d.", len(dfxml_object.volumes))
    logging.debug("len(dfxml_object.files) = %d.", len(dfxml_object.files))

    for obj in dfxml_object:
        if isinstance(obj, Objects.VolumeObject):
            computed_partition_annos[(obj.partition_offset, obj.ftype_str)] = obj.annos or set()
    assert expected_partition_annos == computed_partition_annos

def test_dfxml_object_01_from_cli(ddo_01_from_cli : Objects.DFXMLObject) -> None:
    _test_dfxml_object_01(ddo_01_from_cli)

def test_dfxml_object_01_from_module(ddo_01_from_module : Objects.DFXMLObject) -> None:
    _test_dfxml_object_01(ddo_01_from_module)

def test_dfxml_object_01_from_serialization_1(ddo_01_from_serialization_1 : Objects.DFXMLObject) -> None:
    _test_dfxml_object_01(ddo_01_from_serialization_1)

def test_dfxml_object_01_from_serialization_2(ddo_01_from_serialization_2 : Objects.DFXMLObject) -> None:
    _test_dfxml_object_01(ddo_01_from_serialization_2)

def test_dfxml_object_23_from_cli(ddo_23_from_cli : Objects.DFXMLObject) -> None:
    _test_dfxml_object_23(ddo_23_from_cli)

def test_dfxml_object_23_from_module(ddo_23_from_module : Objects.DFXMLObject) -> None:
    _test_dfxml_object_23(ddo_23_from_module)

def test_dfxml_object_23_from_serialization_1(ddo_23_from_serialization_1 : Objects.DFXMLObject) -> None:
    _test_dfxml_object_23(ddo_23_from_serialization_1)

def test_dfxml_object_23_from_serialization_2(ddo_23_from_serialization_2 : Objects.DFXMLObject) -> None:
    _test_dfxml_object_23(ddo_23_from_serialization_2)

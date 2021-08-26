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

import logging
import tempfile
import warnings

import pytest

import dfxml.objects as Objects

@pytest.mark.xfail(strict=True, reason="print_dfxml currently requires a text, not binary, writer.")
def test_serialization_to_binary_file() -> None:
    dobj = Objects.DFXMLObject()
    with tempfile.NamedTemporaryFile(mode="w+b", suffix=".dfxml") as temp_fh:
        logging.debug("temp_fh.name = %r.", temp_fh.name)
        dobj.print_dfxml(temp_fh)  # type: ignore

def test_serialization_to_text_file() -> None:
    dobj = Objects.DFXMLObject()
    with tempfile.NamedTemporaryFile(mode="w", suffix=".dfxml") as temp_fh:
        logging.debug("temp_fh.name = %r.", temp_fh.name)
        dobj.print_dfxml(temp_fh)

def test_warn_append_allocated_file_to_pobj() -> None:
    # Example source c/o:
    # https://docs.python.org/3/library/warnings.html#testing-warnings
    pobj = Objects.PartitionObject()
    fobj = Objects.FileObject()
    fobj.alloc = True
    assert fobj.is_allocated()
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        pobj.append(fobj)
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning) == 1

def test_warn_append_allocated_file_to_psobj() -> None:
    # Example source c/o:
    # https://docs.python.org/3/library/warnings.html#testing-warnings
    psobj = Objects.PartitionSystemObject()
    fobj = Objects.FileObject()
    fobj.alloc = True
    assert fobj.is_allocated()
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        psobj.append(fobj)
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning) == 1

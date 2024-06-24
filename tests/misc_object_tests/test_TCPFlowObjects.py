#!/usr/bin/env python

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
import os.path
import pathlib
import sys

import pytest

# TODO - It seems TCPFlowObjects might be better served from /dfxml instead of /dfxml/bin.
import dfxml.bin.TCPFlowObjects
import dfxml.objects as Objects


@pytest.fixture
def top_srcdir() -> pathlib.Path:
    srcdir = pathlib.Path(__file__).parent
    return srcdir / ".." / ".."


def test_TCPFlowObjects(top_srcdir: pathlib.Path) -> None:
    path_to_sample = top_srcdir / "samples" / "tcpflow_zip_generic_header.xml"
    assert (
        path_to_sample.exists()
    ), "Hard-coded path from test to sample is no longer valid."

    for event, obj in Objects.iterparse(str(path_to_sample)):
        if not isinstance(obj, Objects.FileObject):
            continue
        results = dfxml.bin.TCPFlowObjects.scanner_results_from_FileObject(obj)
        assert len(results) == 1
        # TODO - This could do with a better presentation in relation to the pytest framework.
        print("Flow name: %r." % obj.filename)
        for result in results:
            result.print_report()

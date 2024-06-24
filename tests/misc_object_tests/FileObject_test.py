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

__version__ = "0.1.1"

import logging
import os
import sys

import libtest

import dfxml.objects as Objects

_logger = logging.getLogger(os.path.basename(__file__))


def test_empty_file_object() -> None:
    dobj = Objects.DFXMLObject()
    fobj = Objects.FileObject()
    dobj.append(fobj)

    # Do file I/O round trip.
    (tmp_filename, dobj_reconst) = libtest.file_round_trip_dfxmlobject(dobj)
    try:
        fobj_reconst = dobj_reconst.files[0]
        assert fobj == fobj_reconst
    except:
        _logger.debug("tmp_filename = %r." % tmp_filename)
        raise
    os.remove(tmp_filename)


def test_blank_file_object_filename() -> None:
    dobj = Objects.DFXMLObject()
    fobj = Objects.FileObject()
    dobj.append(fobj)

    fobj.filename = ""

    # Do file I/O round trip.
    (tmp_filename, dobj_reconst) = libtest.file_round_trip_dfxmlobject(dobj)
    try:
        fobj_reconst = dobj_reconst.files[0]
        assert fobj == fobj_reconst
    except:
        _logger.debug("tmp_filename = %r." % tmp_filename)
        raise
    os.remove(tmp_filename)

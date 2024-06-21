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

import collections
import logging
import tempfile
import typing
import warnings

import pytest

import dfxml.objects as Objects


def test_AbstractHierarchyObject_append() -> None:
    """
    This test confirms expected append() behaviors, in lieu of static type checking enforcement.
    """

    hierarchy_object_classes : typing.List[type] = [
      Objects.DFXMLObject,
      Objects.RegXMLObject,
      Objects.DiskImageObject,
      Objects.PartitionSystemObject,
      Objects.PartitionObject,
      Objects.VolumeObject,
      Objects.HiveObject,
      Objects.FileObject,
      Objects.CellObject
    ]

    parent_object_classes : typing.List[type] = [
      Objects.DFXMLObject,
      Objects.RegXMLObject,
      Objects.DiskImageObject,
      Objects.PartitionSystemObject,
      Objects.PartitionObject,
      Objects.VolumeObject,
      Objects.HiveObject
    ]
    for parent_object_class in parent_object_classes:
        assert issubclass(parent_object_class, Objects.AbstractParentObject)

    matrix_expected : typing.Dict[type, typing.Set[type]] = {
      Objects.DFXMLObject: {
        Objects.DiskImageObject,
        Objects.PartitionSystemObject,
        Objects.PartitionObject,
        Objects.VolumeObject,
        Objects.FileObject
      },
      Objects.RegXMLObject: {
        Objects.HiveObject,
        Objects.CellObject
      },
      Objects.DiskImageObject: {
        Objects.PartitionSystemObject,
        Objects.VolumeObject,
        Objects.FileObject
      },
      Objects.PartitionSystemObject: {
        Objects.PartitionObject,
        Objects.FileObject
      },
      Objects.PartitionObject: {
        Objects.PartitionSystemObject,
        Objects.PartitionObject,
        Objects.VolumeObject,
        Objects.FileObject
      },
      Objects.VolumeObject: {
        Objects.DiskImageObject,
        Objects.VolumeObject,
        Objects.FileObject
      },
      Objects.HiveObject: {
        Objects.CellObject
      }
    }
    matrix_computed_PASS : typing.Dict[type, typing.Set[type]] = collections.defaultdict(set)
    matrix_computed_XFAIL : typing.Dict[type, typing.Set[type]] = collections.defaultdict(set)

    for parent_class in parent_object_classes:
        for child_class in hierarchy_object_classes:
            parent_object = parent_class()
            child_object = child_class()
            try:
                parent_object.append(child_object)
                matrix_computed_PASS[parent_class].add(child_class)
            except TypeError:
                matrix_computed_XFAIL[parent_class].add(child_class)
            except:
                raise
    logging.debug("matrix_computed_XFAIL:")
    logging.debug(matrix_computed_XFAIL)
    assert matrix_expected == matrix_computed_PASS

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

def test_instance_isolation_byte_runs() -> None:
    """
    This test confirms no unintentional confusion of instance variables and class variables when initializing any abstract base classes.

    Reference:
    * https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
    """
    fobj1 = Objects.FileObject()
    fobj2 = Objects.FileObject()

    br1 = Objects.ByteRun(img_offset=1, len=2)
    br2 = Objects.ByteRun(img_offset=3, len=4)

    fobj1.byte_runs = Objects.ByteRuns()
    fobj2.byte_runs = Objects.ByteRuns()

    fobj1.byte_runs.append(br1)
    fobj2.byte_runs.append(br2)

    assert len(fobj1.byte_runs) == 1
    assert len(fobj2.byte_runs) == 1

def test_instance_isolation_child_objects() -> None:
    """
    This test confirms no unintentional confusion of instance variables and class variables when initializing any abstract base classes.

    Reference:
    * https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
    """
    diobj1 = Objects.DiskImageObject()
    diobj2 = Objects.DiskImageObject()
    fsobj1 = Objects.VolumeObject()

    fobj1 = Objects.FileObject(filename="foo")
    fobj2 = Objects.FileObject(filename="bar")
    fobj3 = Objects.FileObject(filename="baz")
    fobj4 = Objects.FileObject(filename="boo")

    diobj1.append(fobj1)
    diobj2.append(fobj2)
    fsobj1.append(fobj3)
    fsobj1.append(fobj4)

    assert len(diobj1.child_objects) == 1
    assert len(diobj2.child_objects) == 1
    assert len(fsobj1.child_objects) == 2

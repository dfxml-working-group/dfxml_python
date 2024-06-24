#! /usr/bin/env python3
"""
This demo shows how to invoke Fiwalk as a subprocess, taking a disk image as
input. Fiwalk's dfxml XML output is sent to an in-memory buffer, which is then
written to an output file. Note that this may fail for very large disk images
if the required buffer size exceeds available RAM!
"""

import io
import sys

from dfxml import fiwalk


def writeDfxml(imageFile: str, outFile: str) -> None:
    """Generate filesystem metadata for disk image and and write resulting
    dfxml to file"""
    # Analyse image file
    with open(imageFile, "rb") as ifs:
        fwOutBuffer = fiwalk.fiwalk_xml_stream(imagefile=ifs)
        fwOut = fwOutBuffer.read()

    # Write dfxml to output file
    with io.open(outFile, "wb") as fOut:
        fOut.write(fwOut)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: {} <imageFile> <outFile>".format(sys.argv[0]))
        exit(1)
    imageFile = sys.argv[1]
    outFile = sys.argv[2]
    writeDfxml(imageFile, outFile)


if __name__ == "__main__":
    main()

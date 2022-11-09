import sys
import io
from dfxml import fiwalk

def writeDfxml(imageFile, outFile):
    """Generate filesystem metadata for disk image and and write resulting dfxml to file"""

    # Analyse image file
    with open(imageFile, "rb") as ifs:
        fwOutBuffer = fiwalk.fiwalk_xml_stream(imagefile=ifs)
        fwOut = fwOutBuffer.read()

    # Write dfxml to output file
    with io.open(outFile, "wb") as fOut:
        fOut.write(fwOut)

def main():
    if len(sys.argv) < 3:
        print("Usage: {} <imageFile> <outFile>".format(sys.argv[0]))
        exit(1)
    imageFile = sys.argv[1]
    outFile = sys.argv[2]
    writeDfxml(imageFile, outFile)

if __name__ == "__main__":
    main()
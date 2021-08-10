# Tools for working with DFXML-files

This directory contains scripts that can be run when the `dfxml` module is installed. Not all of these tools are added to the shell's `PATH` when the `dfxml` package is installed. Instead, these tools should be called in-place, e.g. with `python $PWD/make_differential_dfxml.py`.

## Overview about the provided tools

The following DFXML tools are provided in this directory:

| Script name              | Short description                                                                    |
|--------------------------+--------------------------------------------------------------------------------------|
| allocation_counter       | Produces a cross-tabulation of the allocation state of each file's inode and name.   |
| cat_fileobjects.py       | Prints a new DFXML of all fileobjects in an input DFXML file to stdout.              |
| cat_partitions.py        | Concatenates dfxml-files containing one partition each and prints result to stdout.  |
| deidentify_xml.py        | Removes PII from filenames in a DFXML file.                                          |
| dfxinfo.py               | Print a summary of a DFXML file - summary of all files, duplicate files, file types. |
| dfxml_gen.py             | generates DFXML. Based on the C generator.                                           |
| dfxml_html.py            | A collection of functions for generating HTML.                                       |
| Extractor.py             | Extracts files specified in a XML-file (or all) from an image to a target directory. |
| hash_sectors.py          | Outputs sector hashes for sectors with files matching a predicate.                   |
| iblkfind.py              | Outputs files, which are located in a given set of sectors.                          |
| icarvingtruth.py         | Finds the ground truth in a predefined series of disk images.                        |
| idifference.py           | Generates a report about what's different between two disk images.                   |
| igrep.py                 | Find files in image, which contain the given string.                                 |
| ihistogram.py            | Draws a quick histogram of the timestamps in an XML file.                            |
| imap.py                  | Map image files and try to find "missing" data by comparing with the other imgs.     |
| iredact.py               | Image redaction tool using rules described in the file.                              |
| ireport.py               | Generates stats from a DFXML file(s).                                                |
| iverify                  | Reads an XML file and image and verifies that the files are present.                 |
| rdifference.py           | Finds and reports differences in two Windows registry hive-files.                    |
| report_silent_changes.py | Takes a differentially-annotated DFXML file and outputs subtle and 'silent' changes. |


### Work needed

- dfxml_tool.py 
- idifference2.py
- iexport.py
- exp_slack.py
- validate_dfxml.py
- nsrl_rds.py
- corpus_sync.py


### Uncategorized

- make_differential_dfxml.py
- break_out_diffs_by_anno.py
- mem_info.py (no dependencies)

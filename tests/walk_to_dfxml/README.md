# `walk_to_dfxml`

*Source*: [`../../dfxml/bin/walk_to_dfxml.py`](../../dfxml/bin/walk_to_dfxml.py)

This command walks a directory, producing a `<fileobject>` for each encountered file and directory, and then recurses into each directory.  Output is sent to `stdout`.

File characteristics are drawn from:
* the path
* hashes of the file contents for regular files (i.e., not directories, not device files; also, not soft links)
* the `stat` structure for the file
* the referenced path (for soft links)

Any directory that can be navigated to can be characterized with this script.  This has been tested from the root directory of a (offline) Linux system's root-filesystem partition.  The tool can handle the `/dev` directory without issue.

This tool can be used to walk a network file system, such as a share.  However, be aware that if it is hashing, that would mean the tool is reading the file contents over the network.


## Usage

```bash
cd .../my_directory
walk_to_dfxml > /tmp/my_directory.dfxml
```

This will record all characteristics available for each file in and below `.../my_directory`.

Output should be captured outside of the present working directory, such as the parent directory.  Note that this command will include the hash of an empty file `output.dfxml`:

```bash
cd .../my_directory
walk_to_dfxml > output.dfxml
```

The `-i` (`--ignore`) flag will cause the named file characteristic to not be gathered into the output.  E.g. this command will not collect access time:

```bash
walk_to_dfxml -i atime > /tmp/walk.dfxml
```

(Testing: See the [`Makefile`](Makefile) recipe for `walk_ignore_genprops.dfxml`, which is tested in [`test_walk_to_dfxml.py`](test_walk_to_dfxml.py)'s function `test_walk_ignore_genprops`.)

The program can run without gathering any file hashes, by using the `--ignore-hashes` flag:

```bash
walk_to_dfxml --ignore-hashes > /tmp/walk.dfxml
```

(Testing: See the [`Makefile`](Makefile) recipe for `walk_ignore_hashes.dfxml`, which is tested in [`test_walk_to_dfxml.py`](test_walk_to_dfxml.py)'s function `test_walk_ignore_hashes`.)

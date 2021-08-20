# `make_differential_dfxml`

*Source*: [`../../bin/make_differential_dfxml.py`](../../bin/make_differential_dfxml.py)

This command takes as input two DFXML files, and outputs a DFXML document showing differential annotations.  Output is sent to `stdout`.

This tool was introduced in [Nelson et al., DFRWS 2014](https://doi.org/10.1016/j.diin.2014.05.004).


## Usage

```bash
make_differential_dfxml input_1.dfxml input_2.dfxml > deltas.dfxml
```

If one is using the [DFXML Objects module](../../dfxml/objects.py), the differentially-annotated DFXML can be analyzed by referring to each encountered `FileObject`'s property `.annos`.  See e.g. [`summarize_differential_dfxml.py`](../../dfxml/bin/summarize_differential_dfxml.py)'s output for [changes scoped to single file systems](differential_dfxml_test_by_path_01.txt), or [changes that cross file systems](differential_dfxml_test_by_times_23.txt).

#!/bin/sh
source ${TEST_DIR}/_pick_pythons.sh
"$PYTHON2" ${DEMO_DIR}/demo_registry_timeline.py ../tests/m57-charlie-2009-11-20-charlie-ntuser.dat.regxml
"$PYTHON3" ${DEMO_DIR}/demo_registry_timeline.py ../tests/m57-charlie-2009-11-20-charlie-ntuser.dat.regxml

#!/bin/sh

SCRIPT_DIR="$1"

# Guarantee sane defaults
if [ -z ${TEST_DIR} ];
then
    TEST_DIR="${SCRIPT_DIR}"
fi

if [ -z ${TOOL_DIR} ];
then
    TOOL_DIR="$(dirname ${SCRIPT_DIR})"
fi

if [ -z ${SAMPLE_DIR} ];
then
    SAMPLE_DIR="$(dirname $(dirname ${SCRIPT_DIR}))/samples"
fi

if [ -z ${PYTHONPATH} ];
then
    PYTHONPATH="$(dirname $(dirname ${SCRIPT_DIR}))"
    export PYTHONPATH;
fi

#!/bin/bash
sed -i '/index.rst/d' ./index.rst
find . -name "index.rst" | cut -d'/' -f2,3 | grep 202 | sort | sed 's/^/   /' >> ./index.rst

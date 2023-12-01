#!/bin/bash
rg ':outline:`([a-zA-Z ]+)`' --no-heading --only-matching --replace '$1' | cut -d':' -f2 | sed '/\.rst/d' | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g' | sort | uniq -c | sed '/contacts/d' | awk '{ print $2 "," $1}' | sed 's/_/ /g' > outlined.csv

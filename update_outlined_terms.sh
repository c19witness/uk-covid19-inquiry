#!/bin/bash
rg ':outline:`([a-zA-Z ]+)`' --no-heading --only-matching --replace '$1' | cut -d':' -f2 | sort | uniq | sed '/contacts/d' > outlined.csv

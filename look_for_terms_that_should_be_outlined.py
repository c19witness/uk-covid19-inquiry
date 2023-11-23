from pathlib import Path
import re

outlined_terms = []
outlined_terms_re = []

with open("outlined.csv") as file:
    outlined_terms = [line.rstrip() for line in file]
for outlined_term in outlined_terms:
    outlined_terms_re.append( { "term": outlined_term,
                              "term_re": re.compile(r'\b%s\b' % outlined_term, re.I),
                              "outlined_term_re": re.compile(r':outline:`%s`' % outlined_term, re.I) })

pathlist = Path(".").glob('20*module*/*.rst')
for path in pathlist:
     path_in_str = str(path)
     with open(path_in_str) as file:
         for num, line in enumerate(file, 1):
             for outlined_term_re in outlined_terms_re:
                 m = outlined_term_re['term_re'].search(line)
                 m2 = outlined_term_re['outlined_term_re'].search(line)
                 if m and not m2:
                     print(path_in_str + " " + str(num) + " `" + outlined_term_re['term'] + "`")
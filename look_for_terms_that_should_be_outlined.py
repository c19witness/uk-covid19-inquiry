from pathlib import Path
import re

outlined_terms = []
outlined_terms_re = []

with open("outlined.csv") as file:
    for line in file:
       outlined_terms.append(line.split(",")[0])
for outlined_term in outlined_terms:
    outlined_terms_re.append({ "term": outlined_term,
                              "term_re": re.compile(r'\b%s\b' % outlined_term, re.I),
                              "outlined_term_re": re.compile(r':outline:`%s`' % outlined_term, re.I),
                              "outlined_term_reB": re.compile(r':outline:`.*%s.*`' % outlined_term, re.I)
                              })

pathlist = Path(".").glob('20*module*/*.rst')
for path in pathlist:
     path_in_str = str(path)
     with open(path_in_str) as file:
         for num, line in enumerate(file, 1):
             if not line.startswith("   "):
                 for outlined_term_re in outlined_terms_re:
                     m = outlined_term_re['term_re'].search(line)
                     #if m is not None:
                         #print(str(m))
                     m2 = outlined_term_re['outlined_term_re'].search(line)
                     m2b = outlined_term_re['outlined_term_reB'].search(line)
                     if m and not m2 and not m2b:
                         x1 = m.start() -5
                         x2 = m.end() + 5
                         #print(str(x1))
                         print(path_in_str + " " + str(num) + " `" + outlined_term_re['term'] + "` " + line[x1:
                         x2])

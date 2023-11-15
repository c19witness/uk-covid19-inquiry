import glob, os, re
os.chdir("./")
dateRegex = re.compile(".*(20\d{2})-(\d{2})-(\d{2})\.rst")

moreThanNine = ['2022-10-04', '2023-03-01', '2023-09-13', '2022-10-31', '2023-10-04', '2023-06-06', '2023-06-13', '2023-09-27', '2023-02-28', '2023-09-27']

for file in glob.glob("**/*.rst"):
    fileIx = 1
    #print(file)
    if not dateRegex.match(file):
        continue
    m = file.split("/")[0]
    d = file.split("/")[1].replace(".rst","")
    file1 = open(file, 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    previousLine = ""
    opFile = None
    preamble=[]
    for line in Lines:
        count += 1
        if (line.startswith("----")):
            if opFile is not None:
                opFile.close()
            d___m = d + "_" + m
            os.makedirs(d___m, exist_ok=True)
            ixFile = open(d___m + "/index.rst", 'w')
            ixFile.writelines(d + " " + m + "\n" + ("=" * len(d___m)) +"""

.. toctree::
   :glob:

   ./*
""")
            ixFile.close()
            fName = previousLine.strip().replace("Submissions on Behalf of the ", "SOBO: ").replace("Submissions on Behalf of ", "SOBO ")
            fName = fName.replace("Lady Hallett", "Lady Heather Hallett").replace("Dame Patel", "Dame Priti Patel").replace("Dame Harries", "Dame Jenny Harries").replace("Dame Davies", "Dame Sally Davies")
            #print("fName=" + fName)
            opFileName = d___m + "/" + ("0" if d in moreThanNine and fileIx < 10  else "") + str(fileIx) + "_" + fName.replace(" ", "_").replace(",", "_") + ".rst"
            #print(opFileName)
            if os.path.isfile(opFileName):
                break
            opFile = open(opFileName, 'w')
            opFile.writelines(preamble)
            preamble=[]
            opFile.write(str(fileIx) + ". " + previousLine)
            fileIx += 1
        # print("Line{}: {}".format(count, line.strip()))
        try:
            if not Lines[count].startswith("----"):
                if opFile is None:
                    if not line.startswith("======"):
                        preamble.append(line)
                else:
                    if not line.startswith("^^^^^^^^^^^"):
                        if line.startswith("-----"):
                            extra = 3 if d in moreThanNine else 2
                            opFile.write("=" * (len(previousLine)+extra) + "\n")
                        else:
                            opFile.write(line)
        except IndexError:
            opFile.write(line)
        previousLine = line
    if opFile is not None:
        opFile.close()
    try:
        os.remove(m + "/index.rst", )
    except FileNotFoundError:
        pass

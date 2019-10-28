#!/usr/bin/env python

import os,csv,gzip

# write a script to create new file called closed.txt

outfile="closed.txt"
# on the HPCC cluster you can use the file
file="/bigdata/gen220/shared/simple/title.basics.tsv.gz"
# or if you run this on your own computer use this
#file="title.basics.tsv.gz"


if not os.path.exists(file):
    os.system("curl -O https://datasets.imdbws.com/title.akas.tsv.gz")

with gzip.open("/rhome/schan131/2019_hw2_schan131/title.basics.tsv.gz", "rt", encoding="utf-8") as file:
   reader = csv.reader(file, delimiter="\t")
   rownum = 0
   for row in reader:
      location = row[3]
      if location.lower().find("door") != -1:
         rownum = rownum + 1
   print("Answer 1 is", rownum)

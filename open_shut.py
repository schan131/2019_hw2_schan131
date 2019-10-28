#!/usr/bin/env python
import os,csv,gzip,re,sys

# write a script to create new file called closed.txt

#if not os.path.exists(file):
#    os.system("curl -O https://datasets.imdbws.com/title.akas.tsv.gz")

 #create output file and add contents
sys.stdout = open("closed.txt", "w")

#title.basics.tsv.gz in bigdata/gen220/shared/simple folder seems disrupted -> use a file in my folder.
with gzip.open("/rhome/schan131/2019_hw2_schan131/title.basics.tsv.gz", "rt", encoding="utf-8") as file:
  reader = csv.reader(file, delimiter="\t") #open tsv file

  everydoor = [] #Q1 
  Onlydoor = [] #Q2
  withOpen = [] #Q3a
  withClosed = [] #Q3b

  for row in reader:
    location = row[3] #only use titles in column 4 to avoid count the same things multiple times
    Option1 = re.search(r"[dD]oor", location)
    Option2 = re.search(r"(^|\s)[dD]oor(\s|$)", location)
    Option3a = re.search(r"(^|\s)Open(\s|$)", location)
    Option3b = re.search(r"(^|\s)Closed(\s|$)", location)
    if Option1:
      everydoor.append(location)
    if Option2:
      Onlydoor.append(location)
    if Option3a:
      withOpen.append(location)
    if Option3b:
      withClosed.append(location)
      
  print("Answer 1 is", len(everydoor), "\n", 
 "Answer 2 is", len(Onlydoor), "\n", 
 "Answer 3a: the number of movies with 'Open' is", len(withOpen), "\n", 
 "Answer 3b: the number of movies with 'Closed' is", len(withOpen), "\n")    


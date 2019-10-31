#!/usr/bin/env python
import os,gzip,itertools, sys, re, urllib.request, urllib.parse, urllib.error, csv, Bio

# this is a python script template
# this next line will download the file using curl

#Part 1. Download the files

url1 = "ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"

url2 = "ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

#urllib.request.urlretrieve(url1, "/rhome/schan131/2019_hw2_schan131/Ecoli.gff3.gz")
#urllib.request.urlretrieve(url2, "/rhome/schan131/2019_hw2_schan131/Ecoli.fa.gz")

#part 2.
genenum = []
with gzip.open("/rhome/schan131/2019_hw2_schan131/Ecoli.gff3.gz", "rt", encoding="utf-8") as gff:
  reader = csv.reader(gff, delimiter="\t")
  for row in reader:
    linestrip = row.decode("utf-8").strip()
    genesearch = re.search(r"\tgene\t", linestrip)
    if genesearch:
      genesearch.append[reader]
      print(reader, len(genesearch))

#gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
#fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"


# this is code which will parse FASTA files
# define what a header looks like in FASTA format



#def isheader(line):
#    return line[0] == '>'

#def aspairs(f):
#    seq_id = ''
#    sequence = ''
#    for header,group in itertools.groupby(f, isheader):
#        if header:
#            line = next(group)
#            seq_id = line[1:].split()[0]
#        else:
#            sequence = ''.join(line.strip() for line in group)
#            yield seq_id, sequence



#if not os.path.exists(gff):
#    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz")

#if not os.path.exists(fasta):
#    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
    
#with gzip.open(gff,"r") as fh:
    # now add code to process this
    # data such as
    # for line in fh:

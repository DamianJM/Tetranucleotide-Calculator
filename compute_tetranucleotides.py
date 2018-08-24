#Tetranucleotide Calculator
#Script to compute tetranucleotide frequencies with overlapping strings

import itertools
import argparse, sys
from string import maketrans

trantab = maketrans("ATGC", "TACG")

#Function for counting

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

TETRA = []

for i in itertools.imap(''.join, itertools.product('ATGC', repeat=4)):
	TETRA.append(i)


sequences = []

try:
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Ccalculate Tetranucleotide frequencies of Sequence File",
                type=str)
	args = parser.parse_args()

	filename = args.file

except:
	e = sys.exc_info()[0]
	print e



with open(filename, 'r') as final:
    sequence = ''
    for line in final:
        if line.startswith('>'):
            sequences.append(sequence)
            sequence = ''
        else:
            sequence += line.strip()

orderedNames = TETRA
count = 0
total = len(sequences)
temp = []
rc = ""	
output = open("tetranucleotides.csv", "w")

for i in TETRA:
	output.write(i)
	output.write(",")
output.write("\n")

while count < len(sequences):
	for i in sequences:
		for j in TETRA:
			rc = j.translate(trantab)
			rc = rc[::-1]
			temp.append(occurrences(i,j) + occurrences(i, rc))
		for k in temp:
			output.write(str(k))
			output.write(",")
		output.write("\n")
		temp = []
		rc = ""
		count += 1
		counttotal = (count/total)*100
		if 24 <= counttotal <=26:
			print "Computation 25% complete\n"
		elif 49 <= counttotal <= 51:
			print "Computation 50% complete\n"
		elif 74 <= counttotal <= 76:
			print "Computation 75% complete\n"
		
print "Computation 100% Complete\n"
print "Thanks for using Tetranucleotide Calculator"



output.close()






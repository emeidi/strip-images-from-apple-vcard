#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re
import argparse

def d(msg):
    if verbose == False:
        return

    print(msg)

parser = argparse.ArgumentParser(description='Strips images from an Apple AddressBook.app VCF export for easier uploading to contact directories (e.g. Google Contacts)')

parser.add_argument('--inputfile', metavar='STRING', help='The input file (.vcf)', required=True)
parser.add_argument('--outputfile', metavar='STRING', help='The output file', required=False)
parser.add_argument('--verbose', help='Print debug information', action="store_true", required=False)

args = parser.parse_args()

# Logic to handle command line arguments
# ======================================================================
if args.verbose:
    verbose = True
    d('Enabling command line verbosity as requested by command line')
else:
    verbose = False

filenameInput = args.inputfile
d('Setting filenameInput to "' + filenameInput + '"')

if args.outputfile:
    filenameOutput = args.outputfile
else:
    filenameOutput = re.sub("(\.[a-z]+)$", ".clean\\1", filenameInput)

d('Setting filenameOutput to "' + filenameOutput + '"')

# Check input and output files
#  ======================================================================
if not os.path.exists(filenameInput):
	print("ERROR: File '" + filenameInput + "' not found. Cannot continue.")
	sys.exit(1)

if os.path.exists(filenameOutput):
	print("ERROR: File '" + filenameOutput + "' already exists. Please rename or delete, then re-run this script.")
	sys.exit(1)

# Convert/clean
#  ======================================================================
d("Reading '" + filenameInput + "'")

infile = open(filenameInput)

clean = ""
for line in infile:
	if re.match('PHOTO',line):
		d("Found line starting with PHOTO. Skipping.")
		continue;

	if re.match('\s',line):
		d("Found line starting with space. Skipping.")
		continue;

	clean += line

d("Writing " + filenameOutput)

outfile = open(filenameOutput,"w")
outfile.write(clean)

d("Done.")

sys.exit(0)

import sys
import os
import re

def checkArgs():
	numArgs = len(sys.argv)
	if (numArgs < 3):
		return False
	return True

def debugMsg(msg,type='Info'):
	print(type.upper() + ":")
	print("    " + msg)
	print("")
	
# ===================================================================
# CLI

if checkArgs():
	# Arguments provided on command line - must be a pro!
	filenameInput = sys.argv[1]
	filenameOutput = sys.argv[2]
else:
	filenameInput = raw_input("Input file (.vcf): ")
	filenameOutput = raw_input("Output file (.vcf): ")
	print("")

if not os.path.exists(filenameInput):
	debugMsg("File '" + filenameInput + "' not found",'Error')
	sys.exit(1)

if os.path.exists(filenameOutput):
	answer = raw_input(filenameOutput + " already exists. Overwrite? (y/n)")
	if answer != 'y':
		debugMsg("Please rerun this tool and specify an output filename",'Error')
		sys.exit(1)
	else:
		print("")
	
debugMsg("Reading '" + filenameInput + "'",'Info')

infile = open(filenameInput)

clean = ""
for line in infile:
	if re.match('PHOTO',line):
		debugMsg("Found line starting with PHOTO. Skipping.")
		continue;
	
	if re.match('\s',line):
		debugMsg("Found line starting with space. Skipping.")
		continue;
	
	clean += line

debugMsg("Writing " + filenameOutput)
	
outfile = open(filenameOutput,"w")
outfile.write(clean)

debugMsg("Done.")

sys.exit(0)

# -------------------------------------------------------------------
# The following (simpler) approach was found not to work on a 10+ MB
# .vcf file produced by Apple's Addressbook 
# -------------------------------------------------------------------
raw = infile.read()

debugMsg("File read (" + str(len(raw)) + " chars). Processing.",'Info')

# re.S = . includes \n, re.M = multiline (allows to use ^ as beginning of line)
pattern = re.compile('\nPHOTO;.*?=\n',re.S + re.M)
clean = re.sub(pattern,'\n',raw)

debugMsg("Length before: " + str(len(raw)) + " Length after: " + str(len(clean)))

debugMsg("Writing " + filenameOutput)
outfile = open(filenameOutput,"w")
outfile.write(clean)

debugMsg("Done.")

sys.exit(0)
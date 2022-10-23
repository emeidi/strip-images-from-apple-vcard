Usage
=====
`python3 strip-images-from-apple-vcard.py --inputfile Kontakte.vcf`

Purpose
=======
Strips pictures from vCards .vcf exports from Apple's AddressBook to be imported into other VCF capable tools (e.g. RoundCube Webmail).

I was able to reduce a complete backup of my Apple AddressBook in VCF format weighing 11 MB to 638 KB.

Step by step
============

AddressBook
-----------
1. Open AddressBook
1. Select all address book entries (Cmd-A)
1. AdressBook
1. Export...
1. Export vCard...
1. Save

Alternatively, you just can drag & drop in newer macOSes.

Shell
-----
1. Switch to directory containing this script and the vCards.vcf file
1. `python strip-images-from-apple-vcard.py --inputfile Kontakte.vcf`

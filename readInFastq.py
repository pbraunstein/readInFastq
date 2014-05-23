#!/usr/bin/env python

# readInFastq.py
# Author: Philip Braunstein
#
# Date Created: May 23, 2014
# Last Modified: May 23, 2014
#
# Reads in a Fastq file into a list of lists where each sublist
# has the structure [ID, SEQUENCE, STRANDEDNESS, QUALITY SCORE].
#

from sys import argv  # Access to arguments passed on command line
from sys import exit  # Ability to exit from programs

# CONSTANTS
EXTENSION = "fastq"
FASTQ_LINES = 4

def main():
        checkArgs()

        sequences = readInFastq()

#        print sequences

        print len(sequences)

        exit(0)

# Verifies that the scripts was invoked in a valid way
def checkArgs():
        # If there are not the correct number of arguments, exit
        if len(argv) != 2:
                print "ERROR: Incorrect number of arguments"
                usage()


        # If it is not the right file type exit
        if argv[1].split(".")[-1] != EXTENSION:
                print "ERROR: Must provide", EXTENSION, "file format"
                usage()


# Prints how to run this program from the command line
# and exits non-zero
def usage():
        print "USAGE:", argv[0], "[INPUT_FASTA_FILE]"
        exit(1)


# Reads in FASTQ file and returns list of lists of the form
# [[ID, SEQUENCE, STRANDEDNESS, QUALITY SCORE]]
def readInFastq():
        toReturn = []
        read = None  # Signify read not yet assigned
        count = 0

        with open(argv[1], 'r') as filer:
                for line in filer:
                        line = line.strip()  # Remove white space
                        if count == 0 or count == FASTQ_LINES:
                                if read != None:
                                        toReturn.append(read)

                                read = [line]

                                count = 1  # Reset counter

                        else:
                                read.append(line)
                                count += 1


                toReturn.append(read)  # Border case: one remaining sequence


        return toReturn
                        



if __name__ == '__main__':
        main()

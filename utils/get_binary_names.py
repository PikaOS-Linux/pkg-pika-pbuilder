#!/usr/bin/python3

import sys

import apt_pkg

import apt

# load the apt cache
cache = apt.Cache()

# base package that we use for binary calculation and output file path
if len(sys.argv) < 3:
    print("Usage: get_binary_names.py [Source package name] [PATH TO OUTPUT FILE]")
    sys.exit(1)
pkg = base = sys.argv[1]
output_file = sys.argv[2]

# reload source records
srcrecords = apt_pkg.SourceRecords()
# load source record for argument package
srcrec = srcrecords.lookup(base)
# if source load was successful
if srcrec:
    # then
    # read source binary record
    bins = srcrecords.binaries
    # open output file from argument
    f = open(output_file, "a")
    # write every binary package name with a space at the end
    for bin in bins:
        f.write(f"{bin} ")
else:
    # else
    # print an error and exit with status 5
    print("%s Couldn't be find in apt source package records" % base)
    sys.exit(5)
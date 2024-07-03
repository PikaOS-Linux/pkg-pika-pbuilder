#!/usr/bin/python3
# this is a example how to access the build dependencies of a package

import sys

import apt_pkg

import apt

# load the apt cache
cache = apt.Cache()

# base package that we use for build-depends calculation and output file path
if len(sys.argv) < 3:
    print("Usage: get_full_builddep_tree.py [Package name] [PATH TO OUTPUT FILE]")
    sys.exit(1)
try:
    pkg = base = cache[sys.argv[1]]
except KeyError:
    print("No package %s found" % sys.argv[1])
    sys.exit(1)
output_file = sys.argv[2]

# build-dep source_names blacklist
build_depends_blacklist = []
# build-dep names blacklist
build_depends_pkg_names_blacklist = []
# empty array to store build dependencies
all_build_depends = []
# empty array to make sure not to duplicate
already_proccessed = []
# empty array to make sure not to waste resources converting already scanned pkg_names
already_proccessed_pkg_names = []

# get the build depends for the package itself
# get source name of argument package from cache
srcpkg_name = base.candidate.source_name
if not srcpkg_name:
    print("Can't find source package for '%s'" % pkg.name)
# reload source records
srcrecords = apt_pkg.SourceRecords()
# load source record for argument package
srcrec = srcrecords.lookup(srcpkg_name)
if srcrec:
    # get build_depends as a dict
    bd_dict = srcrecords.build_depends
    try: 
        # load key "Build-Depends" from bd_dict 
        bd = bd_dict["Build-Depends"]
        for b in bd:
            for package in b:
                # parse every key into the needed 3 values
                name, version, comparator = package
                try:
                    # if build-dep name isn't already processed or blacklisted
                    if not name in already_proccessed_pkg_names and not name in build_depends_pkg_names_blacklist: 
                        # load build-dep from cache
                        apt_package = cache[name]
                        # get build-dep source name
                        pkg_source_name = apt_package.candidate.source_name
                        # if source package isn't blacklisted or already processed
                        if not pkg_source_name in already_proccessed and not pkg_source_name in build_depends_blacklist:
                            # then
                            # add the source package to the build_depends array
                            all_build_depends.append(pkg_source_name)
                            # and declare it already proccessed
                            already_proccessed.append(pkg_source_name)
                except:
                    continue
    except: 
        pass
    try:
        # load key "Build-Depends-Indep" from bd_dict 
        bd_indep = bd_dict["Build-Depends-Indep"]
        for b in bd_indep:
                # parse every key into the needed 3 values
                name, version, comparator = package
                try:
                    # if build-dep name isn't already processed or blacklisted
                    if not name in already_proccessed_pkg_names and not name in build_depends_pkg_names_blacklist: 
                        # load build-dep from cache
                        apt_package = cache[name]
                        # get build-dep source name
                        pkg_source_name = apt_package.candidate.source_name
                        # if source package isn't blacklisted or already processed
                        if not pkg_source_name in already_proccessed and not pkg_source_name in build_depends_blacklist:
                            # then
                            # add the source package to the build_depends array
                            all_build_depends.append(pkg_source_name)
                            # and declare it already proccessed
                            already_proccessed.append(pkg_source_name)
                except:
                    continue
    except:
        pass

for bd in all_build_depends:
    # parent build-dep position in array
    bd_position = all_build_depends.index(bd)
    # reload source records
    srcrecords = apt_pkg.SourceRecords()
    # load source record for argument package
    srcrec = srcrecords.lookup(bd)
    if srcrec:
        # get build_depends as a dict
        bd_dict = srcrecords.build_depends
        try: 
            # load key "Build-Depends" from bd_dict 
            bd = bd_dict["Build-Depends"]
            for b in bd:
                for package in b:
                    # parse every key into the needed 3 values
                    name, version, comparator = package
                    try:
                        # if build-dep name isn't already processed or blacklisted
                        if not name in already_proccessed_pkg_names and not name in build_depends_pkg_names_blacklist: 
                            # load build-dep from cache
                            apt_package = cache[name]
                            # get build-dep source name
                            pkg_source_name = apt_package.candidate.source_name
                            # if source package isn't blacklisted or already processed
                            if not pkg_source_name in already_proccessed and not pkg_source_name in build_depends_blacklist:
                                # then
                                # add the source package to the build_depends array after it's parent position
                                all_build_depends.insert(bd_position, pkg_source_name)
                                # and declare it already proccessed
                                already_proccessed.append(pkg_source_name)
                    except:
                        continue
        except:
            continue
        try: 
            # load key "Build-Depends-Indep" from bd_dict 
            bd_indep = bd_dict["Build-Depends-Indep"]
            for b in bd_indep:
                for package in b:
                    # parse every key into the needed 3 values
                    name, version, comparator = package
                    try:
                        # if build-dep name isn't already processed or blacklisted
                        if not name in already_proccessed_pkg_names and not name in build_depends_pkg_names_blacklist: 
                            # load build-dep from cache
                            apt_package = cache[name]
                            # get build-dep source name
                            pkg_source_name = apt_package.candidate.source_name
                            # if source package isn't blacklisted or already processed
                            if not pkg_source_name in already_proccessed and not pkg_source_name in build_depends_blacklist:
                                # then
                                # add the source package to the build_depends array after it's parent position
                                all_build_depends.insert(bd_position, pkg_source_name)
                                # and declare it already proccessed
                                already_proccessed.append(pkg_source_name)
                    except:
                        continue
        except:
            continue

# write result to output file
f = open(output_file, "a")
for line in all_build_depends:
    f.write(f"{line}\n")
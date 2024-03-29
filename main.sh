#! /bin/bash

DEBIAN_FRONTEND=noninteractive

# Clone Upstream
cp -rvf ./debian ./pika-pbuilder/
cd ./pika-pbuilder/

# Get build deps
apt-get build-dep ./ -y

# Build package
dpkg-buildpackage --no-sign

# Move the debs to output
cd ../
mkdir -p ./output
mv ./*.deb ./output/

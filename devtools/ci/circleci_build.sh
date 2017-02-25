#!/bin/sh

source devtools/ci/load_functions.sh
# source code
download_ambertools

amber_source=$HOME/ambertools-test/amber17

# binary
fn='AT.binary.tar.bz2'
url='https://90-81537431-gh.circle-artifacts.com/0/tmp/circle-artifacts.mHmoQJ3/ambertools-build/amber-conda-bld/non-conda-install/linux-64.ambertools-17.0.0-py27_0.25Feb17.H0203.tar.bz2'
wget $url -O $fn
mkdir TEST
cd TEST
tar -xf ../$fn
cd amber17
source amber.sh
mkdir test
cd test
lndir $amber_source/test
cd $AMBERHOME/AmberTools
mkdir test
cd test
lndir $amber_source/AmberTools/test
cd $AMBERHOME
touch config.h
mkdir $AMBERHOME/AmberTools/src
touch $AMBERHOME/AmberTools/src/config.h
INSTALLTYPE make test

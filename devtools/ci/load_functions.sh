#!/bin/sh

url="http://ambermd.org/downloads/ambertools-dev/AmberTools17.cmake.tar.gz"
tarfile=`python -c "url='$url'; print(url.split('/')[-1])"`
version=`python -c "tarfile='$tarfile'; print(tarfile.split('.')[0][-2:])"`

function download_ambertools(){
    wget $url -O $tarfile
    tar -xf $tarfile
}

function install_ambertools_travis(){
    set -ex
    # This AmberTools version is not an official release. It is meant for testing.
    # DO NOT USE IT PLEASE.
    osname=`python -c 'import sys; print(sys.platform)'`
    mkdir $HOME/TMP
    cd amber$version
    mkdir build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX=$HOME/TMP ..
    make install -j2
}

function install_ambertools_circleci(){
    echo "None"
    # mkdir $HOME/TMP
    # cd $HOME/TMP
    # python $HOME/ambertools-test/amber$version/AmberTools/src/conda-recipe/scripts/build_all.py --exclude-osx --py 2.7 --sudo
    # python $HOME/ambertools-test/amber$version/AmberTools/src/conda-recipe/scripts/build_all.py --exclude-osx --py 2.7 --sudo -t ambermini
}

function run_tests(){
    set -ex
    source $HOME/TMP/amber.sh
}

[![Build Status](https://travis-ci.org/Amber-MD/ambertools-test.svg?branch=nightly)](https://travis-ci.org/Amber-MD/ambertools-test)
[![CircleCI](https://circleci.com/gh/Amber-MD/ambertools-test/tree/nightly.svg?style=svg)](https://circleci.com/gh/Amber-MD/ambertools-test/tree/nightly)

# ambertools-test
For testing AmberTools

# How to run your own change?
- fork this repo to your own github account
- make your own AmberTools17.{date}.tar.gz file
```bash
    # do some code changes, then
    cd $AMBERHOME
    sh ./mkrelease_at # about 5 minutes
    # then upload to somewhere so travis or circleci can download it (we give instruction for them to do that).
```
- update AmberTools17 url in [devtools/ci/load_functions.sh](devtools/ci/load_functions.sh)
- (optional) update your own test in [run_tests function](devtools/ci/load_functions.sh)
- (optional) update [.travis file](https://github.com/Amber-MD/ambertools-test/blob/nightly/.travis.yml#L3) to add more builds
- make a pull request to this repo or [activate your travis account](https://travis-ci.org/getting_started). The pull request or any new commit will trigger [travis](https://travis-ci.org/Amber-MD/ambertools-test) and [circleci](https://circleci.com/gh/Amber-MD/ambertools-test) to build/test AmberTools based on [our given recipe](https://github.com/Amber-MD/ambertools-test/blob/nightly/.travis.yml)

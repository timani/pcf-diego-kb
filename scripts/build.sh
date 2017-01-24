#!/bin/bash
# https://github.com/travis-ci/travis-ci/issues/879#issuecomment-12710282

if [[ $TRAVIS_BRANCH == '1.0.-stable' ]]
  cd test/dummy
  rake db:schema:load
else
  cd spec/dummy
  rake db:schema:load
fi

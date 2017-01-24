#!/bin/bash
# https://github.com/travis-ci/travis-ci/issues/879#issuecomment-12710282

# Run the default tests on the Article
python scripts/test.py

# Deploy the Article on when it is on master and PR is from develop
# Only admins can deploy to master
if [[ $TRAVIS_BRANCH == 'master' && $TRAVIS_PULL_REQUEST_BRANCH == 'develop]]
  python scripts/deploy.py
fi

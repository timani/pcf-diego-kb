#!/bin/bash
set -ev

python scripts/frontmatter-test.py

if [ "${TRAVIS_PULL_REQUEST}" = "true" ] && [ "$TRAVIS_BRANCH" == "prod" ]; then
	python scripts/deploy.py
fi


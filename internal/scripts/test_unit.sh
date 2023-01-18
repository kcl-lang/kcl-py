#!/bin/sh

# ---------------------------------------------------------------------------------
# Show the unit test coverage report
# For more info, see the
# [Python Coverage Documents](https://coverage.readthedocs.io/en/latest/)
# TODO: Using more mature tools and practices. e.g.
# https://github.com/CleanCut/green
# https://github.com/oldani/HtmlTestRunner
# ---------------------------------------------------------------------------------

src="$(realpath $(dirname $0))/../../"
unittest_path=$src/test/test_units/
package_name=kclvm
xunit_file=TEST-kclvm.xml
# Install the dependency
python3 -m pip install --upgrade pip
python3 -m pip install pytest pytest-xdist
# Unit test
cd $unittest_path
python3 -m pytest -vv

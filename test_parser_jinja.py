import os
import glob
import datetime

from robot.api import TestData

from templates import JINJA_TEMPLATE

from jinja2 import Template

IMAGEPATH = '/home/fernando/git/testparser/images/Logo-with-strapline_Black-400.png'
TESTDIR = '/home/fernando/git/qa/FeatureTest/suites/regression/'

# TESTDIR = '/home/paolo/qa/FeatureTest/suites/regression/'

FILES_TYPE = '*.txt'


def find_test_files():
    return glob.glob(TESTDIR+FILES_TYPE)


if __name__ == '__main__':
    file_locations = find_test_files()
    test_file_locations = [loc for loc in file_locations if loc.replace(TESTDIR, '')[0].isdigit() or loc.replace(TESTDIR,'')[0] == 'W']
    test_file_locations = sorted(test_file_locations)
    test_suites = []
    last_parse = []
    last_parse.append(datetime.datetime.now().strftime("%a, %d %b %Y"))
    last_parse.append(datetime.datetime.now().strftime("%-I:%M:%S %p"))
    for file_location in test_file_locations:
        suite_location = os.path.abspath(file_location)
        test_file = TestData(source=suite_location)
        test_suites.append(test_file)

    template = Template(JINJA_TEMPLATE)

    output = template.render(test_suites=test_suites, image_path=IMAGEPATH, last_execution=last_parse)

    with open('output.html', 'w') as html_output:
        html_output.write(output.encode('UTF-8'))

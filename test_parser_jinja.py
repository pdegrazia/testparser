import os
import glob

from robot.api import TestData

from templates import JINJA_TEMPLATE

from jinja2 import Template


def find_test_files():
    return glob.glob('./test_files/*.txt')


if __name__ =='__main__':
    file_locations = find_test_files()

    test_suites = []
    for file_location in file_locations:
        suite_location = os.path.abspath(file_location)
        test_file = TestData(source=suite_location)
        test_suites.append(test_file)

    template = Template(JINJA_TEMPLATE)
    output = template.render(test_suites=test_suites)
    with open('output.html', 'w') as html_output:
        html_output.write(output)

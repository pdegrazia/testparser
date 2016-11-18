import os
import glob

from robot.api import TestData

from templates import *


class OutputFile:
    def __init__(self):
        self.output = ''

    def write_header(self):
        self.output += HEAD

    def write(self, tag):
        self.output += tag

    def write_to_file(self):
        with open('output.html', 'w') as html_output:
            html_output.write(self.output)

    def write_list_item(self, item):
        self.output += '<li>' + item

    def write_test_steps(self, test_steps):
        for step in test.steps:
            self.output += '<li>' + step.keyword + '</li>'

    def open_ordered_list(self):
        self.output += '<ol>'

    def close_ordered_list(self):
        self.output += '</ol>'

    def open_unordered_list(self):
        self.output += '<ul>'

    def close_unordered_list(self):
        self.output += '</ul>'

    def close_list_item(self):
        self.output += '</li>'

    def write_footer(self):
        self.output += FOOTER


def find_test_files():
    return glob.glob('./test_files/*.txt')


if __name__ =='__main__':
    file_locations = find_test_files()

    output_file = OutputFile()

    output_file.write(HEAD)
    output_file.open_unordered_list()

    for file_location in file_locations:
        suite_location = os.path.abspath(file_location)
        test_file = TestData(source=suite_location)
        print 'Suite:', test_file.name

        output_file.write_list_item(test_file.name)
        output_file.open_unordered_list()

        for test in test_file.testcase_table:
            output_file.write_list_item(test.name)
            output_file.open_ordered_list()
            output_file.write_test_steps(test.steps)
            output_file.close_ordered_list()
            output_file.close_list_item()
        output_file.close_ordered_list()
        output_file.close_unordered_list()
    output_file.close_unordered_list()
    output_file.write_footer()
    output_file.write_to_file()

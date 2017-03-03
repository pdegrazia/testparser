import os
import sys

from robot.api import TestData

conversion_table = {'TestCaseFileSettingTable':'settings',
                    'VariableTable':'variables',
                    'TestCaseTable':'test_cases',
                    'KeywordTable':'keywords',
                    }


class TestSuite:
    def __init__(self, filename):
        self.filename = filename
        self.real_file = open(self.filename, 'r').read()
        self.suite = TestData(source=filename)

    def check_tags(self):
        if len(self.suite.setting_table.force_tags.as_list()) <= 1:
            print 'No tags!'
        else:
            print 'The following tags are present: {}'.format(self.suite.setting_table.force_tags.as_list()[1:])

    def check_unusued_variables(self):
        for variable in self.suite.variable_table.variables:
            if self.real_file.count(variable.name)<2:
                print '*'*40
                print 'Variable %s not used!' % variable.name
                print '*' * 40

    def check_unused_keywords(self):
        for keyword in self.suite.keyword_table.keywords:
            if self.real_file.count(keyword.name) < 2:
                print 'KW \'%s\' never used!' % keyword.name
            else:
                print 'Keyword reused'


if __name__ =='__main__':
    filename = sys.argv[-1]
    suite_location = os.path.abspath(filename)
    print suite_location

    test_file = TestSuite(suite_location)

    test_file.check_tags()
    test_file.check_unusued_variables()
    test_file.check_unused_keywords()
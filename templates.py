JINJA_TEMPLATE = '''
<html>
    <body>
        <h1> Summary </h1>
        <ul>
        {% for test_suite in test_suites %}
            <li>{{ test_suite.name }}
            <ul>
            {% for test_case in test_suite.testcase_table %}
                <li>{{ test_case.name }}
                    <ol>
                        {% for test_step in test_case.steps %}
                        <li>{{ test_step.keyword }}</li>
                        {% endfor %}
                    </ol>
                </li>
            {% endfor %}
            </ul>
        </li>
        {% endfor %}
        </ul>
    </body>
</html>
'''
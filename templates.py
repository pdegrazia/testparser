JINJA_TEMPLATE = '''
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">
        <script src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
        <script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    </head>
    <body>
        <h1> Summary </h1>
        <div data-role="main" class="ui-content">
                <ul>
                {% for test_suite in test_suites %}
                    <li data-role="collapsible" style="list-style: none;"><h1>{{ test_suite.name }}</h1>
                    <ol>
                    {% for test_case in test_suite.testcase_table %}
                            <li data-role="collapsible" style="list-style: none;"><h1>{{ test_case.name }}</h1>
                                <ul>
                                    {% for test_step in test_case.steps %}
                                    <li>{{ test_step.name }}</li>
                                    {% endfor %}
                                </ul>
                            </li>
                    {% endfor %}
                    </ol>
                </li>
                {% endfor %}
                </ul>
        </div>
    </body>
</html>
'''
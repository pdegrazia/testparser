JINJA_TEMPLATE = '''
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="mystyle.css">
        <style>
            .button-qa-ws {
                background-color: yellow;
            }
        </style>

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    </head>
    <body>
        <h1 style="text-align:center;background-color:#EF632F;color:White;font-family:Merriweather"> Regression pack summary </h1>
        <div id="myBtnContainer"  style="background-color:#F2F2F2;">
            <button class="btn active" onclick="filterSelection('all')"> Show all</button>
            <button class="btn" onclick="filterSelection('fe')"> FE</button>
            <button class="btn" onclick="filterSelection('api')"> API</button>
            <button class="btn" onclick="filterSelection('events')"> EVENTS</button>
        </div>
        <!--
        <div data-role="main" class="ui-content">
                <ul>
                {% for test_suite in test_suites %}
                    <li data-role="collapsible" style="list-style:none;"><h1>{{ test_suite.name }}</h1>
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
        -->
        <div id="suite-accordion">
            <ul class="list-group">
            {% for test_suite in test_suites %}
            {% set suite_loop = loop %}
                <li class="list-group-item" style="background-color:#F2F2F2;">
                      <div class="card">
                        <div class="card-header" id="suite-heading-{{suite_loop.index}}">
                          <h5 class="mb-0">
                            <button class="btn btn-link collapsed" style="color:Black;" data-toggle="collapse" data-target="#collapse-{{suite_loop.index}}" aria-expanded="false" aria-controls="collapse-{{suite_loop.index}}">
                              {{ test_suite.name }}
                                    {% for tag in test_suite.setting_table.force_tags.value %}
                                        <span class="badge badge-pill badge-secondary">{{tag}}</span>
                                    {% endfor %}
                            </button>
                          </h5>
                        </div>

                        <div id="collapse-{{suite_loop.index}}" class="collapse" aria-labelledby="suite-heading-{{suite_loop.index}}" data-parent="#suite-accordion">
                          <div class="card-body" id="test-accordion">
                            <ol class="list-group">
                                {% for test_case in test_suite.testcase_table %}
                                    <li class="list-group-item">
                                        <div class="card">
                                            <div class="card-header" id="test-heading-{{suite_loop.index}}-{{loop.index}}">
                                              <h5 class="mb-0">
                                                <button class="btn btn-link collapsed in" style="color:Black;" data-toggle="collapse" data-target="#test-collapse-{{suite_loop.index}}-{{loop.index}}" aria-expanded="false" aria-controls="test-collapse-{{suite_loop.index}}-{{loop.index}}">
                                                  {{ test_case.name }}
                                                </button>
                                              </h5>
                                            </div>
                                            <div id="test-collapse-{{suite_loop.index}}-{{loop.index}}" class="collapse" aria-labelledby="test-heading-{{suite_loop.index}}-{{loop.index}}" data-parent="#test-accordion">
                                                <div class="card-body">
                                                    <ul class="list-group">
                                                        {% for test_step in test_case.steps %}
                                                            <li>{{ test_step.name }}</li>
                                                        {% endfor %}
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                {% endfor %}
                            </ol>
                          </div>
                        </div>
                      </div>
                </li>
            {% endfor %}
            </ul>
        </div>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

    </body>
</html>
'''
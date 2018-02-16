JINJA_TEMPLATE = '''
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="styles/style.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    </head>
    <body>
        <nav class="navbar bg-light navbar-light justify-content-between py-4">
          <img src="{{image_path}}" width="315" height="82" class="d-inline-block align-top" alt="">
        </nav>
        <div id="filterSection">
            <div id="myBtnContainer" style="margin-top:15px;">
                <div style="float:left;margin-right:60px;margin-left:22px;">
                    <button class="btn btn-outline-dark active" onclick="filterSelection('all')"> Show all</button>
                    <button class="btn btn-outline-dark" onclick="filterSelection('web')"> FE</button>
                    <button class="btn btn-outline-dark" onclick="filterSelection('api')"> API</button>
                    <button class="btn btn-outline-dark" onclick="filterSelection('events')"> EVENTS</button>
                </div>
            </div>
            <div class="form-inline" id="searchForm" style="margin-top:15px;">
                <div>
                    <input class="form-control" id="submitTag" type="search" placeholder="Search by tag" aria-label="Search">
                    <span class="input-group-btn">
                        <button class="btn btn-dark" onclick="tagFilterSelection('clear')" type="button">Clear</button>
                    </span>
                    <button class="btn btn-outline-dark" onclick="tagFilterSelection()" style="margin-right:60px;" type="button">Search</button>
                </div>
                <span id="addfilter" class="btn btn-outline-dark" onclick="showExtraFilter()">Add extra filter</span>
                <div id="extrafilter" style="display:none;">
                    <input class="form-control" id="submitTag2" type="search" placeholder="Search by additional tag" aria-label="Search">
                    <span class="input-group-btn">
                        <button class="btn btn-dark" onclick="tagFilterSelection('clear', 'extraTagShow')" type="button">Clear</button>
                    </span>
                    <button class="btn btn-outline-dark my-2 my-sm-0" onclick="tagFilterSelection('searchbox', 'extraTagShow')" style="margin-right:60px;" type="button">Search</button>
                </div>
                <span id="removefilter" class="btn btn-outline-dark" style="display:none;" onclick="hideExtraFilter();">Remove extra filter</span>
            </div>
            <p id="filter-summary" style="margin-top:15px;margin-left:375px;"><b id=numberresults></b> results shown. Searching by: <b id=categoryfilterapplied></b> <b id=tagfilterapplied></b> <b id=extratagfilterapplied></b></p>
        </div>
        <div id="suite-accordion">
            <ul class="list-group list-group-flush" style="margin-top:15px;">
            {% for test_suite in test_suites %}
            {% set suite_loop = loop %}
                <div class= "filterDiv{% for tag in test_suite.setting_table.force_tags.value %} {{tag.lower()}}{% endfor %} show tagShow extraTagShow" style="background-color:#F2F2F2;">
                <li class="list-group-item">
                      <div class="card">
                        <div class="card-header" id="suite-heading-{{suite_loop.index}}">
                          <h5 class="mb-0">
                            <button class="btn btn-link collapsed" style="color:Black;font-family:Lato;font-size:20px" data-toggle="collapse" data-target="#collapse-{{suite_loop.index}}" aria-expanded="false" aria-controls="collapse-{{suite_loop.index}}">
                              {{ test_suite.name }}
                            </button>
                                {% for tag in test_suite.setting_table.force_tags.value %}
                                    <span class="btn badge badge-pill badge-secondary" onclick="tagFilterSelection('{{tag}}')";>{{tag}}</span>
                                {% endfor %}
                          </h5>
                        </div>

                        <div id="collapse-{{suite_loop.index}}" class="collapse" aria-labelledby="suite-heading-{{suite_loop.index}}">
                          <div class="card-body" id="test-accordion">
                            <ol class="list-group list-group-flush">
                                {% for test_case in test_suite.testcase_table %}
                                    <li class="list-group-item" style="border:none;">
                                        <div class="card">
                                            <div class="card-header" id="test-heading-{{suite_loop.index}}-{{loop.index}}">
                                              <h5 class="mb-0">
                                                <button class="btn btn-link collapsed in" style="color:Black;font-size:19px;" data-toggle="collapse" data-target="#test-collapse-{{suite_loop.index}}-{{loop.index}}" aria-expanded="false" aria-controls="test-collapse-{{suite_loop.index}}-{{loop.index}}">
                                                  {{ test_case.name }}
                                                </button>
                                              </h5>
                                            </div>
                                            <div id="test-collapse-{{suite_loop.index}}-{{loop.index}}" class="collapse" aria-labelledby="test-heading-{{suite_loop.index}}-{{loop.index}}">
                                                <div class="card-body">
                                                    <ul class="list-group list-group-flush">
                                                        {% for test_step in test_case.steps %}
                                                            <div class="keyword" style="font-size:18px;">{{ test_step.name }}</div>
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
                </div>
            {% endfor %}
            </ul>
        </div>
        <script src="scripts/main.js"></script>
    </body>
</html>
'''
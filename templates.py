JINJA_TEMPLATE = '''
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            .filterDiv {
                display: none;
                }
            .show {
                display: none;
            }
            .tagShow {
                display: none;
            }
            .extraTagShow {
                display: none;
            }
            .show.tagShow.extraTagShow{
                display: block;
            }
        </style>

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    </head>
    <body>
        <!--<h1 style="text-align:center;background-color:#F2F2F2;color:White;font-family:Merriweather"> Regression pack summary </h1>-->
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
                <div class= "filterDiv{% for tag in test_suite.setting_table.force_tags.value %} {{tag}}{% endfor %} show tagShow extraTagShow" style="background-color:#F2F2F2;">
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
                                                            <li style="font-size:18px;">{{ test_step.name }}</li>
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
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script>

            showResults();

            function filterSelection(c) {
                var x, i;
                x = document.getElementsByClassName('filterDiv');
                if (c == "all") c = "";
                for (i = 0; i < x.length; i++) {
                    RemoveClass(x[i], "show");
                    if (x[i].className.indexOf(c) > -1) AddClass(x[i], "show");
                }
                document.getElementById('categoryfilterapplied').innerHTML = c;
                showResults()
            }

            function AddClass(element, name) {
                var i, arr1, arr2;
                arr1 = element.className.split(" ");
                arr2 = name.split(" ");
                for (i = 0; i < arr2.length; i++) {
                    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
                }
            }

            function RemoveClass(element, name) {
                var i, arr1, arr2;
                arr1 = element.className.split(" ");
                arr2 = name.split(" ");
                for (i = 0; i < arr2.length; i++) {
                   while (arr1.indexOf(arr2[i]) > -1) {
                      arr1.splice(arr1.indexOf(arr2[i]), 1);
                   }
                }
                element.className = arr1.join(" ");
            }

            function showResults(){
                var matches, total = 0;
                matches = document.getElementsByClassName("show tagShow extraTagShow").length;
                document.getElementById('numberresults').innerHTML = matches;
                //total = document.getElementsByClassName("filterDiv").length;
                //if (matches == total) {}
            }

            function tagFilterSelection(filter = 'searchbox', tag = 'tagShow') {
                var id, input, filterresult, x, i;
                x = document.getElementsByClassName('filterDiv');
                if (filter == "clear") {
                    input = "";
                    if (tag == "tagShow") {
                        $("#submitTag").val("");
                        document.getElementById('tagfilterapplied').innerHTML = input;
                    } else if (tag == "extraTagShow") {
                        $("#submitTag2").val("");
                        document.getElementById('extratagfilterapplied').innerHTML = input;
                    }
                } else if (filter == "searchbox") {
                    if (tag == "tagShow") {
                        id = 'submitTag';
                        filterresult = "tagfilterapplied";
                    }
                    else if (tag == "extraTagShow") {
                        id = 'submitTag2';
                        filterresult = "extratagfilterapplied";
                    }
                    input = document.getElementById(id).value;
                    document.getElementById(filterresult).innerHTML = input;
                } else {
                    input = filter;
                    id = "submitTag"
                    document.getElementById('tagfilterapplied').innerHTML = input;
                    //document.getElementById('submitTag').value = input;
                }
                for (i = 0; i < x.length; i++) {
                    RemoveClass(x[i], tag);
                    if (x[i].className.indexOf(input) > -1) {AddClass(x[i], tag);}
                }
                document.getElementById('submitTag').value = "";
                document.getElementById('submitTag2').value = "";
                showResults()
            }

            function showExtraFilter() {
                document.getElementById("addfilter").style.display = "none";
                document.getElementById("extrafilter").style.display = "block";
                document.getElementById("removefilter").style.display = "block";
            }

            function hideExtraFilter() {
                document.getElementById("removefilter").style.display = "none";
                document.getElementById("extrafilter").style.display = "none";
                document.getElementById("addfilter").style.display = "block";
                tagFilterSelection('clear', 'extraTagShow')
            }

            var tagFilter = document.getElementById("searchForm");
            tagFilter.addEventListener("keydown", function (e) {
                if (e.keyCode === 13) {
                    tagFilterSelection();
                }

            });

            var btnContainer = document.getElementById("myBtnContainer");
            var btns = btnContainer.getElementsByClassName("btn");
            for (var i = 0; i < btns.length; i++) {
              btns[i].addEventListener("click", function(){
                var current = document.getElementsByClassName("active");
                current[0].className = current[0].className.replace(" active", "");
                this.className += " active";
              });
            }

        </script>
    </body>
</html>
'''
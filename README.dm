This is a small script to parse robotframework files contained in a directory, 

It returns an HTML file that contains the suite name and the test cases.

For every test suite, all tags included in the "Settings" section will be shown next to the suite name.

On the top of the page three filters are shown. From left to right:
	- Category filter: 
		- Show all: Shows all test suites within the regression folder.
		- FE: Shows only front-end automations tagged as 'web'.
		- API: Shows automations not covering the user interface, tagged as 'api'.
		- EVENTS: Shows automations covering mixpanel events, tagged as 'events'.
	
	- Tag filter: This filter allows to search by tag. There are three ways to use this filter:
		- By typing tag and clicking on the search button.
		- By typing tag and pressing enter key.
		- By clicking on any tag within any test suite element shown in the list.

	- Extra tag filter: This filter allows to search by a second tag. This optional filter is displayed when the user clicks on 'Add extra filter' button. Unlike the previous tag filter, the optional one will only work when user types a tag and clicks on the 'Search' button (pressing enter doesn't apply the filter!).

Both tag filters can be cleared/used individually.

Below the search boxes a filter summary will tell the user the current filters applied and the number of results that match them.


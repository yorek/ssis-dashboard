# Release Notes

## v 0.6.7 Beta

* Fixed sql scripts so that they works well with ODBC drivers (both on linux and windows)
* Added support for Docker
* Reorganized documentation

## v 0.6.6 Beta

* Improved configuration management. Now confguration is read from config.cfg, which is NOT included in the GitHub repository. This is a step need to make easier to download updted version directly from GitHub. 
* Added support for Google Analytics

## v 0.6.5 Beta

* Moved to Roboto font for better readability
* Navigation menu correctly sort items (Issue #19)
* Started using pylint to have cleaner code

## v 0.6.4 Beta

* Updated to Python 3
* Dropped usage of MetisMenu in favor of SmartMenus
* Added package execution chart
* Moved the package execution details in a dedicated page
* Added the ability to display all events
* Added a page to show parameters execution values and parameter overrides
* Code cleanup and refactored

## v 0.6.3 Beta

* Added first support to show/hide navigation panel
* Included Environment informations in package list (Issue #5)
* Upgraded to Font Awesome v 4.5.0
* Upgraded to Bootstrap 3.3.6
* Added refresh page button

## v 0.6.1 Beta

* Updated Morris.js to v 0.5.1
* Updated MetisMenu to v 1.1.1
* Added information on "Child" Packages
* Added more detail to the "Package Execution History" page. Also added an estimated end time / elapsed time for running packages, using a moving average of 7 steps.
* Added navigation sidebar in the main page that shows available folders and projects
* Added support for folders and project filtering
* Changed configuration file in order to comply with Python/Flask standards
* Cleaned Up code in order to follow Python best pratices (still a lot to do :))

## v 0.5.2 Beta

Added support for "\*" wildcard in project names. Now you can filter a specific project name using an url like: 
```
http://<yourserver>/project/MyPro*
```
Added initial support for Package Execution History. Just click on a package name and you'll see its latest 15 executions

## v 0.4 Beta

First public release

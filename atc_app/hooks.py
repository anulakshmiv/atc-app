# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "atc_app"
app_title = "atc-app"
app_publisher = "frappe"
app_description = "atc-app"
app_icon = "blue"
app_color = "mit"
app_email = "atcqw@gmail.com"
app_license = "mit"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/atc_app/css/atc_app.css"
# app_include_js = "/assets/atc_app/js/atc_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/atc_app/css/atc_app.css"
# web_include_js = "/assets/atc_app/js/atc_app.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "atc_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "atc_app.install.before_install"
# after_install = "atc_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "atc_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"atc_app.tasks.all"
# 	],
# 	"daily": [
# 		"atc_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"atc_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"atc_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"atc_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "atc_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "atc_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "atc_app.task.get_dashboard_data"
# }


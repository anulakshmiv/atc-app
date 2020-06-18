from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
		{
        	"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
			 		"is_query_report": True,
			  		"name": "Opportunity Details (DellEMC)",
					"label": _("Opportunity Details (DellEMC)"),
			  		"doctype": "Opportunity",
				},
		  		{
					"type": "report",
			 		"is_query_report": True,
 			  		"name": "Opportunity Details (Huawei)",
					"label": _("Opportunity Details (Huawei)"),
			  		"doctype": "Opportunity",  
				},
                {
					"type": "report",
			 		"is_query_report": True,
 			  		"name": "Opportunity Details (Juniper)",
					"label": _("Opportunity Details (Juniper)"),
			  		"doctype": "Opportunity",  
				},
                {
					"type": "report",
			 		"is_query_report": True,
 			  		"name": "Opportunity Details (Misc)",
					"label": _("Opportunity Details (Misc)"),
			  		"doctype": "Opportunity",  
				},
  			]
	   	},
    ]
       
     
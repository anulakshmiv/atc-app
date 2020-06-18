# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns =[
		{
			"fieldname":"primary_organization",
			"label":("Primary Organization"),
			"fieldtype":"Select",
			"width":"150"
		},
		{
			"fieldname":"crm_id",
			"label":("CRM ID"),
			"fieldtype":"Data",
			"width":"100"
		},
		{
			"fieldname":"cust_name",
			"label":("Customer Name"),
			"fieldtype":"Link",
			"options":"Customer",
			"width":"200"
		},
		{
			"fieldname":"description",
			"label":("Opportunity Title"),
			"fieldtype":"Data",
			"width":"200"
		},
		{
			"fieldname":"expected_revenue",
			"label":("Expected Revenue (AED)"),
			"fieldtype":"Currency",
			"options":"Currency",
			"width":"150"
		},
		{
			"fieldname":"sales_account_manager",
			"label":("Sales Account Manager"),
			"fieldtype":"Select",
			"width":"200"
		},
		{
			"fieldname":"expected_closure_date",
			"label":("Expected Closure Date"),
			"fieldtype":"Date",
			"width":"150"
		},
		{
			"fieldname":"lead_generated_by",
			"label":("Lead Generated By"),
			"fieldtype":"Select",
			"width":"150"
		},
		{
			"fieldname":"engagement_type",
			"label":("Engagement Type"),
			"fieldtype":"Select",
			"width":"150"
		},
		{
			"fieldname":"opportunity_stage",
			"label":("Opportunity Stage"),
			"fieldtype":"Select",
			"width":"150"
		},
		{
			"fieldname":"commit_month",
			"label":("Commit Month"),
			"fieldtype":"Select",
			"width":"150"
		},
		{
			"fieldname":"commit_week",
			"label":("Commit Week"),
			"fieldtype":"Select",
			"width":"150"
		},
		{
			"fieldname":"juniper_deal_description",
			"label":("Juniper Deal Description"),
			"fieldtype":"Data",
			"width":"200"
		},
		{
			"fieldname":"juniper_deal_value_usd",
			"label":("Juniper Deal Value (USD)"),
			"fieldtype":"Float",
			"width":"150"
		},
		{
			"fieldname":"juniper_dr_id",
			"label":("Juniper DR ID"),
			"fieldtype":"Data",
			"width":"150"
		},
		{
			"fieldname":"juniper_dr_status",
			"label":("Juniper DR status"),
			"fieldtype":"Select",
			"width":"200"
		},
	]
	if filters.get("sales_account_manager") and filters.get("juniper_account_manager"):
		data = frappe.db.sql('''select tabOpportunity.primary_organization,tabOpportunity.crm_id,tabOpportunity.cust_name,tabOpportunity.description,tabOpportunity.expected_revenue,tabOpportunity.sales_account_manager,tabOpportunity.expected_closure_date,tabOpportunity.lead_generated_by,tabOpportunity.engagement_type,tabOpportunity.opportunity_stage,tabOpportunity.commit_month,tabOpportunity.commit_week,`tabJuniper DR Details`.juniper_deal_description,`tabJuniper DR Details`.juniper_deal_value_usd,`tabJuniper DR Details`.juniper_dr_id,`tabJuniper DR Details`.juniper_dr_status
			from tabOpportunity INNER JOIN `tabJuniper DR Details` ON tabOpportunity.name = `tabJuniper DR Details`.parent
			where sales_account_manager = %s and juniper_account_manager = %s''', (filters.get('sales_account_manager'), (filters.get('juniper_account_manager'))))
		print(data)
	elif filters.get("sales_account_manager") and not filters.get("juniper_account_manager"):
		data = frappe.db.sql('''select tabOpportunity.primary_organization,tabOpportunity.crm_id,tabOpportunity.cust_name,tabOpportunity.description,tabOpportunity.expected_revenue,tabOpportunity.sales_account_manager,tabOpportunity.expected_closure_date,tabOpportunity.lead_generated_by,tabOpportunity.engagement_type,tabOpportunity.opportunity_stage,tabOpportunity.commit_month,tabOpportunity.commit_week,`tabJuniper DR Details`.juniper_deal_description,`tabJuniper DR Details`.juniper_deal_value_usd,`tabJuniper DR Details`.juniper_dr_id,`tabJuniper DR Details`.juniper_dr_status
			from tabOpportunity INNER JOIN `tabJuniper DR Details` ON tabOpportunity.name = `tabJuniper DR Details`.parent
			where sales_account_manager = %s''', (filters.get('sales_account_manager')))
		print(data)
	elif filters.get("juniper_account_manager") and not filters.get("sales_account_manager"):
		data = frappe.db.sql('''select tabOpportunity.primary_organization,tabOpportunity.crm_id,tabOpportunity.cust_name,tabOpportunity.description,tabOpportunity.expected_revenue,tabOpportunity.sales_account_manager,tabOpportunity.expected_closure_date,tabOpportunity.lead_generated_by,tabOpportunity.engagement_type,tabOpportunity.opportunity_stage,tabOpportunity.commit_month,tabOpportunity.commit_week,`tabJuniper DR Details`.juniper_deal_description,`tabJuniper DR Details`.juniper_deal_value_usd,`tabJuniper DR Details`.juniper_dr_id,`tabJuniper DR Details`.juniper_dr_status
			from tabOpportunity INNER JOIN `tabJuniper DR Details` ON tabOpportunity.name = `tabJuniper DR Details`.parent
			where juniper_account_manager = %s''', (filters.get('juniper_account_manager')))
		print(data)
	else:
		data = frappe.db.sql('''select tabOpportunity.primary_organization,tabOpportunity.crm_id,tabOpportunity.cust_name,tabOpportunity.description,tabOpportunity.expected_revenue,tabOpportunity.sales_account_manager,tabOpportunity.expected_closure_date,tabOpportunity.lead_generated_by,tabOpportunity.engagement_type,tabOpportunity.opportunity_stage,tabOpportunity.commit_month,tabOpportunity.commit_week,`tabJuniper DR Details`.juniper_deal_description,`tabJuniper DR Details`.juniper_deal_value_usd,`tabJuniper DR Details`.juniper_dr_id,`tabJuniper DR Details`.juniper_dr_status
			from tabOpportunity INNER JOIN `tabJuniper DR Details` ON tabOpportunity.name = `tabJuniper DR Details`.parent''')
		print(data)
	
	return columns, data



# Copyright (c) 2021, Dharshini and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date
from frappe.utils import date_diff

class RentPayment(Document):
    
	def validate(self):
		fromdate=self.date_of_amount_paid_last_time
		todate=self.todays_date
		tot=date_diff(fromdate, todate)
		self.totaldays=abs(int(tot))
		self.total_rent=abs(int(tot))*self.daily_rent
		self.balance_to_be_paid=(abs(int(tot))*self.daily_rent)-self.amount_paid
	pass
	
	
    	

	

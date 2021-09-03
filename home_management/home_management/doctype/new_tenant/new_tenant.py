# Copyright (c) 2021, Dharshini and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class NewTenant(Document):
	def validate(self):
		if frappe.db.exists(
			"Booked Houses",
			{
				"houseno": self.appartment_no,
			}
			):
				frappe.throw("Sorry :( the Flat you have choosen is Already Booked")
		else:
			if frappe.db.exists(
				"To Let Lists",
				{
					"house_no": self.appartment_no,
				}
				):
                		frappe.msgprint("Welcome To CasaGrand Appartment the Flat you have choosen is Booked.")
			if frappe.db.exists(
				"To Let Lists",
				{
					"house_no":self.appartment_no,
				}
				):
						dc=frappe.new_doc("Booked Houses")
						dc.id=self.id
						dc.houseno=self.appartment_no
						dc.save()
						frappe.msgprint("Booking Done!")
			else:
    				frappe.throw("Please choose with available flats")
		
			
			
        

   

   
       


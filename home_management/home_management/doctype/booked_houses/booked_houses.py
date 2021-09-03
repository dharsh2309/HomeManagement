# Copyright (c) 2021, Dharshini and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BookedHouses(Document):
	def on_validate(self):

		self.id=frappe.db.get_value("New Tenant","id")
	pass

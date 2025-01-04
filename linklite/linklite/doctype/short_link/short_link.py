# Copyright (c) 2024, Build With Hussain and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document


class ShortLink(Document):
	def on_trash(self):
		# delete the "Short Link Click" records
		frappe.db.delete("Short Link Click", {"link": self.name})

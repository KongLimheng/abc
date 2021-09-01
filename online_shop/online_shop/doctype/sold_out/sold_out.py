# Copyright (c) 2021, Heng Coder and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SoldOut(Document):
	def before_save(self):
		product = frappe.get_doc("Product", self.product)
		self.validate_qty()
		self.total_price = int(product.price) * self.qty
		# frappe.msgprint(price)

		product.quantities -= self.qty
		product.save()


	def validate_qty(self):
		product = frappe.get_doc("Product", self.product)
		if self.qty > product.quantities:
			frappe.throw(f"Product quantities out of stock remain: {product.quantities}")
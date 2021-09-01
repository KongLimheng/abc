// Copyright (c) 2021, Heng Coder and contributors
// For license information, please see license.txt

frappe.ui.form.on('Category', {
	refresh: function(frm) {
		frm.add_custom_button("Create Product", ()=>{
			console.log(frm.doc)
			frappe.new_doc('Product', {
				category: frm.doc.name
			})
		})
	}
});

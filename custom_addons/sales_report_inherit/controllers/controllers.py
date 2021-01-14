# -*- coding: utf-8 -*-
# from odoo import http


# class SalesReportInherit(http.Controller):
#     @http.route('/sales_report_inherit/sales_report_inherit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_report_inherit/sales_report_inherit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_report_inherit.listing', {
#             'root': '/sales_report_inherit/sales_report_inherit',
#             'objects': http.request.env['sales_report_inherit.sales_report_inherit'].search([]),
#         })

#     @http.route('/sales_report_inherit/sales_report_inherit/objects/<model("sales_report_inherit.sales_report_inherit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_report_inherit.object', {
#             'object': obj
#         })

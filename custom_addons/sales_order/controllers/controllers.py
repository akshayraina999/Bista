# -*- coding: utf-8 -*-
# from odoo import http


# class SalesOrder(http.Controller):
#     @http.route('/sales_order/sales_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_order/sales_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_order.listing', {
#             'root': '/sales_order/sales_order',
#             'objects': http.request.env['sales_order.sales_order'].search([]),
#         })

#     @http.route('/sales_order/sales_order/objects/<model("sales_order.sales_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_order.object', {
#             'object': obj
#         })

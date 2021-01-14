# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_order(models.Model):
    _name = 'sales_order'
    _inherit = 'sale.order'



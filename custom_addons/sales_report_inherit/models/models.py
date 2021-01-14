# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import pytz
from odoo.exceptions import ValidationError, AccessError

class SalesReportInherit(models.Model):
        _name = "sale.order"
        _inherit = "sale.order"

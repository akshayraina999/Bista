# -*- coding: utf-8 -*-
from odoo import models, fields, tools, api, _
import pytz
from odoo.exceptions import UserError, ValidationError

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"


    is_trainee = fields.Boolean('Trainee')
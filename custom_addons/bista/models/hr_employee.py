# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, AccessError


class hr_employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'


    new_ref = fields.Boolean(string="Trainee")

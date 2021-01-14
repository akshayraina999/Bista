# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, AccessError


class hr_employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'


    is_trainee = fields.Boolean(string="Trainee")

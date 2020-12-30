# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class designation(models.Model):
    _name = 'bista_designation.bista_designation'
    _description = 'Bista Designation'
    _rec_name = 'd_name'
    d_name = fields.Char(string='Name', required=True)
    trainee_ids = fields.One2many('bista_trainee.bista_trainee', 'training_batch_id', string='Trainee')

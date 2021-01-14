# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class bista_training(models.Model):
    _name = 'bista_training.bista_training'
    _description = 'Bista Training'

    name = fields.Char(string='Batch Name')
    doj = fields.Char(string='Date of Joining')
    students = fields.Integer(string='Number of Interns')
    trainee_ids = fields.One2many('bista_trainee.bista_trainee', 'training_batch_id', string='Trainee')

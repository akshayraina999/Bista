# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class bista_batch(models.Model):
    _name = 'bista_batch'
    _description = 'Bista Batch'

    name = fields.Char(string='Batch Name', required=True)
    start_date = fields.Date(string="Start Date", readonly=True)
    end_date = fields.Date(string="End Date", readonly=True)

    location = fields.Many2one('location.location', string="Location")
    # trainee = fields.One2many('bista_trainee.bista_trainee', 'location')
    # trainer = fields.One2many('bista_trainer.bista_trainer', 'location')
    stages = fields.Many2one('training_stages', string='Stages')
    state = fields.Selection([('draft', 'Draft'), ('progress', 'Progress'), ('done', 'Done')])
    training_topic = fields.Many2many('training_topic.training_topic', string='Training Topic')
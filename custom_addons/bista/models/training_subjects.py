# -*- coding: utf-8 -*-

from odoo import models, fields, api


class subjects(models.Model):
    _name = 'subjects.subjects'
    _description = 'Subjects'

    name = fields.Char('Name', required=True)
    description = fields.Html(string='Description')
    topics = fields.One2many('training_topic.training_topic', 'topic_sub', string='Topic')
    trainer = fields.Many2many('bista_trainer.bista_trainer', string='Trainer')

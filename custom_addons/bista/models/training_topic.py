# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class topic(models.Model):
    _name = 'training_topic.training_topic'
    _description = 'Topic'

    topic_name = fields.Char(string='Topic Name', required=True)
    topic_sub = fields.Many2one('subjects.subjects', string='Subject')

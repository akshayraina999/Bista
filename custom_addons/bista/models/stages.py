# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class training_stages(models.Model):
    _name = 'training_stages'
    _description = 'Training Stages'

    name = fields.Char('Name')
    batch = fields.Boolean('Available on Batch')
    training = fields.Boolean('Available on Training')

    status = fields.Selection(
        [('draft','Draft'), ('progress', 'Progress'), ('done', 'Done')], string='Status', default='draft', required=True)

    # def draft(self):
    #     for rec in self:
    #         rec.status = 'draft'
    #
    # def progress(self):
    #     for rec in self:
    #         rec.status = 'progress'
    #
    # def done(self):
    #     for rec in self:
    #         rec.status = 'done'
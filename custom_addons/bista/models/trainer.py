# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class trainer(models.Model):
    _name = 'bista_trainer.bista_trainer'
    _description = 'Bista Trainer'

    image = fields.Binary(string="Image", tracking=True)
    name = fields.Char('Full Name', compute='_compute_name', store="True", tracking=True)
    trainer_first_name = fields.Char('Name', required=True)
    trainer_last_name = fields.Char('Last Name')

    @api.depends('trainer_first_name', 'trainer_last_name')
    def _compute_name(self):
        for record in self:
            record.name = str(record.trainer_first_name or '') + ' ' + str(record.trainer_last_name or '')

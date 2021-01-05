# -*- coding: utf-8 -*-

from odoo import models, fields, api

class batch(models.Model):
    _name = 'bista_batch.bista_batch'
    _description = 'Bista Batch'

    batch_name = fields.Char(string='Bista Batch')
    start_date = fields.Date(string="Batch Start Date")
    end_date = fields.Date(string='Batch End Date')
    location = fields.Many2one('location.location', string='Location')
    trainee = fields.One2many('trainee_name', 'x', string='Trainee')
    trainers = fields.One2many('trainer_name', 'y', string='Trainer')
    topics = fields.Many2many('training_topic.training_topic', string='Training Topic')

class batch_trainee(models.Model):
    _name = 'trainee_name'
    _description = 'Bista Trainee'

    trainee_record = fields.Many2one('bista_trainee.bista_trainee', string="Trainee", store=True, index=True)
    x = fields.Many2one('bista_batch.bista_batch', string="x")


class Batch_trainer_name(models.Model):
    _name = 'trainer_name'
    _description = 'Bista Trainer'

    trainer_record = fields.Many2one('bista_trainer.bista_trainer', string="Trainer", store=True, index=True)
    y = fields.Many2one('bista_batch.bista_batch', string="y")
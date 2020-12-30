# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class trainee(models.Model):
    _name = 'bista_trainee.bista_trainee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Bista Trainee'

    image = fields.Binary(string="Image", tracking=True)
    name = fields.Char('Full Name', compute='_compute_name', store="True", tracking=True)
    trainee_first_name = fields.Char('Name', required='1', tracking=True)
    trainee_last_name = fields.Char('Last Name')
    employee_id = fields.Many2one('hr.employee', string="Employee")
    email = fields.Char('Email', required='1')
    dob = fields.Date('Date of Birth')
    doj = fields.Date('Date of Joining')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender", required='1')

    training_batch_id = fields.Many2one('bista_designation.bista_designation', string='Batch')
    trainee_id = fields.Char(string='Trainee ID', default=lambda self: _('ID'), required=True, copy=False,
                             readonly=True,
                             index=True)
    trainee_location = fields.Many2one('location.location', string="Location",
                                       help='Location Field')

    state = fields.Selection(
        [('new', 'New'), ('training', 'Training'), ('employed', 'Employed'), ('rejected', 'Rejected')], string='State',
        default='new', tracking=True)

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
        ('4', 'Extreme High')], string='Priority',
        index=True)

    image_1920 = fields.Image('Logo')

    @api.model
    def create(self, vals):
        print('@@@', vals)
        return super(trainee, self).create(vals)

    def confirm(self):
        for rec in self:
            rec.state = 'training'

    def action_rejected(self):
        for rec in self:
            rec.state = 'rejected'

    def action_employed(self):
        for rec in self:
            rec.state = 'employed'
            employee_details = {
                'name': rec.name,
                'image_1920': rec.image,
                'is_trainee': True
            }
            employee = self.env['hr.employee'].create(employee_details)
            rec.employee_id = employee
        #     contact = self.env['res.partner'].create({'name':rec.trainee_first_name, 'is_trainee':True})
        # return True

    @api.depends('trainee_first_name', 'trainee_last_name')
    def _compute_name(self):
        for record in self:
            record.name = str(record.trainee_first_name or '') + ' ' + str(record.trainee_last_name or '')

    @api.model
    def create(self, vals):
        if vals.get('trainee_id', _('New')) == _('New'):
            vals['trainee_id'] = self.env['ir.sequence'].next_by_code('trainee.id') or _('New')
            result = super(trainee, self).create(vals)
            return result

    _sql_constraints = [('email_uniq', 'unique(email)', 'Email Id should be unique')]

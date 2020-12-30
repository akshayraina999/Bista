# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class trainee_location(models.Model):
    _name = 'location.location'
    _description = 'Trainee Location'

    _rec_name = 'loc_name'
    loc_name = fields.Char(string="Location Name", required=True)
    street1 = fields.Char(string="Street 1")
    street2 = fields.Char(string="Street 2")
    city = fields.Char(string="City")
    state_id = fields.Many2one("res.country.state", string='State', help='Enter State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict',
                                 required=True)
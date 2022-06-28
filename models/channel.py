from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassChannel(models.Model):
    _name = "olclass.channel"
    _inherit = []
    _description = "Online Class Channel"
    _order = 'id'

    name = fields.Char(string='Name', default='New')
    participant_id = fields.Many2one('res.partner', string='Participant')

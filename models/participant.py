from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassParticipant(models.Model):
    _name = "olclass.participant"
    _inherit = []
    _description = "Online Class Participant"
    _order = 'id'

    name = fields.Char(string='Name', default='New')
    participant_id = fields.Many2one('res.partner', string='Participant')

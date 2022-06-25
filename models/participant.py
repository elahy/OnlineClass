from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassParticipant(models.Model):
    _name = "olclass.participant"
    _inherit = []
    _description = "Online Class Participant"
    _rec_name = 'name'
    _order = 'id'

    name = fields.Char(string='Name', default='New')

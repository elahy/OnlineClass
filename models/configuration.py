from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassConfiguration(models.Model):
    _name = "olclass.configuration"
    _inherit = []
    _description = "Online Class Configuration"
    _order = 'id'

    name = fields.Char(string='Name', default='New')

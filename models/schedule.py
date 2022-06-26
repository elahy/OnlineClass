from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassSchedule(models.Model):
    _name = "olclass.schedule"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Online Class Schedule"
    _order = 'id desc'

    topic = fields.Char(string='Topic', default='New')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled'),
    ], string="Status", default='draft', tracking=True, required=True)
    teacher_id = fields.Many2one('res.users', string='Teacher')
    progress = fields.Integer(string="Progress", compute='_compute_progress')
    duration = fields.Float(string="Duration")
    channel = fields.Many2one('mail.channel', string='Channel')
    channel_id = fields.Char(string="Channel Id", compute='_compute_channel_id')

    def action_test(self):
        print(self.channel_id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': f'/web#cids=1&menu_id=84&default_active_id=mail.box_inbox&action=116&active_id=mail.channel_{self.channel_id}'
        }

    @api.depends('channel')
    def _compute_channel_id(self):
        for rec in self:
            rec.channel_id = rec.channel.id

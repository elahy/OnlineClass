from odoo import api, fields, models, _


# from odoo.exceptions import ValidationError


class OlclassSchedule(models.Model):
    _name = "olclass.schedule"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Online Class Schedule"
    _order = 'id desc'

    name = fields.Char(string='Topic', required=True)
    appointment_time = fields.Datetime(string='Schedule Time', tracking=True, required=True,
                                       default=fields.Datetime.now)
    teacher_id = fields.Many2one('res.users', string='Teacher')
    duration = fields.Float(string="Duration")
    course_id = fields.Many2one('olclass.course', string='Course')
    channel_id = fields.Char(string="Channel Id", related='course_id.channel_id')

    def action_test(self):
        print(self.channel_id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': f'/web#cids=1&menu_id=84&default_active_id=mail.box_inbox&action=116&active_id=mail.channel_{self.channel_id}'
        }

    @api.onchange('course_id')
    def course_id_onchange(self):
        if self.course_id:
            self.channel_id = self.course_id.channel_id

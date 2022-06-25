from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassSchedule(models.Model):
    _name = "olclass.schedule"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Online Class Schedule"
    _rec_name = 'name'
    _order = 'id desc'

    name = fields.Char(string='Sequence', default='New')
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

    # def unlink(self):
    #     for rec in self:
    #         if rec.state != 'draft':
    #             raise ValidationError(_("You can delete appointment only in 'draft' state ! "))
    #         return super(HospitalAppointment, self).unlink()

    # @api.model
    # def create(self, vals):
    #     vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
    #     return super(HospitalAppointment, self).create(vals)

    # @api.onchange('patient_id')
    # def onchange_patient_id(self):
    #     self.ref = self.patient_id.ref

    # def action_notification(self):
    #     action = self.env.ref('bm_hospital.action_hospital_patient')
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'display_notification',
    #         'params': {
    #             'title': _('Click to open the patient record'),
    #             'message': '%s',
    #             'links': [{
    #                 'label': self.patient_id.name,
    #                 'url': f'#action={action.id}&id={self.patient_id.id}&model=hospital.patient',
    #             }],
    #             'sticky': False,
    #             'next': {
    #                 'type': 'ir.actions.act_window',
    #                 'res_model': 'hospital.patient',
    #                 'res_id': self.patient_id.id,
    #                 'views': [(False, 'form')]
    #             }
    #         }
    #     }

    # def action_test(self):
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'target': 'new',
    #         'url': 'https://www.odoo.com'
    #     }

    # def action_done(self):
    #     for rec in self:
    #         rec.state = 'done'
    #     return {
    #         'effect': {
    #             'fadeout': 'slow',
    #             'message': 'Done!',
    #             'type': 'rainbow_man',
    #         }
    #     }

    # def action_share_whatsapp(self):
    #     if not self.patient_id.phone:
    #         raise ValidationError(_("Patient Record does not include Phone Number"))
    #     msg = " Hi %s You have an appointment at BM Hospital" % self.patient_id.name
    #     whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.patient_id.phone, msg)
    #     self.message_post(body=msg, subject='Whatsapp')
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'target': 'new',
    #         'url': whatsapp_api_url
    #     }

    # def action_in_consultation(self):
    #     for rec in self:
    #         if rec.state == 'draft':
    #             rec.state = 'in_consultation'

    # def action_done(self):
    #     for rec in self:
    #         rec.state = 'done'

    # def action_cancel(self):
    #     action = self.env.ref('bm_hospital.action_cancel_appointment').read()[0]
    #     return action
    #     # for rec in self:
    #     #     rec.state = 'cancel'

    # def action_draft(self):
    #     for rec in self:
    #         rec.state = 'draft'
    #
    # @api.depends('state')
    # def _compute_progress(self):
    #     for rec in self:
    #         if rec.state == 'draft':
    #             progress = 25
    #         elif rec.state == 'in_consultation':
    #             progress = 50
    #         elif rec.state == 'done':
    #             progress = 100
    #         else:
    #             progress = 0
    #         rec.progress = progress


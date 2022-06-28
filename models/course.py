from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassCourse(models.Model):
    _name = "olclass.course"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Online Class Courses"
    _rec_name = 'name'
    _order = 'id'

    name = fields.Char(string='Course Title')
    course_details = fields.Text(string='Description')
    instructor = fields.Many2one('res.users', string='Instructor')
    course_code = fields.Char(string='Course Code', default='OC001')
    tag_ids = fields.Many2many('course.tag', string='Tags')
    schedule_ids = fields.One2many('olclass.schedule', 'course_id', string='Class Schedules')
    channel = fields.Many2one('mail.channel', string='Channel')
    channel_id = fields.Char(string="Channel Id", compute='_compute_channel_id')
    number_of_class = fields.Integer(string="Number Of Classes")
    number_of_attendees = fields.Integer(string="Number Of Attendees", compute='_compute_number_of_attendees')

    state = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('admission_going_on', 'Admission Going On'),
        ('running', 'Running'),
        ('completed', 'Completed'),
    ], string="Status", default='upcoming', tracking=True, required=True)
    progress = fields.Integer(string="Progress", compute='_compute_progress')

    @api.depends('channel')
    def _compute_channel_id(self):
        for rec in self:
            rec.channel_id = rec.channel.id

    def _compute_number_of_attendees(self):
        for rec in self:
            rec.number_of_attendees = len(rec.channel.channel_last_seen_partner_ids)
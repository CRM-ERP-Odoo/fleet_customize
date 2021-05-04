
from odoo import fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    calendar_event_count = fields.Integer(compute='_invoice_calendar_event_count', string="Calendar Event Count")

    def _invoice_calendar_event_count(self):
        self.calendar_event_count = 0
        if not self.ids:
            return True

        for vehicle in self.filtered('id'):
            vehicle.calendar_event_count = len(self.env['calendar.event'].search([
                ('res_id', '=', vehicle.id),
                ('res_model', '=', 'fleet.vehicle'),
            ]))


from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vehicle_driver_ids = fields.One2many('fleet.vehicle', 'driver_id', string="Vehicles Driver")
    vehicle_future_driver_ids = fields.One2many('fleet.vehicle', 'future_driver_id', string="Vehicles Future Driver")
    vehicle_count = fields.Integer(compute='_invoice_vehicle_count', string="Vehicles Count", groups='fleet.fleet_group_user')

    def _invoice_vehicle_count(self):
        self.vehicle_count = 0
        if not self.ids:
            return True

        for partner in self.filtered('id'):
            partner.vehicle_count = len(partner.vehicle_driver_ids + partner.vehicle_future_driver_ids)

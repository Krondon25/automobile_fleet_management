# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Vehicle(models.Model):
    _name = "vehicle"
    _description = "Vehicle"
    _rec_name = 'vehicle_brand_id'

    vehicle_brand_id = fields.Many2one('vehicle.brand', string='Vehicle brands')
    vehicle_model_id = fields.Many2one('vehicle.models', string='Vehicle models')
    vehicle_color_id = fields.Many2one('vehicle.color', string='vehicle color')
    year = fields.Char(string='vehicle year')
    maintenance_ids = fields.One2many(
        'maintenance.service',
        'vehicle_id',
        'Maintenance Service',
    )

    mileage_id = fields.Many2one('mileage', string='mileage')
    mileage_porcentge_id = fields.Many2one(related='mileage_id.percentage_discount_id')
    purchase_price = fields.Integer(string='Purchase Price')
    purchase_date = fields.Date()
    current_price = fields.Integer(string='Current Price')
    percentage_discount_id = fields.Many2one('mileage.discount')
    quantity_service = fields.Integer(string='quantity of services', compute='_compute_maintenance', store=True)

    @api.onchange('percentage_discount_id')
    def _onchange_percentage_discount(self):
        """ vehicle mileage discount """
        for record in self:
            discount = (record.purchase_price * record.percentage_discount_id.percentage_discount) / 100
            record.current_price = record.purchase_price - discount



    @api.depends('maintenance_ids')
    def _compute_maintenance(self):
        """Automate maintenance services"""

        self.quantity_service = len(self.maintenance_ids)


class VehicleBrand(models.Model):
    _name = "vehicle.brand"

    _description = "brands"

    name = fields.Char()


class VehicleModels(models.Model):
    _name = "vehicle.models"

    _description = "models"

    name = fields.Char()


class VehicleColor(models.Model):
    _name = "vehicle.color"

    _description = "colors"

    name = fields.Char()

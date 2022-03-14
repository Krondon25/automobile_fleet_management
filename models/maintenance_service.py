# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MaintenanceService(models.Model):
    _name = "maintenance.service"

    _description = "Maintenance Service"

    service_id = fields.Many2one('service', string='Type Service')
    start_date = fields.Date(string='start date')
    price = fields.Integer(string="Price")
    vehicle_id = fields.Many2one('vehicle', string='Vehicle')


class Service(models.Model):
    _name = "service"

    _description = "Service"

    name = fields.Char()
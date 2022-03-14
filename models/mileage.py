# -*- coding: utf-8 -*-

from odoo import fields, models


class Mileage(models.Model):
    _name = "mileage"
    _description = "Mileage"

    name = fields.Char()
    quantity = fields.Integer(string='mileage quantity')
    percentage_discount_id = fields.Many2one('mileage.discount')


class MileageDiscount(models.Model):
    _name = "mileage.discount"
    _description = "Mileage discount"

    name = fields.Char()
    percentage_discount = fields.Integer(string='Percentaje discount')

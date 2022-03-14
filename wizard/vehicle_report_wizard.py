# -*- coding: utf-8 -*-

from odoo import api, fields, models


class VehicleReportWizard(models.TransientModel):
    _name = 'vehicle.report.wizard'
    _description = 'Generate report'

    purchase_date = fields.Date(required=True)
    

    def print_report(self):
        return self.env.ref('automobile_fleet_management.report_vehicle').report_action(self)

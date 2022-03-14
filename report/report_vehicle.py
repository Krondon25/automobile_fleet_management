from odoo import api, models, _


class VehicleReport(models.AbstractModel):
    _name = 'report.automobile_fleet_management.report_vehicle_templ'
    _description = 'vehicle Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        obj_wizard = self.env['vehicle.report.wizard'].browse(docids[0])
        docs = self.env['vehicle'].search([('purchase_date','=',obj_wizard.purchase_date)])
        
        return {
            'doc_model': 'vehicle',
            'docs': docs,
            }
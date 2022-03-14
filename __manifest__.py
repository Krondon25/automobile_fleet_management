# -*- coding: utf-8 -*-

{
    'name': 'Automobile Fleet Management',
    'version': '13.0.0',
    'author': 'krondon25',
    'summary': 'Automobile Fleet Management',
    'description': """ This module allows to have a control over the fleet of vehicles. """,
    
    'data': [
        'security/ir.model.access.csv',
        'demo/vehicle_data.xml',
        'demo/mileage_data.xml',
        'views/vehicle_views.xml',
        'views/mileage_views.xml',
        'wizard/vehicle_report_wizard.xml',
        'report/report_vehicle.xml',
    ],
    'installable': True,
    'auto_install': False
}

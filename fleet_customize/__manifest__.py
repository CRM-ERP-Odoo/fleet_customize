# -*- coding: utf-8 -*-
# Copyright © 2021 Oleksandr Komarov (https://modool.pro) <info@modool.pro>

{
    'name': 'Fleet customize',
    'summary': 'Fleet customize',
    'author': 'Oleksandr Komarov',
    'maintainer': 'info@modool.pro',
    'website': 'https://modool.pro',
    'license': 'LGPL-3',
    'category': 'Sales/CRM',
    'version': '14.0.1.0.5',
    'depends': [
        'fleet',
        'contacts',
    ],
    'data': [
        'data/ir_rule_data.xml',
        'security/ir.model.access.csv',
        'views/partner_views.xml',
        'views/fleet_vehicle_views.xml',
        'security/fleet.xml',
    ],
}

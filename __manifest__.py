# -*- coding: utf-8 -*-

{
    'name': 'Delivery Note',
    'version': '12.0.1.0.0',
    'summary': 'Delivery Note',
    'author': 'The256',
    'maintainer': 'The256',
    'company': 'The256',
    'website': 'https://the256.pro/',
    'depends': ['stock'],
    'demo': [],
    'data': [
        'views/report.xml',
		'views/stock.report_delivery_note_document.xml',
		'views/stock.report_deliverynote.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
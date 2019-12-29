# -*- coding: utf-8 -*-
#############################################################################
#
#              Zero For Information Systems.
#
#  Copyright (C) 2019-TODAY Zero Systems(<https://www.erpzero.com>).
#
#  Author:Zero Systems(<https://www.erpzero.com>).
#
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#############################################################################
{
    'name': 'Delivery Note',
    'version': '12.0.1.',
    'summary': 'Delivery Note',
    'description': """ Most of Restaurant and Retail Point of Sale needs as the following""" 
    'author': 'Zero Systems'
    'website': "https://www.erpzero.com",
    'company': 'Zero For Information Systems',
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
}

# -*- coding: utf-8 -*-

{
    'name': "POS Payment Operation Number",
    'version': '16.0.1.0.0',
    'summary': "Agrega un campo para ingresar el número de operación en el pago del POS",
    'category': 'Point of Sale',
    'author': "Tu Nombre / Empresa",
    'depends': ['base','point_of_sale'],
    'data': [
        'view/pos_payment_inherit_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'test_04/static/src/js/payment_screen_extension.js',
            'test_04/static/src/xml/payment_screen_extension.xml',

        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

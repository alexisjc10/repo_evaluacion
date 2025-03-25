# -*- coding: utf-8 -*-
{
    'name': 'Amount To Text',
    'description': """
        Convierte una cantidad monetaria a texto en la moneda correspondiente.
    """,
    'version': '1.0',
    'autor': 'Alexis Canchachi',
    'category': '',
    'depends': ['base', 'mail' ],
    'data': [
        'security/ir.model.access.csv',
        'view/menu_amount_to_text.xml',
        'view/amount_to_text_view.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

# -*- coding: utf-8 -*-
{
    'name': 'Account Invoice Inherit',
    'description': """
        Se añadio campo seleccionable (Boleta y Factura).
    """,
    'version': '1.0',
    'autor': 'Alexis Canchachi',
    'category': '',
    'depends': ['base', 'account'],
    'data': [
        'view/account_move_inherit.xml',
        'view/res_users_inherit_view.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

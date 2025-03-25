# -*- coding: utf-8 -*-
{
    'name': 'Validation SO',
    'description': """
        Validacion de stock de productos en orden de venta.
    """,
    'version': '1.0',
    'autor': 'Alexis Canchachi',
    'category': '',
    'depends': ['base', 'sale_management'],
    'data': [
        'view/res_config_settings_view.xml',
        # 'view/amount_to_text_view.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

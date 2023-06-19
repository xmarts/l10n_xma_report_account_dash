# -*- coding: utf-8 -*-
{
    'name': "reporte custom de facturas, ventas y compras",

    'summary': """""",

    'description': """
    """,

    'author': "XMARTS",
    'website': "",
    'category': 'Accounting',
    'version': '1.0.0',

    'depends': ['base', 'account'],

    'data': [
        'security/ir.model.access.csv',
        #'views/res_currency_rate_inherit.xml',
        'views/res_currency_inherit.xml',
    ],
}

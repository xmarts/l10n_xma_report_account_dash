# -*- coding: utf-8 -*-
{
    'name': 'Account Reports',
    'version': '16.0',
    'summary': "Account Reports",
    'sequence': 16,
    'description': """
                    Odoo Account Reports
                    """,
    'category': 'Accounting',
    'author': 'xmarts',
    'maintainer': 'xmarts',
    'website': '',
    'depends': ['account', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/account_report_view.xml',
        'reports/report.xml',
        'reports/account_report_template.xml',

             ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

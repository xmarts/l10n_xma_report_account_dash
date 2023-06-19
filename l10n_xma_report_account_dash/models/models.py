# -*- coding: utf-8 -*-
from datetime import timedelta
from itertools import groupby
from markupsafe import Markup

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.fields import Command
from odoo.osv import expression
from odoo.tools import float_is_zero, format_amount, format_date, html_keep_url, is_html_empty
from odoo.tools.sql import create_index
import logging
from odoo.addons.payment import utils as payment_utils

from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
# -*- coding: utf-8 -*-
from datetime import timedelta
from itertools import groupby
from markupsafe import Markup

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.fields import Command
from odoo.osv import expression
from odoo.tools import float_is_zero, format_amount, format_date, html_keep_url, is_html_empty
from odoo.tools.sql import create_index
import logging
from odoo.addons.payment import utils as payment_utils

from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

_logger = logging.getLogger(__name__)

class ReportAcountMove(models.Model):
    _name = "report.account.mod"
    
    move_id = fields.Many2one('account.move')
    move_report_id = fields.Many2one('report.account.modline')
    desde = fields.Date()
    hasta = fields.Date()
    
    def open_view_detail_helptime(self):
        return {
            'name': f"""Detalles""",
            'res_model': 'report.account.modline',
            'view_mode': 'tree,form',
            'target': 'current',
            # 'view_id': False,
            'view_id': self.env.ref('l10n_xma_report_account_dash.report_account_modline_tree').id,
            'views': [
                (self.env.ref('l10n_xma_report_account_dash.report_account_modline_tree').id, 'tree'),
               # (self.env.ref('treasury.treasury_lines_form').id, 'form'),
            ],
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', [lines.id for lines in self.move_id if self.desde >= lines.invoice_date and self.hasta <= lines.invoice_date])],
            #'context': {
              #  'group_by': ['partner_id']
            #}
        }
    
    
class ReportAcountMoveLine(models.Model):
    _name = "report.account.modline"
    
    move_id = fields.Many2one('account.move')
    move_report_id = fields.Many2one('report.account.mod')
    name=fields.Char()
    Date = fields.Date()
    partner_id = fields.Many2one('res.partner')
    amount = fields.Float()
    
    
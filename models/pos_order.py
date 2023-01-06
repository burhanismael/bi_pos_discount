# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = 'pos.order'

    discount_type = fields.Selection([('fixed', 'Fixed Discount'), ('percentage', 'Percentage Discount')],
                                     string='Discount Type', related='session_id.config_id.discount_type')

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_type = fields.Selection([('fixed', 'Fixed Discount'), ('percentage', 'Percentage Discount')],
                                     string='Discount Type', default='fixed')

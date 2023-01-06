# -*- coding: utf-8 -*-
# from odoo import http


# class BiPosDiscount(http.Controller):
#     @http.route('/bi_pos_discount/bi_pos_discount', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bi_pos_discount/bi_pos_discount/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bi_pos_discount.listing', {
#             'root': '/bi_pos_discount/bi_pos_discount',
#             'objects': http.request.env['bi_pos_discount.bi_pos_discount'].search([]),
#         })

#     @http.route('/bi_pos_discount/bi_pos_discount/objects/<model("bi_pos_discount.bi_pos_discount"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bi_pos_discount.object', {
#             'object': obj
#         })

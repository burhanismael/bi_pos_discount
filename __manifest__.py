# -*- coding: utf-8 -*-


{
    'name': "bi_pos_discount",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_discount_views.xml',
        'views/pos_order.xml',
    ],
    "assets": {
        'point_of_sale.assets': [
            ('replace', '/point_of_sale/static/src/js/models.js', '/bi_pos_discount/static/src/js/models.js'),
            ('replace', '/point_of_sale/static/src/js/Screens/ProductScreen/Orderline.js', '/bi_pos_discount/static/src/js/Screens/ProductScreen/Orderline.js'),
        ],
        'web.assets_qweb': [
            '/bi_pos_discount/static/src/xml/Screens/ProductScreen/Orderline.xml',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

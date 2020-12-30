# -*- coding: utf-8 -*-
{
    'name': "bista",

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
    'depends': ['base','mail','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/trainee.xml',
        'views/trainee_location.xml',
        'views/trainer.xml',
        'views/res_partner_views.xml',
        'views/hr_employee_views.xml',
        'views/subjects.xml',
        'views/topic.xml',
        'views/stages_view.xml',
        'views/batch_view.xml',
        'views/designation.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

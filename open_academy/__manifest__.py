# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Open Academy module to train odoo development""",

    'description': """
        Odoo 14 Development Tutorials,
        Open academy module for managing trainings:
        -Manage student enroll
        -Attendance registration
        -Trainer
        -Training sessions
        -Courses
        -More..
    """,

    'author': "Fede Herz",
    'website': "http://fhlabs.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',
    'version': '14.0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'website_slides'],
    'images': ['static/description/banner.gif'],

    # always loaded
    'data': [
        'data/slide_channel_data.xml',
        'data/slide_channel_data_v13.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

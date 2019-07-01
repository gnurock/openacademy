# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        ''
        'security/seguridad.xml',
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/partner.xml',
        'views/ejemplo_seguridad.xml',
        'wizard/maestro_wizard_view.xml',
        'views/vista_controller.xml',
        'views/maestro_vista_controller.xml',
        'report/reporte_maestro.xml',
        'report/reporte_maestro_template.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],

}


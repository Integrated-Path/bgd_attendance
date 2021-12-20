# -*- coding: utf-8 -*-
{
    'name': "Baghdad Hotel Attandance",

    'summary': """This report is to print a custom attandace report for Baghdad Hotel""",

    'author': "Integerated Path",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Attendances',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance', 'to_attendance_device'],

    # always loaded
    'data': [
        'data/custom_assets.xml',
        'report/to_attendance_device_report.xml',
        'report/attendance_report.xml',
        
    ],
}

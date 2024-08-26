{
    'name': 'Custom Stock Report',
    'version': '1.0',
    'category': 'Reporting',
    'description': 'Add a custom report to Stock Picking form',
    'depends': ['stock'],
    'data': [
        'report/stock_report_template.xml',
        'views/stock_picking_form_inherit.xml',
    ],
    'installable': True,
}

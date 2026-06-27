{
    'name': 'Kalibrasi Alat Kesehatan',
    'version': '19.0.1.0.0',
    'summary': 'Manajemen Kalibrasi Alat Kesehatan',
    'author': 'Fadly Muktafi (Junior Odoo Programmer)',
    'category': 'Inventory',
    'depends': ['base', 'product', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/kalibrasi_views.xml',
    ],
    'installable': True,
    'application': True,
}
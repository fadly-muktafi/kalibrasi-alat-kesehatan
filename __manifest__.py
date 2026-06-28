{
    'name': 'Kalibrasi Alat Kesehatan',
    'version': '19.0.1.0.0',
    'summary': 'Manajemen Kalibrasi Alat Kesehatan',
    'author': 'Fadly Muktafi (Junior Odoo Programmer)',
    'category': 'Healthcare',
    'depends': ['base', 'product', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'views/kalibrasi_views.xml',
    ],
    'installable': True,
    'application': True,
}
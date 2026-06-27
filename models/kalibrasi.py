from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class KalibrasiAlatKesehatan(models.Model):
    _name = 'kalibrasi.alat.kesehatan'
    _description = 'Manajemen Kalibrasi Alat Kesehatan'

    name = fields.Char(string='Kode Kalibrasi', default='Data Baru', copy=False, required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    product_id = fields.Many2one('product.product', string='Alat Kesehatan', required=True)
    no_seri = fields.Char(string='Nomor Seri Alat', required=True)
    technician_id = fields.Many2one('hr.employee', string='Teknisi Kalibrasi', required=True)
    tanggal_kalibrasi = fields.Date(string='Tanggal Kalibrasi')
    interval_bulan = fields.Integer(string='Interval (Bulan)', default=12)
    tanggal_berikutnya = fields.Date(string='Jatuh Tempo Kalibrasi', compute='_compute_tanggal_berikutnya', store=True)
    hasil = fields.Selection([
        ('approved', 'Lulus'),
        ('rejected', 'Tidak Lulus'),
    ], string='Hasil Kalibrasi')
    catatan = fields.Text(string='Catatan Tambahan')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('process', 'Mengkalibrasi'),
        ('done', 'Terkalibrasi'),
        ('expired', 'Kadaluarsa'),
    ], string='Status', default='draft', tracking=True)
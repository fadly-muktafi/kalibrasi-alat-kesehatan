from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class KalibrasiAlatKesehatan(models.Model):
    _name = 'kalibrasi.alat.kesehatan'
    _description = 'Manajemen Kalibrasi Alat Kesehatan'
    _order = 'jatuh_tempo desc'
    _rec_name = 'name'

    name = fields.Char(string='Kode Kalibrasi', default='Data Baru', copy=False, required=True)
    product_id = fields.Many2one('product.product', string='Alat Kesehatan', required=True)
    model_alat = fields.Char(string='Model Alat', required=True)
    no_seri = fields.Char(string='No. Seri', required=True)
    technician_id = fields.Many2one('hr.employee', string='Teknisi', required=True)
    kalibrasi_mulai = fields.Date(string='Kalibrasi Mulai')
    kalibrasi_selesai = fields.Date(string='Kalibrasi Selesai')
    interval = fields.Integer(string='Interval (Bulan)', default=12)
    jatuh_tempo = fields.Date(string='Jatuh Tempo', compute='_compute_jatuh_tempo', store=True)
    catatan = fields.Text(string='Catatan Tambahan')
    hasil = fields.Selection([
        ('approved', 'Lolos'),
        ('rejected', 'Gagal'),
    ], string='Hasil Kalibrasi')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('process', 'Mengkalibrasi'),
        ('done', 'Terkalibrasi'),
        ('expired', 'Kadaluwarsa'),
    ], string='Status', default='draft', tracking=True)

    @api.depends('kalibrasi_selesai', 'interval')
    def _compute_jatuh_tempo(self):
        for record in self:
            if record.kalibrasi_selesai:
                record.jatuh_tempo = record.kalibrasi_selesai + relativedelta(months=record.interval)
            else:
                record.jatuh_tempo = False
    
    def action_process(self):
        self.kalibrasi_mulai = fields.Date.today()
        self.status = 'process'

    def action_approved(self):
        self.kalibrasi_selesai = fields.Date.today()
        self.hasil = 'approved'
        self.status = 'done'

    def action_rejected(self):
        self.kalibrasi_selesai = fields.Date.today()
        self.hasil = 'rejected'
        self.status = 'done'
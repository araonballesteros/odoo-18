from odoo import models, fields

class TourBooking(models.Model):
    _name = 'tour.booking'
    _description = 'Reserva de Paquete Turístico'

    name = fields.Char(string='Referencia', required=True)
    notes = fields.Text(string='Notas')
from odoo import models, fields, api

class TourBooking(models.Model):
    _name = 'tour.booking'
    _description = 'Reserva de Paquete Turístico'

    name = fields.Char(string='Referencia', required=True, default='New')
    notes = fields.Text(string='Notas')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('tour.booking') or '/'
        return super().create(vals)

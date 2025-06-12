# -*- coding: utf-8 -*-
{
    'name': 'Reservas de Paquetes Turisticos',
    'version': '1.0',
    'summary': 'Reserva y venta de paquetes turisticos integrados con Website, Ecommerce, Facturacion y Portal',
    'description': """
Gestiona reservas y ventas de paquetes turisticos, integrando catalogo, reservas, pagos y portal de clientes.
""",
    'author': 'Desarrollador IA - Odoo 18 CE',
    'website': 'http://localhost:8069',
    'category': 'Sales',
    'depends': [
        'base', 'website', 'sale_management', 'account', 'calendar', 'contacts', 'portal'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/tour_booking_views.xml',
        'data/tour_booking_sequence.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
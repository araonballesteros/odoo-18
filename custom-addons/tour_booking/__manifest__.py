# -*- coding: utf-8 -*-
{
    'name': 'Reservas de Paquetes Turísticos',
    'version': '1.0',
    'summary': 'Gestion básica de reservas de paquetes turísticos sin integración con Website ni Ecommerce',
    'description': """
Permite gestionar reservas de paquetes turísticos de forma sencilla. Aún no integra catálogo en línea ni comercio electrónico.

Para conocer el plan de integración futura con Website y Ecommerce consulte `docs/website_ecommerce_integration.md`.
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

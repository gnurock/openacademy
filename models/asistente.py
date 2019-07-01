

from odoo  # -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

# Hereda  de maestro
class asistente(models.Model):
    _name = 'openacademy.asistente'
    _description = 'Clase asistente'
    _inherit = "openacademy.maestro"

    jefe = fields.Char(
        string='',
        size=64,
        required=False,
        readonly=False,
        defaults={:False}
        )


# -*- coding: utf-8 -*-
from odoo import models, fields, api


class asistenteEstudiante(models.Model):
    _name = 'maestro.wizard'

    def _get_default_students(self):

        return self.env['openacademy.maestro'].browse(self.env.context.get('active_ids'))

    maestro_ids = fields.Many2many('openacademy.maestro', string='maestro', default=_get_default_students)
    #level = fields.Char('Level')

    nombre=fields.Char(string='nombre')

    @api.multi
    def set_maestro_salario(self):
        for record in self:
            if record.maestro_ids:
                for maestro in record.maestro_ids:
                    maestro.nombre = self.nombre

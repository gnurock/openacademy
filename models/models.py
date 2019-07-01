# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api
from openerp.exceptions import ValidationError,except_orm
import inspect
import logging
import os

directorioActual = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
rutaProyecto = os.path.dirname(directorioActual)

logging.basicConfig(filename=rutaProyecto+"/logs/openacademy_log.log",level=logging.DEBUG)


class openacademy(models.Model):
    _name = 'openacademy.alumno'
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

# DEFAULT_SERVER_DATETIME_FORMAT = "%Y-%m-%d"

class Course(models.Model):
    _name = 'openacademy.course'
    name = fields.Char(string= "Title",requiered =True)
    description = fields.Text()


class Maestro(models.Model):
    _name = 'openacademy.maestro'
    _rec_name = 'nombre'
    numero_empleado = fields.Char(required=True, size=10, store=True, help="Capu")
    nombre = fields.Char(string="Nombre", required=True, size=50)
    foto = fields.Binary(String="Foto")
    ap_paterno = fields.Char(
         string='Apellido Paterno',
         required=True,
    )
    ap_materno = fields.Char(
        string='Apellido Materno',
        required='True',
    )
    # ap_paterno = fields.Char(String= "Apellido Paterno", required=True,size=50, )
    fecha_nacimiento = fields.Date(
         string='Fecha Nacimiento',
    )

    horas_clase = fields.Integer(string='Horas de clase semanales',required=True)
    # Al momento de utilizar un compute requiere usar un store para no iontente hacer calculos  en todos los campposs
    # salario = fields.Char(string='Salario',compute='_value_pc',store=True)
    salario = fields.Char(string='Salario Semanal')
    aula = fields.Integer()
    nivel_sni=fields.Integer()
    sexo = fields.Selection(selection=[('M', 'M'), ('F', 'F')])
    description = fields.Text()
    asignatura_ids = fields.One2many('openacademy.asignatura', 'maestro')
     # numero_empleado=fields.
     # numero_empleado=fields.Many2many('openacademy.asignatura','clavePr')
###


    @api.constrains('nombre','ap_paterno','ap_materno')
    def check_name(self):
        print "check_name"
        # logging.info("REVIASA DECORADOR");
        regex = r"([a-zA-Z]+)"
        regexnum=r"([0-9]+)"
        for rec in self:
            # here i forced that the name should start with alphabets if it's not the case remove ^[a-zA-Z]
            # and just keep:  re.match(r"[ a-zA-Z]+", rec.name)
            if rec.nombre and rec.ap_paterno and rec.ap_materno:
                if not re.search(regex,rec.nombre) or re.search(regexnum,rec.nombre):
                # print "error"
                    raise except_orm('Nombre no valido, no use nùmeros ni càracteres espececiales')
                if not re.match(regex, rec.ap_paterno) or re.search(regexnum,rec.nombre):
                    raise except_orm('Apellido Paterno no vàlido, no use nùmeros ni càracteres espececiales')
                if not re.match(regex, rec.ap_materno) or re.search(regexnum,rec.nombre):
                    raise except_orm('Apellido materno no vàlido')
            else:
                raise except_orm('Ingrese todos los campos obligatorios')



    @api.multi
    def imprimir_reporte(self):
        return self.env['report'].get_action(self, 'openacademy.reporte_maestro_template')

##


     ##
    @api.depends('horas_clase')
    def _value_pc(self):
        #logging.info("Calculo salario")
        self.salario = float(self.horas_clase) *120

    @api.onchange('horas_clase')
    def validar_hoas_clase(self):
        if self.horas_clase:
            if self.horas_clase <10 or self.horas_clase>150 :
                #print "Edad no valida"
                self.horas_clase = 0
                raise except_orm('Error', 'Debe tener como minimo 10 horas de clase y como maximo 150 horas')

     # @api.depends('nombre')
     # def _obtener_numero_empleado(self):
     # self.numero_empleado=str(self.nombre)
        # from datetime import datetime
        # for record in self:
        # date = record.fecha_nacimiento
        # self.numero_empleado = datetime.strptime(date, DEFAULT_SERVER_DATETIME_FORMAT)

class Asignatura(models.Model):
    _name = 'openacademy.asignatura'
    _rec_name = 'nombre'
    _description = 'Description'
    #clave=fields.Char(string='Clave',size=10,required=True)

    nombre = fields.Char(
        string='',
        size=64,
        required=False,
        readonly=False,
        defaults=False
        )
    #claveAl = fields.Many2many('openacademy.alumno','numero_matricula')
    maestro = fields.Many2one('openacademy.maestro', string='Maestro')
    # clavePr = fields.One2many('openacademy.maestro','numero_empleado')


class Alumno(models.Model):
    _name = 'openacademy.alumno'
    _rec_name = 'numero_matricula'
    numero_matricula = fields.Char(string = "Matricula", required=True,size=10)
    nombre =fields.Char(string="Nombre",requiered=True,size=100)
    ap_paterno=fields.Char(string="Apellido Paterno",requiered=True,size=50)
    ap_materno=fields.Char(string="Apellido materno",requiered=True,size=50)
    fecha_nacimiento = fields.Date(
        string='Fecha de Nacimiento'
    )


    #asignatura=fields.Char(string="Asignatura", size=20)
    #grupo=fields.Char(string="Grupo",size=2)

    grupo= fields.Many2one('openacademy.grupo','grupo_ids')
    asignatura= fields.Many2many('openacademy.asignatura','claveAL')
    #field_id = fields.Many2one('openacademy.users')
    #field_id = fields.Many2one(comodel_name='res.users')


class Grupo(models.Model):
    _name = 'openacademy.grupo'
    _description = 'Description'
    _rec_name='aula'
    # clave=fields.Char(String="Clave",size=10,required=True)
    aula = fields.Char(
        string='Aula',
        size=2,
        required=True,
        readonly=False,
        defaults=False
        )
    # field_ids = fields.One2many('res.users', 'rel_id')
    grupo_ids = fields.One2many('openacademy.alumno', 'numero_matricula')


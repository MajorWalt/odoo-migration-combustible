# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Sale Methods

class MetodoVenta(models.Model):    
    _name = "servicentro.metodoventa"
    _description = "Nomenclador de los Metodos Ventas"
    _rec_name = 'descripcion'

    metodo = fields.Integer(string='Número Identificacion', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    estado = fields.Boolean(string='Estado', required=True)
    cliente = fields.Char(string='Cliente', required=True)


sql_constraints = [
        ('name_code_uniq', 'unique(metodo)', '¡El numero identifcacion debe ser único y no se puede repetir!')
    ]
    
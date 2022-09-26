# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Classification of Cards

class Tarjetas(models.Model):    
    _name = "servicentro.tarjeta"
    _description = "Nomenclador de las classificaciones de tarjetas"
    _rec_name = 'descripcion'

    classificacion = fields.Integer(string='Clasificación de tarjeta', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    state = fields.Boolean(string='Estado', required=False)
    


sql_constraints = [
        ('name_code_uniq', 'unique(classificacion)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
    
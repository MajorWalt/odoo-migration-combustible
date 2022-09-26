# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Classification of Cards

class Tarjetas(models.Model):    
    _name = "servicentro.idtarjeta"
    _description = "Nomenclador de tipos de ID tarjetas"
    _rec_name = 'nombre'

    tipotarjeta = fields.Integer(string='Clasificación de Tarjeta', required=True)
    nombre = fields.Char(string='Descripción', required=False)
    state = fields.Boolean(string='Estado', required=False)
    tipo = fields.Selection([
        ('B', 'banda'),
        ('c', 'Chip'),
            ], required=True, default='B')


sql_constraints = [
        ('name_code_uniq', 'unique(tipotarjeta)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
    
# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Classification of Cards

class TipoPaga(models.Model):    
    _name = "servicentro.tipopaga"
    _description = "Nomenclador de los Tipos de Paga"
    _rec_name = 'tipo_pago'

    tipo_pago = fields.Char(string='Clasificación de tarjeta', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    signo = fields.Selection([
        ('positivo', '+'),
        ('negativo', '-'),
            ], required=False, default='positivo')
    trans = fields.Char(string='Trans', required=False)
    totalizer = fields.Char(string='Totalizer', required=False)
    no_orden = fields.Char(string='No-Orden', required=False)
    state = fields.Boolean(string='Estado', required=False)
    


sql_constraints = [
        ('name_code_uniq', 'unique(tipo_pago)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
    
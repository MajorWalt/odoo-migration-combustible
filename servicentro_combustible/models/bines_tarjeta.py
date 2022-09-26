# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Classification of Cards

class BinesTarjeta(models.Model):    
    _name = "servicentro.binestarjeta"
    _description = "Nomenclador de los Bines de la Tarjeta"
    _rec_name = 'bin'

    bin = fields.Char(string='Bin de tarjeta', required=True)
    long = fields.Integer(string='Número de Longitud', required=False)
    descripcion = fields.Char(string='Descripción', required=True)
    clase = fields.Integer(string='Clase', required=False)
    tipo_idtarjeta = fields.Many2one('servicentro.idtarjeta', string='Tipo de Tarjeta', required=True)
    tipo_pago = fields.Many2one('servicentro.tipopaga', string='Tipo de Pago', required=True)
    metodo_venta = fields.Many2one('servicentro.metodoventa', string='Método de Venta', required=True)
    state = fields.Boolean(string='Estado', required=False)
    
sql_constraints = [
        ('name_code_uniq', 'unique(bin)', '¡El bin debe ser único y no se puede repetir!')
    ]
    
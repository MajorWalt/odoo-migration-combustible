# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Surtidor

class Servicio(models.Model):    
    _name = "servicentro.servicio"
    _description = "Los Servicios"
    _rec_name = 'Nid'

    Nid = fields.Integer(string='Identificador del Servicio', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    tipo_combustible = fields.Many2one('product.template', string='Tipo de Combustible')
    codigo = fields.Float(string='Código',size = 13, digits=(13,0)  ,required=False)
    id_producto = fields.Char(string='Identificador del Producto', required=False)
    state = fields.Boolean(string='Estado', required=True)
   



sql_constraints = [
        ('name_code_uniq', 'unique(descripcion)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
sql_constraints = [
        ('name_code_uniq', 'unique(Nid)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
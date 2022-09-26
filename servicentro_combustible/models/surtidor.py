# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Surtidor

class Surtidor(models.Model):    
    _name = "servicentro.surtidor"
    _description = "Los Surtidores"
    _rec_name = 'Nid'

    Nid = fields.Integer(string='Tipo de Surtidor', required=True)
    localidad = fields.Char(string='Localidad del Surtidor', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    ubicacion = fields.Char(string='Ubicación', required=False)
    tipo_combustible = fields.Many2one('product.template', string='Tipo de Combustible', required=True)
    state = fields.Boolean(string='Estado', required=False)
    image = fields.Binary(string="Imagen")



sql_constraints = [
        ('name_code_uniq', 'unique(descripcion)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
    
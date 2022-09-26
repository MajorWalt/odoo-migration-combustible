# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for Surtidor

class Operacion(models.Model):    
    _name = "servicentro.operacion"
    _description = "Las Operaciones"
    _rec_name = 'Nid'

    Nid = fields.Integer(string='Identificador de Operaciones', required=True)
    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
   



sql_constraints = [
        ('name_code_uniq', 'unique(name)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
    
# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for pos

class POS(models.Model):    
    _name = "servicentro.pos"
    _description = "Nomenclador de POS"
    _rec_name = 'idabo'

    id_pos = fields.Char(string='Código de Identificación del POS', required=True)
    idabo = fields.Integer(string='Idabo de POS', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    chapilla = fields.Float(string='Chapilla del POS',size = 10, digits=(10,0)  ,required=False)
    caja = fields.Char(string='Caja del POS', required=True)
    descripcioncaja = fields.Char(string='Descripción de la Caja', required=True)
    

sql_constraints = [
        ('name_code_uniq', 'unique(id_pos)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]
    
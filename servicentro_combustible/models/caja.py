# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools


## Database table creation for caja

class Caja(models.Model):    
    _name = "servicentro.caja"
    _description = "Nomenclador de Caja"
    _rec_name = 'descripcion'

    caja_no = fields.Char(string='Código identificación de la caja', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    red = fields.Char(string='Red de la caja', required=True)
    no_dev = fields.Char(string='No DEV', required=False)
    dir_com = fields.Char(string='DIR COM', required=False)
    puerto_ent = fields.Char(string='Puerto Ent', required=False)
    puerto_sal = fields.Char(string='Puerto Sal', required=False)
    

sql_constraints = [
        ('name_code_uniq', 'unique(caja_no)', '¡El NI de la caja debe ser único y no se puede repetir!')
    ]
    
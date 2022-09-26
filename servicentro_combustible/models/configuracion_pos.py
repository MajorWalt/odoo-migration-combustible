# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools

## Database table creation for POS Configuracion


class ConfiguracionPOS(models.Model):
    _name = "servicentro.configuracionpos"
    _description = "Configuracion de POS"
    _rec_name = 'id_conf'

    id_conf = fields.Char(string='Código de Identificación', required=True)
    nombre = fields.Char(string='Nombre del POS', required=True)
    path = fields.Char(string='Path al fichero de datos', required=False)
    localidad = fields.Char(string='Localidad del POS', required=False)
    red = fields.Char(string="Red del POS",required = True)
    estado = fields.Boolean(string="Estado del POS",required = True)


sql_constraints = [
        ('name_code_uniq', 'unique(id_conf)', '¡El codigo del POS debe ser único y no se puede repetir!')
    ]
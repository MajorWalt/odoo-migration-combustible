# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools

## Database table creation for Combustible


  
class Combustible(models.Model):    
    _name = "servicentro.combustible"
    _description = "Tipo de combustibles"
    _rec_name = 'descripcion'

    Nid = fields.Integer(string='Tipo de Combustible', required=True)
    nombre = fields.Char(string='Código del Combustible', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    state = fields.Boolean(string='Estado', required=False)
    image = fields.Binary(string="Imagen")
    color = fields.Integer(string = "Color")



class CombustibleInherited(models.Model):    
   ## _name = "servicentro.combustible"
    _inherit = "product.template"
   ## _description = "Tipo de combustibles"
    _rec_name = 'Nid'

    Nid = fields.Integer(string='Tipo de Combustible', required=True)
    nombre = fields.Char(string='Código del Combustible', required=True)
    descripcion = fields.Char(string='Descripción', required=False)
    state = fields.Boolean(string='Estado', required=False)
    image = fields.Binary(string="Imagen")
    color = fields.Integer(string = "Color")


sql_constraints = [
       ('name_code_uniq', 'unique(nombre)', '¡El nombre del combustible debe ser único y no se puede repetir!')
    ]

sql_constraints = [
        ('name_code_uniq', 'unique(Nid)', '¡El nombre de la identificacion numero del combustible debe ser único y no se puede repetir!')
    ]    



class ReporteCombustibles(models.Model):
    _name = "reporte.combustibles"
    _auto = False
    _description = 'Reporte de los combustibles del servicentro'
    
    Nid = fields.Integer('Tipo de Combustible')
    nombre = fields.Char('Código del Combustible')
    descripcion = fields.Char('Descripción')
    state = fields.Boolean('Estado')
    image = fields.Binary("Imagen")
    color = fields.Integer("Color")
    

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'reporte_combustibles')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW reporte_combustibles AS (
                SELECT
                    row_number() OVER () AS id,
                    line.nombre,
                    line.descripcion,
                    line.state,
                    line.color
                     FROM (
                        SELECT *
                        	FROM product_product ) as line
                   )""")

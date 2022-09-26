# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools

class ReporteVentasPOS(models.Model):
    _name = 'ventas.reporte'
    _auto = False
    _description = 'Reporte de las ventas del servicentro'
    
    
    precio = fields.Integer('Precio')
    fecha_oper = fields.Date('Fecha')
    ticket = fields.Integer('Ticket')
    descripcion = fields.Char(string='Descripción')
    

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'ventas_reporte')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW ventas_reporte AS (
                SELECT
                    row_number() OVER () AS id,
                    line.tipo_oper,
                    line.fecha_oper,
                    line.precio,
                    line.ticket,
                    line.descripcion FROM (
                        SELECT
                            sa.tipo_oper as tipo_oper,
                            sa.fecha_oper as fecha_oper,
                            sa.precio as precio,
                            sa.ticket as ticket,
                            o.descripcion as descripcion
                        	FROM servicentro_azucena sa
                        LEFT JOIN servicentro_operacion o ON (sa.tipo_oper = o.id)) as line
                   
                )""")

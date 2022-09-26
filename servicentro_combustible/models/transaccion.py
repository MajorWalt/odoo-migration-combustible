# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools

## Database table creation for Combustible


class Azucena(models.Model):    
    _name = "servicentro.azucena"
    _description = " Las operaciones del POS provenientes de Autogara "
    _rec_name = 'ticket'
   
    turno = fields.Date(string='Turno', required=True)   
    localidad = fields.Many2one('servicentro.configuracionpos',string='Localidad', required=True)   
    idabo = fields.Many2one('servicentro.pos',string='Idabo', required=True)
    codigo_op = fields.Integer(string='Codigo OP', required=True)
    tipo_oper = fields.Many2one('servicentro.operacion',string='Tipo de Operación', required=True)
    brazo = fields.Many2one('servicentro.surtidor',string='Surtidor/Brazo', required=True)
    bin = fields.Many2one('servicentro.binestarjeta',string='Bin de tarjeta', required=True)
    ticket = fields.Integer(string='Ticket', required=True)
    no_oper = fields.Integer(string='No_Oper', required=True)
    fecha_cad = fields.Integer(string='Fecha_Cad', required=True)
    servicio = fields.Many2one('servicentro.servicio',string='Servicio', required=True)
    fecha_oper = fields.Date(string='Fecha_Oper', required=True)
    hora = fields.Integer(string='Hora', required=True)
    precio = fields.Integer(string='Precio', required=True)
    saldo = fields.Integer(string='Saldo', required=True)
    precioXunit = fields.Integer(string='Precio por Unit', required=True)
    moneda = fields.Integer(string='Moneda', required=True)
    tasa = fields.Integer(string='Tasa', required=True)
    paidamt = fields.Integer(string='Paid Amount', required=True)




sql_constraints = [
        ('name_code_uniq', 'unique(no_oper)', '¡El nombre de la transaccion debe ser único y no se puede repetir!')
    ]

def fichero(self):
    print("Works")
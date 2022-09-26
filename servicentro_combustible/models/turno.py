# -*- coding: utf-8 -*-

from email.policy import default
from operator import index
from odoo import api, fields, models, _, tools
from datetime import datetime
from tkinter import filedialog
import tkinter as tk

## Database table creation for Combustible


class Azucena(models.Model):    
    _name = "servicentro.turno"
    _description = " Los turnos"
    
    
    fecha_oper = fields.Date(string='Fecha_Oper', required=True)
    localidad = fields.Char(string='Localidad', required=True)


    #api.onchange('fecha_oper','localidad')
    #def onchange_fecha_oper(self):
    #date = self.fecha_oper.strftime("%m/%d/%Y")

    #self.key = "TEST" 
    #
    
    def generate_coupon_function(self):
       
        print("WORKS")
        
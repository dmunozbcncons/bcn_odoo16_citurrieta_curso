# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Informacion del curso'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Descripción')
    level = fields.Selection(string='Level',selection = [('beginer','Beginer'),('intermediate','Intermediate'),('advanced','Advanced')], copy=False)
    activate = fields.Boolean(string='Activate',default=True)
    
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = "res.users"

    user_edit = fields.Boolean(string="Puede Editar Tipo de Factura", default=False)


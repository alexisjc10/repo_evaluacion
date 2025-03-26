# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    allow_confirm_without_stock = fields.Boolean(
        string="Permitir Confirmar sin Stock",
        config_parameter="sale.allow_confirm_without_stock"
    )


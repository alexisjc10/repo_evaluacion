from odoo.exceptions import ValidationError
from odoo import models, fields, _, api



class PosPayment(models.Model):
    _inherit = 'pos.payment'

    operation_number = fields.Char(string="Número de Operación")

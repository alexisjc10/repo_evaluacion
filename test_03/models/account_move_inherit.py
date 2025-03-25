from odoo.exceptions import ValidationError
from odoo import models, fields, _, api


class AccountMove(models.Model):
    _inherit = "account.move"

    type_document = fields.Selection([
        ('ticket', 'Boleta'),
        ('invoice', 'Factura')], string='Tipo de Documento')


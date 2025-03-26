from odoo.exceptions import ValidationError
from odoo import models, fields, _, api


class AccountMove(models.Model):
    _inherit = "account.move"

    type_document = fields.Selection([
        ('ticket', 'Boleta'),
        ('invoice', 'Factura')], string='Tipo de Documento')

    @api.onchange('type_document')
    def _onchange_type_document(self):
        user = self.env.user
        if user.user_edit == False:
            raise ValidationError(_("No tiene permisos para realizar esta accion"))



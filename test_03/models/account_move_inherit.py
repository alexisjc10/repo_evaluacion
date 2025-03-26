from odoo.exceptions import ValidationError
from odoo import models, fields, _, api


class AccountMove(models.Model):
    _inherit = "account.move"

    type_document = fields.Selection([
        ('ticket', 'Boleta'),
        ('invoice', 'Factura')], string='Tipo de Documento')

    edit_type_document = fields.Boolean(string="Puede Editar Tipo de Documento", default=False, compute="_compute_edit_type_document")

    def _compute_edit_type_document(self):
        for record in self:
            user = self.env.user
            record.edit_type_document = user.user_edit

    @api.onchange('type_document')
    def _onchange_type_document(self):
        for record in self:
            user = self.env.user
            record.edit_type_document = user.user_edit




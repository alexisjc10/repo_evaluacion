from odoo.exceptions import ValidationError
from odoo import models, fields, _, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        # Obtener configuración global de ventas
        allow_confirm_without_stock = self.env["ir.config_parameter"].sudo().get_param(
            "sale.allow_confirm_without_stock")

        # Convertir el valor en booleano (ya que get_param devuelve string)
        if allow_confirm_without_stock == 'True':
            return super(SaleOrder, self).action_confirm()

        # Si la opción no está activada, aplicar validación de stock
        for rec in self:
            for line in rec.order_line:
                if line.product_id.free_qty <= line.product_uom_qty:
                    raise ValidationError(
                        _("No hay stock suficiente para el producto: %s") % line.product_id.display_name)

        return super(SaleOrder, self).action_confirm()

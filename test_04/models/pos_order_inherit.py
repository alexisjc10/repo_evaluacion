# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class PosOrder(models.Model):
    _inherit = "pos.order"

    def _process_payment_lines(self, order, order_data, pos_session, draft):
        """Guarda el número de operación en pos.payment dentro de `order_data.payment_ids`."""
        res = super()._process_payment_lines(order, order_data, pos_session, draft)

        # Verifica que se esté recibiendo `payment_ids`
        if "payment_ids" not in order_data or not order_data["payment_ids"]:
            print("`order_data.payment_ids` no existe o está vacío.")
            return res

        for payment_data in order_data["payment_ids"]:
            # Llama al método para obtener el número de operación
            operation_number = self.update_payment_operation_numbers([payment_data])

            payment_id = payment_data.get("id")
            if not payment_id:
                print("`payment_id` no encontrado en `payment_data`.")
                continue

            # Buscar el pago en la base de datos
            payment = self.env["pos.payment"].search([
                ("pos_order_id", "=", order.id),
                ("id", "=", payment_id)
            ], limit=1)

            if payment and operation_number:
                payment.write({"operation_number": operation_number})
                print(f"Número de operación guardado en pos.payment ID {payment.id}: {operation_number}")
            else:
                print(f"No se encontró pos.payment para Order ID {order.id} y Payment ID {payment_id}")

        return res

    @api.model
    def update_payment_operation_numbers(self, payment_data):
        """Devuelve el último número de operación de la lista de pagos sin modificar nada."""
        if not isinstance(payment_data, list) or not payment_data:
            print("Los datos de pago no son válidos.")
            return None  # Devuelve None si no hay datos válidos

        last_operation_number = None  # Variable para almacenar el último número de operación encontrado

        for payment in payment_data:
            operation_number = payment.get("operation_number")
            if operation_number:
                last_operation_number = operation_number  # Guarda el último número de operación encontrado

        return last_operation_number

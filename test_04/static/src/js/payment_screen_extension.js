/** @odoo-module **/
import { useState } from "@odoo/owl";
const Registries = require("point_of_sale.Registries");
const PaymentScreen = require("point_of_sale.PaymentScreen");
import rpc from "web.rpc";

const ReferenceButtonPaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
        setup() {
            super.setup();
            this.state = useState({ operationNumber: "" });
            this.syncOperationNumber();
        }

        syncOperationNumber() {
            let order = this.env.pos.get_order();
            if (!order) {
                console.warn("No hay orden activa.");
                return;
            }

            let paymentline = order.selected_paymentline;
            if (paymentline) {
                this.state.operationNumber = paymentline.operation_number || "";
                console.log("Número de operación sincronizado:", this.state.operationNumber);
            } else {
                console.warn(" No hay línea de pago seleccionada.");
            }
        }

        onInputChange(event) {
            let value = event.target.value.trim();
            this.state.operationNumber = value;
            console.log("Capturando entrada del usuario:", value);

            let order = this.env.pos.get_order();
            let paymentline = order ? order.selected_paymentline : null;

            if (paymentline) {
                paymentline.operation_number = value;
                console.log("Número de operación guardado en la línea de pago:", paymentline.operation_number);
            } else {
                console.warn("No se encontró línea de pago para almacenar el número.");
            }
        }

        async _finalizeValidation() {
    let order = this.env.pos.get_order();
    if (!order) {
        console.warn(" No hay orden para validar.");
        return super._finalizeValidation(...arguments);
    }

    let payment_data = [];
    order.paymentlines.forEach((payment) => {
        if (!payment.operation_number && this.state.operationNumber) {
            payment.operation_number = this.state.operationNumber;
        }

        // Asegurar que `payment.id` tenga un valor válido antes de enviarlo
        let payment_id = payment.id || payment.cid;

        if (payment_id && payment.operation_number) {
            payment_data.push({
                //order_id: order.server_id || order.id, // ID de la orden en el backend
                order_id: order.id, // ID de la orden en el backend
                payment_id: payment_id, // ID del pago (real o temporal)
                operation_number: payment.operation_number,
            });
        }
    });

    console.log("Datos de pagos antes de enviar:", payment_data);

    if (payment_data.length > 0) {
        await rpc.query({
            model: "pos.order",
            method: "update_payment_operation_numbers",
            args: [payment_data],
        }).then(() => {
            console.log(" Números de operación guardados correctamente.");
        }).catch((error) => {
            console.error(" Error al guardar en la orden:", error);
        });
    }

    return super._finalizeValidation(...arguments);
}

    };

Registries.Component.extend(PaymentScreen, ReferenceButtonPaymentScreen);

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from num2words import num2words


class AmountToText(models.Model):
    _name = "amount.to.text"
    _description = "Amount To Text"
    _inherit = ['mail.thread']


    amount = fields.Monetary(string="Monto", tracking=True)
    currency_id = fields.Many2one("res.currency", string="Moneda", tracking=True)
    amount_text = fields.Char(string="Monto en letras", compute="_compute_amount_text", tracking=True)

    @api.depends("amount", "currency_id")
    def _compute_amount_text(self):
        for record in self:
            record.amount_text = self.amount_to_text(record.amount, record.currency_id)

    def amount_to_text(self, amount, currency):
        """ Convierte una cantidad monetaria a texto en la moneda correspondiente. """
        parte_entera = int(amount)
        parte_decimal = round((amount - parte_entera) * 100)

        texto_entero = num2words(parte_entera, lang='es').capitalize()
        texto_decimal = f"{parte_decimal:02d}/100"
        moneda = currency.name
        return f"{texto_entero} con {texto_decimal} {moneda}"

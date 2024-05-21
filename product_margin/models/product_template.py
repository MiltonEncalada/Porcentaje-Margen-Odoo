from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    margin_percentage = fields.Float(string='Margen de Ganancia (%)', compute='_compute_margin_percentage')

    @api.depends('list_price', 'standard_price')
    def _compute_margin_percentage(self):
        for product in self:
            if product.list_price:
                product.margin_percentage = ((product.list_price - product.standard_price) / product.list_price) * 100
            else:
                product.margin_percentage = 0

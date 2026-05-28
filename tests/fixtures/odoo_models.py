"""Sample Odoo-style models for testing inheritance extraction."""

from odoo import models, fields


class SaleOrderBase(models.Model):
    _name = 'sale.order'

    name = fields.Char()


class SaleOrderExtension(models.Model):
    _inherit = 'sale.order'

    extra = fields.Boolean()


class ResPartner(models.Model):
    _inherit = ['res.partner', 'mail.thread']
    _inherits = {'res.company': 'company_id'}

    points = fields.Integer()

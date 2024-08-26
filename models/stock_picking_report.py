from odoo import models

class StockPickingReport(models.Model):
    _inherit = 'stock.picking'

    def action_report_stock_picking_test(self):
        # Llamamos directamente al reporte sin abrir la interfaz de branding
        return self.env.ref('custom_stock_report.action_report_stock_picking_test').with_context(disable_report_customization=True).report_action(self)

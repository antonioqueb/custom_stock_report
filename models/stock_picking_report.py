from odoo import models

class StockPickingReport(models.Model):
    _inherit = 'stock.picking'

    def action_report_stock_picking_test(self):
        # Enviar los documentos actuales al reporte
        return self.env.ref('custom_stock_report.action_report_stock_picking_test').report_action(self)

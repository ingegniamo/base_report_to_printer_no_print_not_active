from odoo import _, api, exceptions, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval, wrap_module



class PrintingPrinter(models.Model):
    _inherit = "printing.printer"
    def print_document(self, report, content, **print_opts):
        if self.active:
            return super().print_document(report, content, **print_opts)
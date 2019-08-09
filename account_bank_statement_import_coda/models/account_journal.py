from odoo import models, api, _


class AccountJournal(models.Model):
    _inherit = "account.journal"

    def _get_bank_statements_available_import_formats(self):
        formats_list = super(AccountJournal, self)._get_bank_statements_available_import_formats()
        formats_list.append('coda')
        return formats_list
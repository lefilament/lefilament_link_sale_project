# -*- coding: utf-8 -*-

# © 2017 Le Filament (<http://www.le-filament.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class ProjectLFConfiguration(models.TransientModel):
    _name = 'project.config.settings'
    _inherit = 'project.config.settings'

    lf_tarif_jour = fields.Float('Day Price')
    lf_alias_prefix = fields.Char('Alias prefix')

    @api.multi
    def set_default_generate_project_alias(self):
        Values = self.env['ir.values'].sudo() or self.env['ir.values']
        for config in self:
            Values.set_default('project.config.settings', 'generate_project_alias', config.generate_project_alias)

    @api.multi
    def set_default_lf_tarif_jour(self):
        return self.env['ir.values'].sudo().set_default(
            'project.config.settings', 'lf_tarif_jour', self.lf_tarif_jour)

    @api.multi
    def set_default_alias_prefix(self):
        return self.env['ir.values'].sudo().set_default(
            'project.config.settings', 'lf_alias_prefix', self.lf_alias_prefix)
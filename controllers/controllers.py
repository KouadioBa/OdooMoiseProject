# -*- coding: utf-8 -*-
from odoo import http

class OpenMoise(http.Controller):
    @http.route('/open-moise', auth='public')
    def index(self, **kw):
        return "Hello, world"

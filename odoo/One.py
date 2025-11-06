from odoo import http
from odoo.http import content_disposition, request
import os


class PWAController(http.Controller):

    @http.route('/sw.js', type='http', auth='public')
    def service_worker(self, **kwargs):
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, '..', 'static', 'src', 'sw.js')
        file_path = os.path.abspath(file_path)

        with open(file_path, 'rb') as f:
            content = f.read()
        headers = [('Content-Type', 'application/javascript')]
        return request.make_response(content, headers)

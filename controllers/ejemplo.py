from odoo import http


class Ejemplo(http.Controller):
    @http.route('/example', type='http', auth='public', website=True)
    def render_example_page(self):
        return http.request.render('openacademy.vista_controller', {})

    @http.route('/example/detail', type='http', auth='public', website=True)
    def navigate_to_detail_page(self):
        companies = http.request.env['res.company'].sudo().search([])
        return http.request.render('openacademy.vista_detalle_controller', {'companies': companies})




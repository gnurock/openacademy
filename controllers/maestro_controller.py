from odoo import http


class Maestro_controller(http.Controller):
    @http.route('/maestro', type='http', auth='public', website=True, csrf=False)
    def render_example_page(self):
        datos = http.request.env['openacademy.maestro'].sudo().search([])
        return http.request.render('openacademy.maestro_vista_controller', {'datos': datos})
    
    @http.route('/maestro/editar',type='http', auth='public', website=True, csrf=False)
    def render_maestro_editar(self,**post):
        if post:
            maestro_id = int(post.get('id', False))
            maestro = http.request.env['openacademy.maestro'].sudo().search([('id', '=', maestro_id)])
            numero_empleado = maestro.numero_empleado
            descripcion = maestro.description
            return http.request.render('openacademy.maestro_editar',
                                       {'numero_empleado': numero_empleado, 'descripcion': descripcion,
                                        'id':maestro_id})
        else:
            print "no hay tal cosa"
  
    # accion de guardar cambios de datos en maestro
    @http.route('/maestro/guardar',type='http',auth='public',website=True,crsf=False)
    def render_maestro_guardar(self,**post):
        if post:
            maestro_id = int(post.get('id',False))
            print "guardar cambios en maestro",maestro_id
            if maestro_id:
                obj = http.request.env['openacademy.maestro'].sudo().browse(maestro_id)
                for o in obj:
                    obj.write({
                        # 'edad' : post.get('edad', False),
                        'numero_empleado': post.get('numero_empleado', False),
                        'description': post.get('descripcion', False),
                    })
                
        datos=http.request.env['openacademy.maestro'].sudo().search([])
        return http.request.render('openacademy.maestro_vista_controller', {'datos':datos})

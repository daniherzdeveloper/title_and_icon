import base64
import io
from odoo import http
from odoo.http import request
from odoo.tools.mimetypes import guess_mimetype

try:
    from werkzeug.utils import send_file
except ImportError:
    from odoo.tools._vendor.send_file import send_file

class CompanyFaviconController(http.Controller):

    @http.route(['/web/binary/company_favicon/<int:company_id>'], type='http', auth="none", cors="*")

    def company_favicon(self, company_id, **kw):
        company = request.env['res.company'].sudo().browse(int(company_id))
        favicon = company.favicon

        if favicon:
            image_base64 = base64.b64decode(favicon)
            mimetype = guess_mimetype(image_base64, default='image/ico')

            response = send_file(
                io.BytesIO(image_base64),
                request.httprequest.environ,
                mimetype=mimetype,
                download_name='favicon.ico',
            )
        
            return response
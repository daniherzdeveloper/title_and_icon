import base64
import io
import os
from odoo import models, api, fields, tools
from PIL import Image

class Company(models.Model):
    _inherit = 'res.company'
    _description = 'Res Company Inherit'

    favicon = fields.Binary(
        string="Company Favicon",
        help="This field holds the image used to display a favicon for a given company.",    
    )

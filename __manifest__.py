{
    'name': 'Title and Icon',
    'version': '17.0',
    'license': 'AGPL-3',
    'author': 'daniherzdeveloper@gmail.com',
    'category': 'Extra Tools',
    'summary': 'Title and Icon',
    'depends': ['base', 'web'],
    'data': [
        'views/res_company_inherit_view.xml',
        'views/custom_favicon.xml',
    ],
    'assets' : {
        'web.assets_backend': [
            'title_and_icon/static/src/**/*',
        ],
    }
}

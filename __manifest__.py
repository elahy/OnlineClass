# -*- coding: utf-8 -*-

{
    'name': 'Online Class',
    'version': '1.0.0',
    'category': 'Learning',
    'author': 'Qudrat-E-Elahy',
    'sequence': -110,
    'summary': 'Live Video Call Online Class',
    'description': """Live Video Call Online Class""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/participant_view.xml',
        'views/course_view.xml',
        'views/channel_view.xml',
        'views/configuration_view.xml',
        'views/course_tag_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'post_init_hook': '',
    'license': 'LGPL-3',
}

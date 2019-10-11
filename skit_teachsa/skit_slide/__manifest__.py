# -*- coding: utf-8 -*-

{
    'name': 'Slide',
    'summary': "Slide customization",
    'category': 'Website',
    'author': 'Srikesh Infotech',
    'company': 'Srikesh Infotech',
    'website': 'http://www.srikeshinfotech.com',
    'license': "AGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'views/slide_document.xml',
        'views/skit_quiz.xml',
        'views/slide_options.xml',
        'views/website_slides_views.xml',
        'views/skit_website_login_form.xml',
        'views/website_template.xml',
        'views/res_partner_views.xml',
        'views/sponser.xml',
        'views/elearning_student.xml',
        'views/slide_grade_views.xml',
        'views/quotes.xml',
        'views/question.xml',
        'views/website_grade_templates.xml'
        ],
    'qweb': [
         'static/src/xml/quotestemp.xml',
        ],
    'depends': ['website_slides', 'website_forum', 'rating',
                'sale', 'base', 'calendar'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
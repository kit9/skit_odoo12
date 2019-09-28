# -*- coding: utf-8 -*-
from odoo import models, fields

class Slide(models.Model):
 
    _inherit = 'slide.channel'
 
    channel_type= fields.Selection([('D','Documentation'),
                                    ('T','Training')],
                                     string='Type')
    user_id = fields.Many2one('res.users', string='Responsible', index=True)

    website_id = fields.Many2one('website',string='Website')
    
    enroll = fields.Selection([('P','Public'),
                               ('On','On Invitation'),
                               ('On','On Payment')],
                                string='Enroll Policy')
    upload_group_ids = fields.Many2many(
        'res.groups', 'rel_upload_groups', 'channel_id', 'group_id',
        string='Upload Groups', help="Groups allowed to upload presentations in this channel. If void, every user can upload.")
          
    enroll_group_ids = fields.Many2many(
        'res.groups', 'rel_enroll_groups', 'channel_id', 'group_id',
        string='Enroll Groups', help="Groups allowed to upload presentations in this channel. If void, every user can upload.")      
    allow_comment = fields.Boolean(string='Allow Rating')
    
    forum_id = fields.Many2one('forum.forum',string='Forum')
    
    publish_template_id = fields.Many2one(
        'mail.template', string='New Content Email',
        help="Email template to send slide publication through email",
        default=lambda self: self.env['ir.model.data'].xmlid_to_res_id('website_slides.slide_template_published'))
   
    share_template_id = fields.Many2one(
        'mail.template', string='Share Template',
        help="Email template used when sharing a slide",
        default=lambda self: self.env['ir.model.data'].xmlid_to_res_id('website_slides.slide_template_shared')) 

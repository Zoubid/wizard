# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp import exceptions 

class TodoWizard(models.TransientModel):
    _name = 'wizard'
    name = fields.Char('Name', required=True)
    
    @api.multi
    def create_request(self):
        print "You click finish"

        return True


	



class callingwizard(models.Model):
	_name='call.wizard'

	@api.multi
	def open(self):

		    res = self.env['ir.actions.act_window'].for_xml_id('wizard','action_view_wizard')
		    return res

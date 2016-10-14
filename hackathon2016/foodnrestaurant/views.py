from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest,HttpResponsePermanentRedirect,HttpResponseForbidden
import json
from models import *


MENU = {
	'1':
		[
			{'name':'Beer','id':1,'price':30},
			{'name':'Chocolate','id':2,'price':30},
			{'name':'Lay\'s','id':3,'price':30}
		],
	'2':
		[
			{'name':'Item1','id':4,'price':30},
			{'name':'Item2','id':5,'price':30},
			{'name':'Item3','id':6,'price':30},
		]
}

def test(request):
	return HttpResponse('HAHAHAHAHAHAHAHAHAHA',content_type='application/json')

def  get_menu(request,hotelid):
	return HttpResponse(json.dumps(MENU[hotelid]),content_type='application/json')

def place_order(request,FMN):
	resp = {'success':False}
	try:
		orders = request.POST['order']
		for order in orders:
			o = Order(bookingId=FMN,itemId=order['id'],unit=order['unit'],price=order['price'])
			o.save()
		resp['success'] = True
	except:
		raise
	return resp

def get_order(request,FMN):
	resp = {'success':False,'order':[],'grandtotal':0}
	try:
		orders = []
		grandtotal = 0
		o = Order.objects.filter(bookingId=FMN)
		for order in o:
			orders.append({'id':order.itemId,'price':order.price,'unit':order.unit,'total':(order.price*order.unit)})
			grandtotal += (order.price*order.unit)
		resp = {'success':True,'order':orders,'grandtotal':grandtotal}
	except:
		raise
	return resp

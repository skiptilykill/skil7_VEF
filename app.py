from bottle import *
#from bottle import app, redirect, response, request, template, route, run
from beaker.middleware import SessionMiddleware
import os

'''
@route('/')
def index():
    if request.get_cookie('hello'):
        return "Hello again"
    else:
        response.set_cookie('hello', 'world')
        return 'Hello World'
'''

adminuser = 'admin'
adminpwd = 'pass'

@route('/')
def index():
    return template('index')

@route('/login')
def login():
    return template('login')

@route('/login', method='post')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == adminuser and password == adminpwd:
        response.set_cookie('account', username, secret='my_secret_code')
        return redirect('/restricted')
    else:
        return "Login failed. <br> <a href='/login'>Login</a>"

@route('/restricted')
def restricted():
    user = request.get_cookie('account', secret='my_secret_code')
    print(user)
    if(user):
        return "Restricted area. <br> <a href='/signout'>Log off</a>"
    else:
        return "You are not logged in. Access denied"

@route('/signout')
def signout():
    response.set_cookie('account', "", expires=0)
    return "You have been signed out. <br> <a href='/login'> Login</a>"

#session lausn

session_opt = {
    'session.type': 'file',
    'session.data_dir': './data'
}

products = [
    {"pid": 1, "name": "vara A", "price": 100},
    {"pid": 2, "name": "vara B", "price": 400},
    {"pid": 3, "name": "vara C", "price": 800},
    {"pid": 4, "name": "vara D", "price": 300}
]

my_session = SessionMiddleware(app(), session_opt)

@route('/shop')
def shop():
    return template('shop', products=products)

@route('/cart/add/<id>')
def add_to_cart(id):
    session = request.environ.get('beaker.session')
    if session.get(id):
        fjoldi = session.get('Fjoldi_' + id)
        fjoldi = int(fjoldi)
        fjoldi = fjoldi + 1
        session['Fjoldi_' + id] = fjoldi
    else:
        session[id] = products[int(id) - 1]['name']
        session['Fjoldi_' + id] = '1'
    #session[id] = products[int(id)-1]['name']
    session.save()

    print(session)
    return  redirect('/cart')

@route('/cart')
def cart():
    session = request.environ.get('beaker.session')
    karfa = []
    karfa = []
    for i in range(1, len(products)+1):
        i =  str(i)
        if session.get(i):
            vara =  session.get(i)
            fjoldi = session.get('Fjoldi_' + i)
       
            karfa.append({'vara': vara, 'fjoldi': fjoldi})
    return template('cart', karfa=karfa)

@route('/cart/remove')
def remove_cart():
    session = request.environ.get('beaker.session')
    session.delete()
    return redirect('/shop')

run(app=my_session, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

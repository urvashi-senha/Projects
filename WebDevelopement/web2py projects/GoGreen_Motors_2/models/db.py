# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
  #  db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
  db=DAL("mysql://root:urvashi@localhost/DBPHASE3");
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)




db.define_table('EMPLOYEE',
	SQLField('Emp_ID', type = 'integer' , length = 11 ),
	SQLField('Name', type = 'string' , length = 256 ),
	SQLField('Address', type = 'string' , length = 256 ),
	SQLField('Ph_no', type = 'integer' , length = 20 ),
	SQLField('Salary', type = 'integer' , length = 11 ),
	SQLField('Designation', type = 'string', requires= IS_IN_SET(['Manager','Team Leader','Executive']) ),
	SQLField('Email_id', type = 'string' , length = 256 ),
	primarykey=['Emp_ID'],
	migrate=False)

db.define_table('CUSTOMER',
	SQLField('Customer_ID', type = 'integer' , length = 11 ),
	SQLField('Name', type = 'string' , length = 256 ),
	SQLField('Address', type = 'string' , length = 256 ),
	SQLField('Ph_no', type = 'integer' , length = 20 ),
	SQLField('Date_of_birth', type = 'date' ),
	primarykey=['Customer_ID'],
	migrate=False)

db.define_table('OTHER_PRODUCTS',
	SQLField('Product_ID', type = 'integer' , length = 11 ),
	SQLField('Name', type = 'string' , length = 256 ),
	SQLField('Price', type = 'integer' , length = 11 ),
	SQLField('Availability', type = 'string' , length = 3 ),
	primarykey=['Product_ID'],
	migrate=False)
db.define_table('BOUGHT',
	SQLField('Customer_ID', type = 'integer' , length = 11 ,  requires = IS_IN_DB(db,db.CUSTOMER.Customer_ID) ),
	SQLField('Product_ID', type = 'integer' , length = 11 , requires = IS_IN_DB(db,db.OTHER_PRODUCTS.Product_ID) ),
	SQLField('Receipt_no', type = 'integer' , length = 11 ),
	primarykey=['Receipt_no'],
	migrate=False)

db.define_table('MODEL',
	SQLField('Model_no', type = 'integer' , length = 11 ),
	SQLField('Name', type = 'string' , length = 256 ),
	SQLField('Selling_price', type = 'integer' , length = 11 ),
	SQLField('Waiting_time', type = 'integer' , length = 11 ),
	SQLField('Availability', type = 'string' , length = 3 ),
	primarykey=['Model_no'],
	migrate=False)

db.define_table('DELIVERS_TO',
	SQLField('Model_no', type = 'integer' , length = 11 ,  requires = IS_IN_DB(db,db.MODEL.Model_no) ),
	SQLField('Customer_ID', type = 'integer' , length = 11  , requires = IS_IN_DB(db,db.CUSTOMER.Customer_ID) ),
	SQLField('Registration_no', type = 'integer' , length = 11 ),
	SQLField('Engine_no', type = 'integer' , length = 11 ),
	SQLField('Chassis_no', type = 'integer' , length = 11 ),
	SQLField('Mode_of_payment', type = 'string' , length = 6 ),
	SQLField('Date', type = 'date' ),
	primarykey=['Registration_no'],
	migrate=False)

db.define_table('DEMANDS',
	SQLField('Customer_ID', type = 'integer' , length = 11 ,  requires = IS_IN_DB(db,db.CUSTOMER.Customer_ID) ),
	SQLField('Model_no', type = 'integer' , length = 11 , requires = IS_IN_DB(db,db.MODEL.Model_no) ),
	SQLField('Date', type = 'date' ),
	SQLField('Waiting_list_no', type = 'integer' , length = 11 ),
	primarykey=['Customer_ID', 'Model_no', 'Waiting_list_no'],
	migrate=False)



db.define_table('FINANCE',
	SQLField('Id', type = 'integer' , length = 11 ),
	SQLField('Type', type = 'string', requires=IS_IN_SET(['Income','Expense']) ),
	SQLField('Date', type = 'date' ),
	SQLField('Cause', type = 'string' , length = 100 ),
	SQLField('Employee_Id', type = 'integer' , length = 11 , requires = IS_IN_DB(db,db.EMPLOYEE.Emp_ID) ),
	primarykey=['Id'],
	migrate=False)

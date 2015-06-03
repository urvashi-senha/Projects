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
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
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

db.define_table('categories',
    db.Field('name','string',required=True,requires=IS_NOT_IN_DB('categories.id','categories.name')))
    
db.define_table('links',
    db.Field('url','string',requires=IS_URL(),label='Link'),
    db.Field('username',db.auth_user,requires=IS_IN_DB(db,'auth_user.id','auth_user.name'),label='User'),
    db.Field('heading','string',required=True,label='Heading'),
    db.Field('category','string',label='Category'),
    db.Field('date_posted','datetime',default=request.now.date()),
    db.Field('time_posted','datetime',default=request.now),
    db.Field('likes','integer',default='0'),
    db.Field('dislikes','integer',default='0'),
    db.Field('points','integer',default='100'),
    db.Field('video_link','string',requires=IS_URL()))


db.define_table('liked',
    db.Field('usr',db.auth_user,requires=IS_IN_DB(db,'auth_user.id','auth_user.name'),label='User'),
    db.Field('link',db.links,requires=IS_IN_DB(db,'links.id','links.id')))

db.define_table('disliked',
    db.Field('usr',db.auth_user,requires=IS_IN_DB(db,'auth_user.id','auth_user.name'),label='User'),
    db.Field('link',db.links,requires=IS_IN_DB(db,'links.id','links.id')))


db.define_table('comments',
    db.Field('usr',db.auth_user,requires=IS_IN_DB(db,'auth_user.id','auth_user.name'),label='User'),
    db.Field('link',db.links,requires=IS_IN_DB(db,'links.id','links.id')),
    db.Field('commented','string',required=True),
    db.Field('date_com','datetime',default=request.now.date()),
    db.Field('time_com','datetime',default=request.now))

# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def search():
     """an ajax wiki search page"""
     return dict(form=FORM(INPUT(_id='keyword',_name='keyword',
              _onkeyup="ajax('callback', ['keyword'], 'target');")),
              target_div=DIV(_id='target'))
              
def callback():
     """an ajax callback that returns a <ul> of links to wiki pages"""
     query1 = db.EMPLOYEE.Name.contains(request.vars.keyword)
     query2 = db.CUSTOMER.Name.contains(request.vars.keyword)
     query3 = db.OTHER_PRODUCTS.Name.contains(request.vars.keyword)
     query4 = db.MODEL.Name.contains(request.vars.keyword)
     pages1 = db(query1).select()
     pages2 = db(query2).select()
     pages3 = db(query3).select()
     pages4 = db(query4).select()
     links = [A(p.Name, _href=URL('show_cust',args=p.Customer_ID)) for p in pages2]
     links.append([A(p.Name) for p in pages1])
     links.append([A(p.Name, _href=URL('show_prd',args=p.Product_ID)) for p in pages3])
     links.append([A(p.Name, _href=URL('show_model',args=p.Model_no)) for p in pages4])
     return UL(*links)
 
def search2():
     """an ajax wiki search page"""
     return dict(form=FORM(INPUT(_id='keyword',_name='keyword',
              _onkeyup="ajax('callback', ['keyword'], 'target');")),
              target_div=DIV(_id='target'))
              
def callback2():
     """an ajax callback that returns a <ul> of links to wiki pages"""
     query1 = db.EMPLOYEE.Name.contains(request.vars.keyword)
     query2 = db.CUSTOMER.Name.contains(request.vars.keyword)
     pages1 = db(query1).select()
     pages2 = db(query2).select()
     links = [A(p.Name, _href=URL('show_empl',args=p.Emp_ID)) for p in pages1]
     links.append([A(p.Name) for p in pages2])
     return UL(*links)
            
def index():
    'auth' in globals()
   
    message="Go Green Welcomes You !!"
    if auth.user :
        if auth.user.id==1:
            message="Welcome TSM HYDERABAD"
            redirect(URL('admin'))
        else:
            message="Welcome Employee"
            redirect(URL('empl'))
    else:
        redirect(URL('user'))
    return locals()

def admin():
    man=db(db.EMPLOYEE.Designation=='Manager').select()
    team=db(db.EMPLOYEE.Designation=='Team Leader').select()
    exe=db(db.EMPLOYEE.Designation=='Executive').select()
    return locals()
def add_employee():
    'auth' in globals()

    if auth.user:
         if auth.user.id!=1:
             redirect(URL('user'))
         else:
            form=SQLFORM(db.EMPLOYEE)
            if form.accepts(request.vars,session):
                    response.flash='Employee Added !!'
            elif form.errors:
                    response.flash='ERRORS!!!'
    else:
         redirect(URL('user'))
    return locals()

def delete_employee():
    'auth' in globals()
    message=""
    if auth.user.id==1:
        list=db(db.EMPLOYEE.Emp_ID>0).select()
        form=SQLFORM.factory(
                    db.Field('usrname',db.EMPLOYEE,requires=IS_IN_DB(db,'EMPLOYEE.Emp_ID','EMPLOYEE.Email_id'),required=True))
        if form.accepts(request.vars,session):
                    e=db(db.EMPLOYEE.Emp_ID==int(request.vars.usrname)).select()
                    db(db.EMPLOYEE.Emp_ID==int(request.vars.usrname)).delete()
                    db(db.auth_user.email==e[0]['Email_id']).delete()
                    message="employee deleted !!"
                    redirect(URL('delete_employee'))
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('user'))
    return locals()

def edit_emp():
        'auth' in globals()
        if auth.user.id==1:
             form=SQLFORM.factory(db.Field('usrname',db.EMPLOYEE,requires=IS_IN_DB(db,'EMPLOYEE.Emp_ID','EMPLOYEE.Email_id'),required=True))
             if form.accepts(request.vars,session):
                    #print "888888888888"
                    print form.vars.usrname
                    redirect(URL(r=request, f='edit_empl_2?eid=%d' % int(form.vars.usrname)))
             elif form.errors:
                    response.flash='ERRORS!!!'
        else:
            redirect(URL('user'))
        return locals()

def edit_model():
      if auth.user:
         form=SQLFORM.factory(db.Field('usrname',db.MODEL,requires=IS_IN_DB(db,'MODEL.Model_no','MODEL.Name'),required=True))
         if form.accepts(request.vars,session):
                    #print "888888888888"
                    print form.vars.usrname
                    redirect(URL(r=request, f='edit_model_2?eid=%d' % int(form.vars.usrname)))
         elif form.errors:
                    response.flash='ERRORS!!!'
      else:
            redirect(URL('user'))
      return locals()
         
def edit_model_2():
    if auth.user:
        eid=int(request.vars.eid)
        record=db(db.MODEL.Model_no==int(eid)).select()
        return locals()
def edit_model_3():
        if auth.user:
             eid=int(request.post_vars.eid)
             nam=request.post_vars.nam  
             prc=int(request.post_vars.prc)
             tim=request.post_vars.tim
             avb=request.post_vars.avb
             db(db.MODEL.Model_no==eid).update(Name=nam,Selling_price=prc,Waiting_time=tim,Availability=avb)
             redirect(URL('edit_model'))
        return locals()
        
def show_empl():
      print '****************////'
      eid=int(request.args(0))
      print '*********'
      print eid  
      record=db(db.EMPLOYEE.Emp_ID==int(eid)).select()
      return locals()
def show_cust():
      if auth.user:
        eid=int(request.args(0))
        record=db(db.CUSTOMER.Customer_ID==int(eid)).select()
      return locals()

def show_prd():
      if auth.user:
          eid=int(request.args(0))
          record=db(db.OTHER_PRODUCTS.Product_ID==int(eid)).select()
      return locals()
def show_model():
      if auth.user:
          eid=int(request.args(0))
          record=db(db.MODEL.Model_no==int(eid)).select()
      return locals()
              
def edit_empl_2():
    if auth.user:
        eid=int(request.vars.eid)
        record=db(db.EMPLOYEE.Emp_ID==int(eid)).select()
        return locals()

def edit_emp_3():
     if auth.user:
         eid=request.post_vars.eid
         nam=request.post_vars.nam
         add=request.post_vars.add
         no=request.post_vars.no
         sal=request.post_vars.sal
         deg=request.post_vars.deg
         email=request.post_vars.email
         db(db.EMPLOYEE.Emp_ID==eid).update(Name=nam,Address=add,Ph_no=no,Salary=sal,Designation=deg,Email_id=email)
         redirect(URL('edit_emp'))
         return locals()
          

def add_model():
    'auth' in globals()
    if auth.user.id==1:
        form=SQLFORM(db.MODEL)
        if form.accepts(request.vars,session):
                    response.flash='Model Added !!'
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()
def del_model():
    'auth' in globals()
    message=""
    if auth.user.id==1:
        form=SQLFORM.factory(
                    db.Field('model',db.MODEL,requires=IS_IN_DB(db,'MODEL.Model_no','Models.Name'),required=True))
        if form.accepts(request.vars,session):
                    db(db.MODEL.Model_no==request.vars.model).delete()
                    response.flash="Model Deleted !!"
                    redirect(URL('del_model'))
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()

def add_other_product():
    'auth' in globals()
    if auth.user.id==1:
        form=SQLFORM(db.OTHER_PRODUCTS)
        if form.accepts(request.vars,session):
                    response.flash='Product Added !!'
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()
def del_other_product():
    'auth' in globals()
    message=""
    if auth.user.id==1:
        form=SQLFORM.factory(
                    db.Field('product',db.OTHER_PRODUCTS,requires=IS_IN_DB(db,'OTHER_PRODUCTS.Product_ID','OTHER_PRODUCTS.Name'),required=True))
        if form.accepts(request.vars,session):
                    db(db.OTHER_PRODUCTS.Product_ID==request.vars.product).delete()
                    response.flash="Product Deleted !!"
                    redirect(URL('del_other_product'))
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()

def empl():
    if auth.user:
            e=db(str(auth.user.email) == db.EMPLOYEE.Email_id).select()
            ee=str(e[0]['EMPLOYEE.Designation'])
    else:
            redirect(URL('user'))
    return locals()
            
       
def add_customer():
    'auth' in globals()
    if auth.user:
        form=SQLFORM(db.CUSTOMER)
        if form.accepts(request.vars,session):
                    response.flash='Customer Added !!'
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()
  
def edit_cust():
      if auth.user:
           form=SQLFORM.factory(db.Field('usrname',db.CUSTOMER,requires=IS_IN_DB(db,'CUSTOMER.Customer_ID','CUSTOMER.Name'),required=True))
           if form.accepts(request.vars,session):
                    #print "888888888888"
                    print form.vars.usrname
                    redirect(URL(r=request, f='edit_cust_2?eid=%d' % int(form.vars.usrname)))
           elif form.errors:
                    response.flash='ERRORS!!!'
      else:
            redirect(URL('user'))
      return locals()

def edit_cust_2():
    if auth.user:
        eid=int(request.vars.eid)
        record=db(db.CUSTOMER.Customer_ID==int(eid)).select()
        return locals()
def edit_cust_3():
    if auth.user:
         eid=int(request.post_vars.eid)
         nam=request.post_vars.nam
         add=request.post_vars.add
         no=int(request.post_vars.no)
         dob=request.post_vars.dob
         db(db.CUSTOMER.Customer_ID==eid).update(Name=nam,Address=add,Ph_no=no,Date_of_birth=dob)
         redirect(URL('edit_cust'))
         return locals()
          
def add_sale():
    'auth' in globals()
    if auth.user:
        form=SQLFORM(db.BOUGHT)
        if form.accepts(request.vars,session):
                    response.flash='Product Sold !!'
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()

def order_bike():
    'auth' in globals()
    if auth.user:
        form=SQLFORM(db.DEMANDS)
        if form.accepts(request.vars,session):
                    response.flash='Bike Ordered !!'
                    list=db(db.FINANCE.Id>0).select(orderby=~(db.FINANCE.Id))
                    l=int(list[0]['FINANCE.Id']) + 1
                 #   print '%%%%%'
                 #   print l
                 #   e=db(db.EMPLOYEE.Emp_ID>0).select()
                 #   print "///"
                  #  print auth.user.email
                    e=db(str(auth.user.email) == db.EMPLOYEE.Email_id).select()
                  #  print '*****'
                   # print e
                    ee=int(e[0]['EMPLOYEE.Emp_ID'])
                   # print "88888888888888"
                  #  print ee
                    db.FINANCE.insert(id=l,Type='Income',Date=request.now.date(),Cause='Bike sale',Employee_Id=ee)
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()

def sell_bike():
    'auth' in globals()
    if auth.user:
        form=SQLFORM(db.DELIVERS_TO)
        if form.accepts(request.vars,session):
                    m=int(request.vars.Model_no)
                    c=int(request.vars.Customer_ID)
                    db((db.DEMANDS.Model_no==m ) & (db.DEMANDS.Customer_ID==c)).delete()                           
                    response.flash='Bike Ordered !!'
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()

def add_expense():
    'auth' in globals()
    if auth.user:
        form=SQLFORM(db.FINANCE)
        if form.accepts(request.vars,session):
                    response.flash='Expense Added !!'
        elif form.errors:
                    response.flash='ERRORS!!!'
    else:
        redirect(URL('index'))
    return locals()

def list():
        if auth.user:
            l=db(db.DEMANDS.Waiting_list_no > 0).select()
            c=db(db.CUSTOMER.Customer_ID > 0).select()
        else:
            redirect(URL('user'))
        return locals()

def order_bikes():
       if auth.user:
           m=db(db.MODEL.Model_no > 0).select()
           l=db(db.DEMANDS.Waiting_list_no > 0).select()
       else:
           redirect(URL('index'))
       return locals()
              
            
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

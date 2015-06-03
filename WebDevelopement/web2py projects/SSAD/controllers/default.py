# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

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
    """if auth.user:
        if auth.user.id==1:
            redirect(URL('admin'))
        else:
            redirect(URL('index'))
    """
    return dict(form=auth())


@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    'auth' in globals()
    if auth.user:
        if (auth.user.id)==1:
            message = "WELCOME ADMIN IIITH !!"
            redirect(URL('admin'))
        else:
            message = "WELCOME TO MY REDDIT !!"
            cat=db(db.categories.id>0).select('categories.name')
  
    else:
        redirect(URL('user'))
    return dict(message=message,cat=cat)
@auth.requires_login()
def display():
   if auth.user:
    cat=str(request.post_vars.cate)
    lists=db(db.links.category==cat).select(orderby=~(db.links.points))
    ids=db(db.auth_user.id>0).select()
    if len(lists)>0:
        for i in range(len(lists)):
            c=int(lists[i]['links.id'])
            com=db(db.comments.link==c).select()
    else:
        com=[]
   else:
    redirect(URL('user'))
   return dict(lists=lists,cat=cat,ids=ids,com=com)

def like():
    if auth.user:
        a=int(auth.user.id)
        i=request.post_vars.link
        cat=str(request.post_vars.cat)
        users=db(db.disliked.link == i).select()
        flag=0
        for k in range(len(users)):
            if a==int(users[k]['disliked.usr']):
                db(db.disliked.usr==a).delete()
                db.liked.insert(usr=a,link=i)
                lik=db(db.links.id==i).select('links.dislikes')
                l=int(lik[0]['links.dislikes'])
                l=l-1
                db(db.links.id==i).update(dislikes=l)
                pi=db(db.links.id==i).select()
                p=int(pi[0]['links.points'])
                p=p+8
                db(db.links.id==i).update(points=p)
                lik=db(db.links.id==i).select()
                l=int(lik[0]['links.likes'])
                l=l+1
                db(db.links.id==i).update(likes=l)
                flag=1
                message= " U had disliked this earlier,now liked !!"
                session.flash=T("Post liked!")
        if flag==0:
            u=db(db.liked.link==i).select()
            for m in range(len(u)):
                if a==int(u[m]['liked.usr']):
                    message="post already liked"                    
                    flag=1
                    session.flash=T("Post liked!")
        if flag==0:
             lik=db(db.links.id==i).select()
             l=int(lik[0]['links.likes'])
             l=l+1
             db(db.links.id==i).update(likes=l)
             pi=db(db.links.id==i).select()
             p=int(pi[0]['links.points'])
             p=p+5
             db(db.links.id==i).update(points=p)
             db.liked.insert(usr=a,link=i)
             message = "post liked"
             session.flash=T("Post liked!")
    else:
        redirect(URL('user'))
    return dict(message=message,users=users,cat=cat)

def dislike():
    if auth.user:
        a=auth.user.id
        i=request.post_vars.link
        cat=str(request.post_vars.cat)
        users=db(db.liked.link==i).select()
        flag=0
        for k in range(len(users)):
            if a==int(users[k]['liked.usr']):
                db(db.liked.usr==a).delete()
                db.disliked.insert(usr=a,link=i)
                lik=db(db.links.id==i).select('links.likes')
                l=int(lik[0]['links.likes'])
                l=l-1
                db(db.links.id==i).update(likes=l)
                lik=db(db.links.id==i).select('links.dislikes')
                l=int(lik[0]['links.dislikes'])
                l=l+1
                db(db.links.id==i).update(dislikes=l)
                pi=db(db.links.id==i).select()
                p=pi[0]['links.points']
                p=p-8
                db(db.links.id==i).update(points=p)
                flag=1
                message= " U had liked this earlier,now disliked !!"
                session.flash=T("Post Disliked!")
        if flag==0:
            u=db(db.disliked.link==i).select()
            for m in range(len(u)):
                if a==int(u[m]['disliked.usr']):
                    message="post already disliked"
                    flag=1
                    session.flash=T("Post Disliked!")
        if flag==0:
             lik=db(db.links.id==i).select('links.dislikes')
             l=int(lik[0]['links.dislikes'])
             l=l+1
             db(db.links.id==i).update(dislikes=l)
             db.disliked.insert(usr=a,link=i)
             message= "post disliked "
             session.flash=T("Post Disliked!")
    else:
        redirect(URL('user'))
    return dict(message=message,cat=cat)
@auth.requires_login()
def comment():
    if auth.user:
        ids=auth.user.id
        i=request.post_vars.link
        cat=str(request.post_vars.cat)
    else:
        redirect(URL('user'))
    return dict(ids=ids,i=i,cat=cat)
@auth.requires_login()    
def add_comment():
    com=request.post_vars.comment
    i=request.post_vars.ids
    link=request.post_vars.link
    cat=str(request.post_vars.cat)
    db.comments.insert(usr=i,link=link,commented=com)
    session.flash=T("Post Commented successfully!")
    return dict(cat=cat)

@auth.requires_login()
def view_posts():
    if auth.user:
        a=auth.user.id
        lists=db(db.links.username==auth.user).select(orderby=~(db.links.points))
        ids=db(db.auth_user.id>0).select()
        com=[]
        if len(lists)>0:
            for i in range(len(lists)):
                com=(db(db.comments.id>0).select())
            
        else:
            com=[]
    else:
        redirect(URL('user'))
    return dict(lists=lists,com=com,ids=ids,a=a)
def edit_post():
    if auth.user:
        link=request.post_vars.link
        lists=db(db.links.id==link).select()
        cat_list=db(db.categories.id>0).select()
        cate=[]
        if len(cat_list)>0:
                  for i in range(len(cat_list)):
                          cate.append(cat_list[i]['categories.name'])
    else:
        redirect(URL('user'))
    return dict(lists=lists,cate=cate)
def edit_post_2():
    if auth.user:
       i=int(request.post_vars.link)
       url=str(request.post_vars.url)
       head=str(request.post_vars.head)
       cat=str(request.post_vars.cat)
       db(db.links.id==i).update(url=url,heading=head,category=cat)
       session.flash=T("Post edited successfully!")
    else:
        redirect(URL('user'))
    return locals()

def del_post():
    if auth.user:
        a=int(request.post_vars.a)
        link=int(request.post_vars.link)
        db(db.links.id==link).delete()
        db(db.liked.link==link).delete()
        db(db.disliked.link==link).delete()
        db(db.comments.link==link).delete()
        session.flash=T("Post deleted successfully!")        
    else:
        redirect(URL('user'))
    return locals()
@auth.requires_login()
def admin():
    if auth.user:
        if(auth.user.id)!=1:
            redirect(URL('index'))
        else:
            message="ADMIN HOME PAGE "
        return dict(message=message)
    else:
        redirect(URL('user'))
    return locals()
@auth.requires_login()
def add_category():
    'auth' in globals()
    if auth.user:
        flag=1
    else:
        redirect(URL('index'))
    return locals()
def add_category_2():
    cat_name=request.post_vars.cat_name
    if cat_name=='':
            redirect(URL('add_category'))
    list=db(db.categories.id>0).select()
    if len(list) > 0:
            records=[]
            for i in range(len(list)):
                records.append(list[i]['categories.name'])
            flag=0
            for i in range(len(records)):
                if str(records[i])==str(cat_name):
                    message="Category exists !!"
                    flag=1
            if flag==0:
                db.categories.insert(name=cat_name)
                message="New category added successfully !!"
         
    else:
        db.categories.insert(name=cat_name)
        message="New category added successfully !!"
    return dict(message=message)
@auth.requires_login()
def delete_user():
        'auth' in globals()
        if auth.user:
            if auth.user.id==1:
                form=SQLFORM.factory(
                    db.Field('usrname',db.auth_user,requires=IS_IN_DB(db,'auth_user.id','auth_user.email'),required=True))
                if form.accepts(request.vars,session):
                    redirect(URL(r=request,f='delete_user_2?usrname=%d'% int(form.vars.usrname)))
                elif form.errors:
                    response.flash='ERRORS!!!'
            else:
                response.flash='access denied'
                redirect(URL('index'))
        else:
            redirect(URL('user'))
        return dict(form=form)
@auth.requires_login()        
def delete_user_2():
        if auth.user:
            if auth.user.id==1:
                usrname=int(request.vars.usrname)
                if usrname==1:
                    redirect(URL('delete_user'))
                l=db(db.liked.usr==usrname).select()
                d=db(db.disliked.usr==usrname).select()
                for i in range(len(l)):
                   lik=db(db.links.id==l[i]['liked.link']).select()
                   lo=int(lik[0]['links.likes'])
                   lo=lo-1
                   db(db.links.id==int(l[i]['liked.link'])).update(likes=lo)
                   p=int(lik[0]['links.points'])
                   p=p-5
                   db(db.links.id==int(l[i]['liked.link'])).update(points=p)
                for i in range(len(d)):
                   lik=db(db.links.id==d[i]['disliked.link']).select()
                   lo=int(lik[0]['links.dislikes'])
                   lo=lo-1
                   db(db.links.id==d[i]['disliked.link']).update(dislikes=lo)
                   p=int(lik[0]['links.points'])
                   p=p+3
                   db(db.links.id==d[i]['disliked.link']).update(points=p)
                db(db.auth_user.id==usrname).delete()
            else:
                redirect(URL('index'))
        else:
            redirect(URL('user'))
        return locals()
@auth.requires_login()     
def admin_view_posts():
    if auth.user:
        if auth.user.id==1:
            a=auth.user.id
            print a
            lists=db(db.links.id>0).select(orderby=~(db.links.points))
            ids=db(db.auth_user.id>0).select()
            if len(lists)>0:
                for i in range(len(lists)):
                    c=int(lists[i]['links.id'])
                    com=db(db.comments.link==c).select()
            else:
                com=[]
        else:
            redirect(URL('user'))
    return dict(lists=lists,com=com,ids=ids,a=a)
@auth.requires_login()       
def delete_post_admin_1():
    if auth.user:
            if auth.user.id==1:
                form=SQLFORM.factory(
                    db.Field('link',db.links,requires=IS_IN_DB(db,'links.id','links.heading'),required=True))
                if form.accepts(request.vars,session):
                    redirect(URL(r=request,f='delete_post_admin?link=%d'% int(form.vars.link)))
                elif form.errors:
                    response.flash='ERRORS!!!'
            else:
                    response.flash='access denied'
                    redirect(URL('index'))
            return dict(form=form)

def delete_post_admin():
    if auth.user:
            if auth.user.id==1:
                link=int(request.vars.link)
                db(db.links.id==link).delete()
                db(db.liked.link==link).delete()
                db(db.disliked.link==link).delete()
                db(db.comments.link==link).delete()     
            else:
                redirect(URL('index'))
    else:
            redirect(URL('user'))
    return locals()
    
@auth.requires_login()
def post_link():
   if auth.user:
       if auth.user.id == 1:
         redirect(URL('admin')) 
       else:
          i=db(db.auth_user.id==auth.user.id).select()
          d=i[0]['auth_user.id']
          fname=i[0]['auth_user.first_name']
          lname=i[0]['auth_user.last_name']
          cat_list=db(db.categories.id>0).select()
          cate=[]
          if len(cat_list)>0:
                  for i in range(len(cat_list)):
                          cate.append(cat_list[i]['categories.name'])
   else:
       redirect(URL('user'))
   return locals()

def post_link_2():
   fname=str(request.post_vars.fname)
   lname=str(request.post_vars.lname)
   name=fname+' '+lname
   i=int(request.post_vars.i)
   url=str(request.post_vars.url)
   video=str(request.post_vars.video)
   if url=='' and video=='':
       redirect(URL('post_link'))
   head=str(request.post_vars.head)
   if head=='':
       redirect(URL('post_link'))
   cat=str(request.post_vars.cat)
   if cat=='':
       redirect(URL('post_link'))
   if video=='':
       db.links.insert(url=url,username=i,heading=head,category=cat,likes=0,dislikes=0)
   elif url=='':
        db.links.insert(username=i,heading=head,category=cat,likes=0,dislikes=0,video_link=video)
   message= "Successfully posted !!"
   return dict(message=message,name=name)
   
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

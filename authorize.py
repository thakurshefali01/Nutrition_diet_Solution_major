def authorizeuser(auth,role,userrole):
    if(auth==True):
        if(role==userrole):
            return True
        else:
            return False,"Wrong user Type"
    else:
        return False,"Not login"
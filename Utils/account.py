import grp
from simplepam import authenticate

def isAdmin(username,admin_group):
    return (username,admin_group in [g.gr_name for g in grp.getgrall() if username in g.gr_mem] if True else False)
def canLogin(username,password,admin_group):
    return authenticate(isAdmin(username,'sudo' if admin_group == 'sudo' else 'user')[0] if isAdmin(username,'sudo' if admin_group == 'sudo' else 'user')[1] else '' ,password)
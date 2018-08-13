#coding=gbk
from privileges import Privileges
from admin import Admin

privileges = ['can add post','can delete post','can ban user'];
pri = Privileges(privileges);
admin = Admin('guoying','ma','麦田里的守望者',pri);
admin.show_privileges();

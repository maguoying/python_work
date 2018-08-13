#coding=gbk
from user import Admin,Privileges

privileges = ['can add post','can delete post','can ban user'];
pri = Privileges(privileges);
admin = Admin('guoying','ma','麦田里的守望者',pri);
admin.show_privileges();

#coding=gbk
from user import Admin,Privileges

privileges = ['can add post','can delete post','can ban user'];
pri = Privileges(privileges);
admin = Admin('guoying','ma','�������������',pri);
admin.show_privileges();

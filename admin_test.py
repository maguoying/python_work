#coding=gbk
from privileges import Privileges
from admin import Admin

privileges = ['can add post','can delete post','can ban user'];
pri = Privileges(privileges);
admin = Admin('guoying','ma','�������������',pri);
admin.show_privileges();

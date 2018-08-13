#coding=gbk
class User():
    def __init__(self,first_name,last_name,summary):
        self.first_name = first_name;
        self.last_name = last_name;
        self.summary = summary;
    
    def describe_user(self):
        print(self.summary);
    
    def greet_user(self):
        print('Welcome,' + self.first_name.title() + ' ' + self.last_name.title());

class Admin(User):
    def __init__(self,first_name,last_name,summary,privileges):
        super().__init__(first_name,last_name,summary);
        self.privileges = privileges;
        
    def print_privileges(self):
        for privilege in self.privileges.privileges:
            print(privilege);
            
class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges;
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege);
            
privileges = ['can add post','can delete post','can ban user'];
pri = Privileges(privileges);
admin = Admin('guoying','ma','�������������',pri);
print('>>>>>>>>>>>>>>>>>>>��ӡprint_privileges�б�');
print(admin.privileges.privileges);
print('>>>>>>>>>>>>>>>>>>>ѭ����ӡprint_privileges�б�');
admin.print_privileges();

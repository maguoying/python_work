#coding=gbk
from user import User
class Admin(User):
    def __init__(self,first_name,last_name,summary,privileges):
        super().__init__(first_name,last_name,summary);
        self.privileges = privileges;
        
    def show_privileges(self):
        for privilege in self.privileges.privileges:
            print(privilege);

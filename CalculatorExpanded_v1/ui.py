from user_op import UserOp

class UI:
    def __init__(self):
        print("Init UI")
        self.userop = UserOp()

    def run_menu(self):
        #print("run_menu")
        self.userop.user_menu()
        self.userop.choice()
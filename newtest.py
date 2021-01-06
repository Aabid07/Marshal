__doc__ = """ This is new doc file and it is used to 
              define new classes and it's functionalities.  
         
          """

__author__ = "Mohammad Aabid Hussain"


class UserException(Exception):
    def __init__(self, msg):
        self.msg = msg
        # super(UserException, self).__init__()
        self.message()

    def message(self):
        return Exception(f"ERROR: {self.msg}")


EX = UserException("This is userException Class")
print(EX)

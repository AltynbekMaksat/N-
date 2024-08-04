class UserManager:
    
    database = {}
    counter = 0
    
    def __init__(self):
        self.dummy = 0
        
        
    def addUser(self, name):
        print(f"Adding user with name: {name}")
        UserManager.counter += 1
        UserManager.database[UserManager.counter] = name
        print(f"User was added with id : {UserManager.counter}")
        return UserManager.counter
    
    def getUser(self, id):
        if id in UserManager.database.keys():
            print(f"User found with id : {id}", ", name is ", {UserManager.database[id]})
            return UserManager.database[id]
        else:
            print("No user found with id ", {id})
            return None
        
    
        
    
        
        
        
        

# Creating an instance of UserManager
obj = UserManager()

# Accessing attributes and calling methods
obj.addUser("Jaras")
obj.addUser("Miras")
obj.addUser("Erasyl")

obj.getUser(2)
obj.getUser(5)

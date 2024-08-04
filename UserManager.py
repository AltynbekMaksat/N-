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
        
    def deleteUser(self, id):
        if id in UserManager.database.keys():
            print(f"Deleting user with id : {id}")
            del UserManager.database[id]
            return True
        else:
            print("No user found with id ", {id}, " to delete ")
            return False
        
    def findUserByName(self, name):
        ans = []
        for key1, name1 in UserManager.database.items():
            if name1 == name:
                ans.append(key1)
                
        return ans
                
        
        

# Creating an instance of UserManager
obj = UserManager()

# Accessing attributes and calling methods
obj.addUser("Jaras")
obj.addUser("Miras")
obj.addUser("Erasyl")
obj.addUser("Miras")

obj.getUser(2)
obj.getUser(5)

print(obj.deleteUser(3))

print(obj.findUserByName("Erasyl"))

class Singleton:
    __instance=None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
            return Singleton.__instance
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("this class is a singleton")
        else:
            Singleton.__instance = self

s = Singleton()
print(s)

s= Singleton.getInstance()
print(s) 

s= Singleton.getInstance()
print(s) 


# Output : 
"""
Output --> <__main__.Singleton object at 0x00300D90>
None      
None
"""


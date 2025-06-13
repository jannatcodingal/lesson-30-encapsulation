class myclass:
    __Privatevar=27;
def __privmeth(self):
    print("im inside the class myclass")
def hello(self):
    print("private variable value",self.__Privatevar)
foo=myclass()
foo.__privmeth()
foo.hello()
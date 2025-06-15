class reverse:
    def __init__(self, string):
        self.string = string
    def reverse_string(self):
        return self.string[::-1]
    def __str__(self):
        return self.reverse_string()
r1 =("Hi! My name is Jannat.")
print(r1)
print("after reverse :")
r2= reverse("Hi! My name is Jannat.")
print(r2)
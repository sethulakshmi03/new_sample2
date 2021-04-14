class parent:
    def print_name(self ,name):
        print("Name is ",name)
class parent1(parent):
    def print_sddress(self,address):
        print("Address is",address)
class child(parent1):
    def print_class(self,cls):
        print("class is ",cls)
c = child()
c.print_class(5)
c.print_name("sethu")
c.print_sddress("asdfgf")

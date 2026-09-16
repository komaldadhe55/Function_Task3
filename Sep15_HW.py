def f1():
     def f2():
         def f3():
            print("We are inside a f3 function")
         return f3
     return f2()

Third_fun = f1()
print(Third_fun)
Third_fun()

# <function f1.<locals>.f2.<locals>.f3 at 0x000001657E1E3690>
# We are inside a f3 function



def add(n1):
    def addTwo(n2):
          def addThree(n3):
               return n1+n2+n3
          return addThree
    return addTwo

res = add(100)(100)(100)
print(res)

# 300

def add(n1):
    def addTwo(n2):
          def addThree(n3):
               return n1+n2+n3
          return addThree
    return addTwo

res = add(100)(100)
print(res(40))
print(res(140))
print(res(20))
print(res(80))

# 240
# 340
# 220
# 280








# Реализовать класс singleton (использовать декоратор)
def singleton(a):
    m = {}
    def wrap(*args, **kwargs):
        if a not in m:
            m[a] = a(*args, **kwargs)
        return m[a]
    return wrap

@singleton
class Class():
    pass
k = Class()
b = Class()
print(k)
print(b)
print(k is b)
print(type(k))
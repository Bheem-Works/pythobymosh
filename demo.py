count = 0

def add():
    global count
    count += 1

add()
add()
print(count)  # ✅ 1

a = b = c = 'hello'
print(a)
print(b)
print(c)


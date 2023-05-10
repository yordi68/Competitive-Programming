l , r = list(map(int , input().split()))

xor = l ^ r

path = 0
while xor != 0:
    path += 1
    xor = xor >> 1

max_ = 0
new = 1

while path != 0:
    max_ += new
    new = new << 1
    path -= 1

print(max_)
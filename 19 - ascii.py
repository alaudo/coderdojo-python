a = "Jingle bells, Jingle bells Jingle all the way Oh what fun it is to ride"

l = []

for i in a:
    l.append(ord(i))

print(l)

m = []

for t in l:
    m.append(t + 2)

print(m)

v = []
for k in m:
    v.append(chr(k))

print(''.join(v))



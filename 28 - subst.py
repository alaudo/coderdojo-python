def subst(text):
    s = { 'т' : 't', '$' : 's', '@' : 'a', '!' : 'i', 'Я' : 'r', '1' : 'l', 'ш' : 'w', '0' : 'o', 'п' : 'n'}
    return "".join([t if not(t in s) else s[t] for t in text ])

print(subst("тhe$e @Яe que$т!0п$ f0Я @cт!0п, п0т $pecu1@т!0п, шh!ch !$ !d1e."))

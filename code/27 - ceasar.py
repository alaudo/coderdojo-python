stoplist = [ ' ', ',', '?']
def ceasar(text, shift):
    return "".join([t if (t in stoplist) else chr(ord('a') + (ord(t) - ord('a') + shift + 26) % 26 ) for t in text])

print(ceasar("kpfkhhgtgpeg yknn egtvckpna dg vjg fqyphcnn qh ocpmkpf, dwv yjq ectgu?",-2))

def mirror(text):
    words = text.split(" ")
    nwords = []
    for w in words:
        nw = w[::-1]
        nwords.append(nw)
    return " ".join(nwords)

print(mirror("s'tI suoregnad ot eb thgir nehw eht tnemnrevog si .gnorw"))

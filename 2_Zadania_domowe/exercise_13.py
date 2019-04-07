def censor(s):
    t = []
    for a in s.split():
        if a in ["PHP", "C", "Java"]:
            t.append("****")
        else:
            t.append(a)
    return " ".join(t)

s = "Java is the best, but PHP is the bestest!"
d = censor(s)
print(d)




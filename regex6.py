def rev(sentence):
    l = sentence.split()
    l.reverse()
    print (*[l[i] for i in range(len(l))], sep= ' ')
rev(input())
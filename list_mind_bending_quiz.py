def extendlist(val,list=[]):
    list.append(val)
    return list

extendlist(10) # 10 appended in the default list.
extendlist(123,[]) #123 is appended in the new list not the appended list
extendlist("a")# a is appended in the default list. in which 10 was alreadly present.

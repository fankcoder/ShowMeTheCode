with open('words.txt','r') as f:
    lines = f.readlines()
flag = False
comment = raw_input()
def rinput():
    for each in lines:
        each = each.strip()
        if each in comment:
            Freedom = comment.replace(each,'***')
            print Freedom
        else:
            print "Human Rights"
rinput()

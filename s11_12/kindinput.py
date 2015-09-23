with open('words.txt','r') as f:
    lines = f.readlines()
flag = False
comment = raw_input()
for each in lines:
    each = each.strip()
    if comment == each:
        print "Freedom"
    else:
        print "Human Rights"

import time

b = [{'name': "Alice", 'profession': "UI/UX Designer", 'age': "27"},
     {'name': "John", 'profession': "QA Engineer", 'age': "33"},
     {'name': "Stuart", 'profession': "Constructor", 'age': "19"}]
print(
    "~~~@@@~~~~~~@@@~~~~~~@@@~~~~~~@@@~~~~@@~~~~~~@@@@@@~~\n~@@~~~@@~~@@~~~@@~~@@~~~@@~~@@~~~@@~~@@~~~~~~@@~~~~~~\n~@@~~~~~~~@@~~~@@~~@@~~~@@~~@@~~~~~~~@@~~~~~~@@~~~~~~\n~@@~~~~~~~@@~~~@@~~@@~~~@@~~@@~~~~~~~@@~~~~~~@@@@@~~~\n~@@~~@@@~~@@~~~@@~~@@~~~@@~~@@~~@@@~~@@~~~~~~@@~~~~~~\n~@@~~~@@~~@@~~~@@~~@@~~~@@~~@@~~~@@~~@@~~~~~~@@~~~~~~\n~~~@@@~~~~~~@@@~~~~~~@@@~~~~~~@@@~~~~@@@@@@~~@@@@@@~~\n")
search = input()
time.sleep(1)
print("~~~~~~~~~~~~~~~~~~~~~~")
print("Searching for", search)
print("~~~~~~~~~~~~~~~~~~~~~~")
print("")
d = list()
for a in b:
    for x in a:
        d.append(a[x])
n = False
for z in d:
    if search == z:
        n = True
        result = search
        break
    elif len(set(search)) - len((set(search)) & set(z)) < 1:
        print("Did you mean", z, "?")
        print("")
        result = z
        n = True
        break
    elif len((set(search)) & set(z)) > 7:
        print("Did you mean", z, "?")
        print("")
        result = z
        n = True
        break
if n == False:
    print("Nothing could be found for", search)
else:
    print("Search results:")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for a in b:
        for x in a:
            if a[x] == result:
                resulto = a
    for x in resulto:
        print("The subject's", x, "is", resulto[x])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

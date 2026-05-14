contacts={'Karim':'012545656','Ahmed':'016343646','Amr':'01367569'}
for key,value in contacts.items():
    print(key,value)
s=input('search for contacts ').capitalize()
if s in contacts.keys():
    print(contacts[s])
else:
    print('not found')
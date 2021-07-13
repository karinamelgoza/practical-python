acronyms = ['lol', 'idk', 'smh', 'tbh']

print(acronyms)

acronyms.append('brb')

print(acronyms)

acronyms.remove('tbh')

print(acronyms)

del acronyms[0]

print(acronyms)

if 'lol' in acronyms:
    print("it's in the list")
else:
    print("it's not in the list")

for i in acronyms:
    print(i)

# dictionaries

acronyms = {
    'lol': 'laugh out loud',
    'idk': "i don't know"
}

acronyms['tbh'] = 'to be honest'

print(acronyms)

sentence = 'idk' + ' what happened ' + 'tbh'
translation = acronyms.get('idk') + ' what happened ' + acronyms.get('tbh')

print('sentence:', sentence)
print('translation:', translation)

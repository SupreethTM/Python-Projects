def vowels_count(new):
    with open(new) as s:
        new = s.read()
    new1 = new.lower()
    vowel = ['a','e','i','o','u']
    new_vowel = []
    count = 0
    for n in new1:
        if n in vowel:
            count += 1
            new_vowel.append(n)
    print(f'Then number of vowel avaliable in file is : {count}')
    print(f'The letters avaliable in the file {new_vowel}')
    
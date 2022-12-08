def write_using_c_language(phrase):
    alphabet = dict()
    alphabet['letter_space'] = ['  ','  ','  ','  ','  ','  ','  ','  ','  ']
    alphabet['A'] = [' CCCCCC ',
                     'CC    CC',
                     'CC    CC',
                     'CC    CC',
                     'CCCCCCCC',
                     'CC    CC',
                     'CC    CC',
                     'CC    CC',
                     'CC    CC']
    alphabet['B'] = ['CCCCCCC  ',
                     'CC    CC ',
                     'CC     CC',
                     'CC    CC ',
                     'CCCCCCC  ',
                     'CC    CC ',
                     'CC     CC',
                     'CC    CC ',
                     'CCCCCCC  ']
    alphabet['C'] = ['  CCCCC ',
                     ' CC    C',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     ' CC    C',
                     '  CCCCC ']
    alphabet['D'] = ['CCCCCCC  ',
                     'CC    CC ',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC    CC ',
                     'CCCCCCC  ']
    alphabet['E'] = ['CCCCCCCC',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CCCCCC  ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CCCCCCCC']
    alphabet['I'] = ['CC',
                     '  ',
                     'CC',
                     'CC',
                     'CC',
                     'CC',
                     'CC',
                     'CC',
                     'CC']
    alphabet['L'] = ['CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CCCCCCCC']
    alphabet['M'] = ['CCC       CCC',
                     'CCCC     CCCC',
                     'CC CC   CC CC',
                     'CC  CC CC  CC',
                     'CC   CCC   CC',
                     'CC         CC',
                     'CC         CC',
                     'CC         CC',
                     'CC         CC']
    alphabet['N'] = ['CCC       CC',
                     'CCCC      CC',
                     'CC CC     CC',
                     'CC  CC    CC',
                     'CC   CC   CC',
                     'CC    CC  CC',
                     'CC     CC CC',
                     'CC      CCCC',
                     'CC       CCC']
    alphabet['O'] = [' CCCCCCCC ',
                     'CCC    CCC',
                     'CC      CC',
                     'CC      CC',
                     'CC      CC',
                     'CC      CC',
                     'CC      CC',
                     'CCC    CCC',
                     ' CCCCCCCC ']
    alphabet['P'] = ['CCCCCCC ',
                     'CC    CC',
                     'CC     C',
                     'CC    CC',
                     'CCCCCCC ',
                     'CC      ',
                     'CC      ',
                     'CC      ',
                     'CC      ']
    alphabet['R'] = ['CCCCCCCC',
                     'CC    CC',
                     'CC    CC',
                     'CC    CC',
                     'CCCCCCCC',
                     'CC CC   ',
                     'CC  CC  ',
                     'CC   CC ',
                     'CC    CC']
    alphabet['S'] = [' CCCCCCC',
                     'CCC     ',
                     'CC      ',
                     'CCC     ',
                     ' CCCCCC ',
                     '     CCC',
                     '      CC',
                     '     CCC',
                     'CCCCCCC ']
    alphabet['U'] = ['CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CCC   CCC',
                     ' CCCCCCC ']
    alphabet['V'] = ['CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     'CC     CC',
                     ' CC   CC ',
                     '  CC CC  ',
                     '   CCC   ']
    
    phrase = phrase.upper()
    words = phrase.split(' ')
    for word in words:
        list_to_print = ['','','','','','','','','']
        for letter in word:
            if letter in alphabet:
                for i in range(9):
                    list_to_print[i] = list_to_print[i] + alphabet[letter][i] + alphabet['letter_space'][i]
        print('')
        for i in range(9):
            print(list_to_print[i])

print('Running Unit tests...')
print('All tests passed!')
write_using_c_language('parabens pra voce')
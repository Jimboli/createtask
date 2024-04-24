def InputLoop():
    a = True
    InputFile = input('Enter file name to process: ')

    while a:
        try:
            InputFile = InputFile.strip()
            open(InputFile, 'r')
            a = False
        except:
            print(f"File name {InputFile} doesn't exist. ")
            print('Please enter correct file name.')
            InputFile = input('Please enter file name to process: ')

    return InputFile


def FunctionParser():
    FileName = InputLoop()
    print('Here is a list of top 5 email users: ')
    print('====================================')
    OpenFile = open(FileName, 'r')

    FileDictionary = dict()

    for line in OpenFile:
        if line.startswith('From'):
            SpaceSplit = line.split()
            Email_Address=SpaceSplit[1]
            if Email_Address not in FileDictionary:
                FileDictionary[Email_Address] = 1
            else:
                FileDictionary[Email_Address] = FileDictionary.get(Email_Address) + 1

        else:
            continue

    SortedTuples = (sorted([(v,k) for k,v in FileDictionary.items()]))
    SortedTuples = sorted(SortedTuples, reverse=True)

    for i in range(0, 5):
        print("%s     $%s" % (SortedTuples[i][0], SortedTuples[i][1]))


loop = 'y'
while loop == 'y':
    FunctionParser()
    print('====================================')
    loop = input('Do you want to try another file? (y or n)')


print('Thank you for playing. ')
print('>>>')

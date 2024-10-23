Calls = 0

def count_calls ():
    global Calls
    Calls += 1

def  string_info (string ):
    count_calls()
    return (len(string),string.upper(), string.lower())



def  is_contains (string, list_to_search):
    count_calls()
    return string.lower() in [string.lower() for string in list_to_search]






print(string_info('Капибара'))
print(string_info('Армагеддон'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Городской ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # Совпадений нет
print(Calls)
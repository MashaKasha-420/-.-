calls = 0
def count_calls ():
    global calls
    calls += 1


def string_info (string:str):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains (string:str, list_to_search:list):
    count_calls()
    string = string.lower()
    for element in list_to_search:
        if element.lower() == string:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

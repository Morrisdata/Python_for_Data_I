########################################################
## KEYWORD ARGUMENTS AND DEFAULT PARAMETER VALUES
########################################################
"""
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description('The Lord of the Rings', 'J. R. R. Tolkien', 'George Allen & Unwin', 
                       1954, 1.0, 22, 456)
"""

"""
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', 
                       publisher='George Allen & Unwin',
                       year=1954, 
                       author='J. R. R. Tolkien', 
                       version=1.0,
                       num_pages=456, 
                       num_chapters=22)
"""

"""
def split_check(amount, num_people, tax_rate, tip_rate):
    # ...
split_check(125.00, tip_rate=0.15, num_people=2, tax_rate=0.095)


"""

"""
def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')

print_date(30, 7, 2012, 0)
print_date(30, 7, 2012, 1)
print_date(30, 7, 2012)




##################################
## ARBITRARY ARGUMENT LISTS AFTER COMPLETING CLASS ONCE
##################################
def sandwich(bread, meat, *args): 
    print('%s on %s' % (meat, bread), end=' ') 
    if len(args) > 0: 
        print('with', end=' ') 
    for extra in args: 
        print(extra, end=' ') 
    print("")


sandwich('sourdough', 'turkey', 'mayo')
sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')

"""
def sandwich(bread, meat, **kwargs):
    print('%s on %s' % (bread, meat))
    for category, extra in kwargs.items():
        print('   %s: %s' % (category, extra))

sandwich('sourdough', 'turkey', sauce='mayo')
sandwich('wheat', 'ham', sauce1='mustard', veggie1='tomato', veggie2='lettuce')


"""

def gen_command(application, **kwargs):
    command = application
    for argument in kwargs:
        command += ' --%s=%s' % (argument, kwargs[argument])
    return command

print (gen_command('notepad.exe'))  # No options
print (gen_command('Powerpoint.exe', file='pres.ppt', start=True, slide=3))



## RUN a program
from sys import exit 

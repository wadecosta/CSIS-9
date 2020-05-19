# Lab 11 Ascii Art
# Wade Costa

def topline(width, n):
    x = int( (width-2-n)/2 ) # x is leading spaces
    print(' '*x, end='')
    print('/', end='')
    print(' '*n, end='')
    print('\\')

def bottomline(width, n):
    x = int( (width-2-n)/2 )
    print(' '*x, end='')
    print('\\', end='')
    print(' '*n, end='')
    print('/')

# Main Part 1
width = 10
topline(width, 0)
topline(width, 2)
topline(width, 4)
topline(width, 6)
print('<' + ('-'*(width-2)) + '>')
bottomline(width, 6)
bottomline(width, 4)
bottomline(width, 2)
bottomline(width, 0)



# Main Part 2
print('\n'*5)

def pm():
    pm = ('+ - - - - + - - - - +')
    slash = ('/' + ' '*9 + '/' + ' '*9 + '/')

    print(pm)
    print((slash + '\n')*3 + slash )
    print(pm)
    print((slash + '\n')*3 + slash )

    print(pm)

pm()

# Main Part 3
print('\n'*5)

def letterW():
    print('\\' + ' '*6 + '/\\'+ ' '*6 + '/')
    print(' ' + '\\' + ' '*4 + '/' + ' '*2 + '\\' + ' '*4 + '/')
    print(' '*2 + '\\' + ' '*2 + '/' + ' '*4 + '\\' + ' '*2 + '/')
    print(' '*3 + '\\' + '/' + ' '*6 + '\\' + '/')

  

def letterA():
    print(' '*7 + '/\\' + ' '*7)
    print(' '*6 + '/' + ' '*2 + '\\' + ' '*6)
    print(' '*5 + '/' + '-'*4 + '\\' + ' '*5)
    print(' '*4 + '/' + ' '*6 + '\\' + ' '*4)
    print(' '*3 + '/' + ' '*8 + '\\' + ' '*2)


def letterD():
    print(' '*3 + '|' + '-'*8 + '>')
    print(' '*3 + '|' + ' '*9 + '>')
    print(' '*3 + '|' + ' '*10 + '>')
    print(' '*3 + '|' + ' '*10 + '>')
    print(' '*3 + '|' + ' ' *9 + '>')
    print(' '*3 + '|' + '-'*8 + '>')

def letterE():
    print(' '*3 + '|' + '-'*10 + '|')
    print(' '*3 + '|')
    print(' '*3 + '|' + '-'*10 + '|')
    print(' '*3 + '|')
    print(' '*3 + '|' + '-'*10 + '|')
    
    


# Add a tree next to the letters
letterW()
print('\n'*2)
letterA()
print('\n'*2)
letterD()
print('\n'*2)
letterE()


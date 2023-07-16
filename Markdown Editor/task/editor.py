def header():
    while True:
        lvl = int(input('Level: '))
        if 1 <= lvl <= 6:
            break
        print('The level should be within the range of 1 to 6')
    txt = input('Text: ')
    return f"{'#'*lvl} {txt}\n"


def plain():
    txt = input('Text: ')
    return f"{txt}"


def bold():
    txt = input('Text: ')
    return f"{'**'}{txt}{'**'}"


def italic():
    txt = input('Text: ')
    return f"{'*'}{txt}{'*'}"


def inlinecode():
    txt = input('Text: ')
    return f"{'`'}{txt}{'`'}"


def newline():
    return f"\n"


def link():
    lbl = input('Label: ')
    url = input('URL: ')
    return f"[{lbl}]({url})"


def orderedlist():
    ls = ""
    while True:
        rows = int(input('Number of rows: '))
        if rows > 0:
            break
        print('The number of rows should be greater than zero')
    for row in range(1, rows+1):
        txt = input(f'Row #{row}')
        ls += f"{row}. {txt}\n"
    return ls


def unorderedlist():
    ls = ""
    while True:
        rows = int(input('Number of rows: '))
        if rows > 0:
            break
        print('The number of rows should be greater than zero')
    for row in range(1, rows+1):
        txt = input(f'Row #{row}')
        ls += f"* {txt}\n"
    return ls


def menu():
    text = ''
    while True:
        com = input('Choose a formatter: ')
        if com == 'plain':
            text += plain()
            print(text)
        elif com == 'bold':
            text += bold()
            print(text)
        elif com == 'italic':
            text += italic()
            print(text)
        elif com == 'inline-code':
            text += inlinecode()
            print(text)
        elif com == 'link':
            text += link()
            print(text)
        elif com == 'header':
            text += header()
            print(text)
        elif com == 'new-line':
            text += newline()
            print(text)
        elif com == 'ordered-list':
            text += orderedlist()
            print(text)
        elif com == 'unordered-list':
            text += unorderedlist()
            print(text)
        elif com == '!help':
            print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\nSpecial commands: !help !done')
        elif com == '!done':
            output = open('output.md', 'w')
            output.write(text)
            output.close()
            break
        else:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    menu()


text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed felis eget velit aliquet sagittis id consectetur. Suscipit adipiscing bibendum est ultricies integer quis auctor elit sed. 

Fames ac turpis egestas sed. Enim praesent elementum facilisis leo vel fringilla est ullamcorper. Cras ornare arcu dui vivamus arcu. Vitae turpis massa sed elementum tempus egestas sed. In cursus turpis massa tincidunt dui. Dui accumsan sit amet nulla facilisi morbi tempus iaculis. Tincidunt praesent semper feugiat nibh sed. Lorem mollis aliquam ut porttitor leo a. Suscipit tellus mauris a diam maecenas. Est ante in nibh mauris cursus mattis molestie a. At consectetur lorem donec massa sapien faucibus et molestie ac. Amet purus gravida quis blandit. In vitae turpis 

massa sed elementum tempus egestas sed. Urna porttitor rhoncus dolor purus non enim praesent elementum. Integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque. At imperdiet dui accumsan sit amet nulla facilisi. Eget mauris pharetra et ultrices neque ornare aenean euismod. Et leo duis ut diam quam nulla porttitor. Vitae suscipit tellus mauris a diam maecenas sed enim. Eget nulla facilisi etiam dignissim diam quis enim lobortis. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras. Suspendisse potenti nullam ac tortor vitae purus faucibus. At ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget. Non enim praesent elementum facilisis leo vel fringilla. '''

# split text with split() method.
text = text.lower()
# split makes it as a list
f_text  = text.split(' ')

for char in f_text:
    if ',' in char:
        print(char)
        f_text[f_text.index(char)] = char.replace(',','')
        print(char)
    if '.' in char:
        print(char)
        f_text[f_text.index(char)] = char.replace('.','')
        print(char)
    if '\n' in char:
        f_text[f_text.index(char)] = char.replace('\n','')
        
print(f_text)

for char in f_text:
    print(char)
word_search = input("Check if the word exists in the text: ")
counter = 0

for w in f_text:
    if w == word_search:
        counter += 1

print(f'A word {w} appears {counter} times in the text. ')


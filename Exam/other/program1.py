# 2. b) WAP to read the contents of text file and store all even length words in even.txt and
# all odd length files in odd.txt files respectively.

f = open('other/text1.txt')
content = f.read().split()
f.close()

evenFile = open('other/even.txt', 'w')
oddFile = open('other/odd.txt', 'w')

for word in content:
    if len(word) % 2 == 0:
        evenFile.write(word + ' ')
    else:
        oddFile.write(word + ' ')

evenFile.close()
oddFile.close()
with open('dataset.txt') as data:
    line = data.readline()
    letter = ''
    letters_number = ''
    total_str = ''
    length = len(line)

    for i in range(length - 1):
        if 65 <= ord(line[i]) <= 122:
            for j in range(i + 1, length):
                if '0' <= line[j] <= '9':
                    letters_number += line[j]
                else:
                    letter = line[i]
                    print(letter, int(letters_number))
                    for y in range(int(letters_number)):
                        total_str += letter
                    letters_number = ''
                    break

with open('processed.txt', 'w') as data:
    data.write(total_str)


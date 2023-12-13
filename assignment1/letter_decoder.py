replacements = {
        '!': 's',
        '@': 'h',
        '#': 'e',
        '$': 'r',
        '%': 'l',
        '^': 'o',
        '&': 'c',
        '*': 'k'
    }


# decoding the content of the file
def decode(text):
    decoded_text = ''.join(replacements.get(c, c) for c in text)
    return decoded_text


# reading the file
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


# writing the decoded text to a new file
def write_file(file_name, decoded_text):
    with open(file_name, 'w') as decoded_file:
        decoded_file.write(decoded_text)


# extracting the words starting with 'a' or 'A' in a list and displaying them
def select_a_words(decoded_text):
    words_with_a = [word for word in decoded_text.split() if word.startswith('a') or word.startswith('A')]
    print(words_with_a)


def file_processing():
    text = read_file('sherlock.txt')
    decoded_text = decode(text)
    write_file('sherlock_decoded_letter.txt', decoded_text)
    select_a_words(decoded_text)


if __name__ == '__main__':
    file_processing()

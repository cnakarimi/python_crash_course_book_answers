def count_occurences_file(f, to_count):
    try:
        with open(f) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("File not found")
    else:
        s = ''
        for l in lines:
            if l.isspace():
                continue
            s += l.strip()

        return s.lower().count(to_count)


file_name = 'redemption.txt'
print(count_occurences_file(file_name, 'the '))

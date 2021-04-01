def split_str(str):
    head, num = '', ''
    i = 0
    while i < len(str):
        if str[i].isdigit():
            break
        head += str[i].lower()
        i += 1
    while i < len(str):
        if not str[i].isdigit():
            break
        num += str[i]
        i += 1

    return head, int(num)


def solution(files):
    sorted_files = []
    for f in files:
        sorted_files.append((f, *split_str(f)))
    sorted_files.sort(key=lambda x: (x[1], x[2]))

    return [file[0] for file in sorted_files]


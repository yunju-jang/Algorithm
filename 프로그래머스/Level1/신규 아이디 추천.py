def solution(new_id):
    # 1
    new_id = new_id.lower()
    #2
    temp_id = ''
    for c in new_id:
        if c.isalnum() or c in '-_.':
            temp_id += c
    #3
    while ".." in temp_id:
        temp_id = temp_id.replace('..', '.')
    #4
    if temp_id[0] == ".":
        new_id = temp_id[1:]
        if len(new_id) != 0 and new_id[-1] == '.':
            new_id = new_id[:-1]
    elif temp_id[-1] == ".":
        new_id = temp_id[:-1]
    #5
    if len(new_id) == 0:
        new_id = "a"
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    #7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id
def decode(message_file):
    # Read all lines from the file
    with open(message_file) as msg_file:
        msg_lines = msg_file.readlines()
        
    # Split each line into a tuple(Key, Value) and add it to a dictionary
    msg_dict = {}
    for msg in msg_lines:
        pair = msg.split(' ')
        if pair[0]:
            msg_dict.update({int(pair[0]): pair[1].strip()})
            
    # Sort the dictionary ascending by key
    msg_dict = dict(sorted(msg_dict.items()))

    # Decode the message using the pyramid pattern
    msg = ''
    key = 1
    pyramid_line = 1
    n = len(msg_dict)
    while key <= n:
        if key == n:
            msg = msg + str(msg_dict[key])
        else:
            msg = msg + str(msg_dict[key]) + ' '
        pyramid_line = pyramid_line + 1
        key = key + pyramid_line
            
    return msg

print(decode('coding_qual_input.txt'))
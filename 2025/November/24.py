def is_valid_message(message, validation):
    w=message.split()
    r=""
    for i in w:
        r+=i[0].lower()
    return True if r==validation.lower() else False
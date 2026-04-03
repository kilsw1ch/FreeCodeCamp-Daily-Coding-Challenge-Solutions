def send_message(route):
    r=-0.5
    for i in route:
        r+=0.5
        r+=i/300000
    return round(r,4)
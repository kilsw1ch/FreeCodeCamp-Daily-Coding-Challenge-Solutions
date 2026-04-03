def classification(temp):
    if temp>=0 and temp<3700:
        return "M"
    if temp>3699 and temp<5200:
        return "K"
    if temp>5199 and temp<6000:
        return "G"
    if temp>5999 and temp<7500:
        return "F"
    if temp>7499 and temp<10000:
        return "A"
    if temp>9999 and temp<30000:
        return "B"
    if temp>29999:
        return "O"
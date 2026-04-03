def get_sign(date_str):
    a=date_str[5:7]+date_str[8:]
    a=int(a)
    if a>=120 and a<=218:
        return "Aquarius"
    if a>=219 and a<=320:
        return "Pisces"
    if a>=321 and a<=419:
        return "Aries"
    if a>=420 and a<=520:
        return "Taurus"
    if a>=521 and a<=620:
        return "Gemini"
    if a>=621 and a<=722:
        return "Cancer"
    if a>=723 and a<=822:
        return "Leo"
    if a>=823 and a<=922:
        return "Virgo"
    if a>=923 and a<=1022:
        return "Libra"
    if a>=1023 and a<=1121:
        return "Scorpio"
    if a>=1122 and a<=1221:
        return "Sagittarius"
    else:
        return "Capricorn" 
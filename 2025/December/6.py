def format_date(date_string):
    ds=date_string
    y=(ds[-4]+ds[-3]+ds[-2]+ds[-1]).replace(' ','')
    w=ds.split()
    m=w[0]
    match(m):
        case "January":m="01"
        case "February":m="02"
        case "March":m="03"
        case "April":m="04"
        case "May":m="05"
        case "June":m="06"
        case "July":m="07"
        case "August":m="08"
        case "September":m="09"
        case "October":m="10"
        case "November":m="11"
        case "December":m="12"
    d=w[1].replace(',','')
    if len(d)>1:
        return f"{y}-{m}-{d}"
    else:
        return f"{y}-{m}-0{d}"
def get_semifinal_matchups(teams):
    d={}
    for i in teams:
        d[i[:3]]=int(i[5])*3+int(i[7])*2+int(i[9])
    t=list(sorted(d.items(), key=lambda kv: kv[1], reverse=True))
    t1=str(t[0])
    t2=str(t[1])
    t3=str(t[2])
    t4=str(t[3])
    return f"The semi-final games will be {t1[2:5]} vs {t4[2:5]} and {t2[2:5]} vs {t3[2:5]}."
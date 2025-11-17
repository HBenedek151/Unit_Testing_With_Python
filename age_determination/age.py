def categorise_by_age(age):
    if 126 <= age:
        return "halott"
    elif 66 <= age:
        return "idős"
    elif 19 <= age:
        return "felnőtt"
    elif 10 <= age:
        return "gyerek"
    elif 0 <= age:
        return "baba" 
    else:
        return "hibás adat"
    
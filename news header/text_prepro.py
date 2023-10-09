def text_prepro(t):
    import re

    patturn = r'\([^)]*\)'
    t = re.sub(pattern=patturn, repl='', string=str(t))

    patturn = r'\[[^)]*\]'
    t = re.sub(pattern=patturn, repl='', string=str(t))

    patturn = r'\<[^)]*\>'
    t = re.sub(pattern=patturn, repl='', string= str(t))

    patturn = r'\{]^)]*\}'
    t = re.sub(pattern=patturn, repl='', string=str(t))

    patturn = r['^a-zA-Z가-힣']
    t = re.sub(pattern=patturn, repl='', string= str(t))

    t_split = t.split()
    t_list = []
    for i in t_split :
        if len(i) !=1 :
            t_list.append(i)


    return t_list

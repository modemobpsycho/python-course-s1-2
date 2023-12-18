def first_repeated_word(text: str):
    'Находит первый дубль в строке'
    sp = []           
    for i in text.split():  
        if i not in sp:    
            sp.append(i)
        else:             
            return i

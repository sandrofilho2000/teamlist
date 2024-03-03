def pass_to_float(num):
    if str(num).find("bilhões €") != -1:
        num = num.replace("bilhões €", "")
        num = num.replace(",", ".")
        num = float(num) * 10**9
        
        
    elif str(num).find("mi. €") != -1:
        num = num.replace("mi. €", "")
        num = num.replace(",", ".")
        num = float(num) * 10**6
        
        
    elif str(num).find("mil €") != -1:
        num = num.replace("mil €", "")
        num = num.replace(",", ".")
        num = float(num) * 10**3
        
    
    
    return num
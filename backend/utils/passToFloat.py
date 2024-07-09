def pass_to_float(num):
    if str(num).find("bilhões €") != -1:
        num = num.replace("bilhões €", "")
        num = num.replace(",", ".")
        num = float(num) * 10**9
        
        
    elif str(num).find("mi. €") != -1:
        num = num.replace("mi. €", "")
        num = num.replace(",", ".")
        num = float(num) * 10**6
        
        
    elif str(num).find("mil €") != -1 or str(num).find("k") != -1 :
        num = num.replace("mil €", "")
        num = num.replace("k", "")
        num = num.replace("€", "")
        num = num.replace(",", ".")
        num = float(num) * 10**3
            
        
    elif str(num).find("m") != -1 :
        num = num.replace("m", "")
        num = num.replace("€", "")
        num = num.replace(",", ".")
        num = float(num) * 10**6
        
        
           
    elif str(num).find("-") != -1 :
        num = 0
    
    
    return num
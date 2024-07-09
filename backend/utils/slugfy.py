from unidecode import unidecode
import re

def slugfy(input_string):
    # Remove acentos e caracteres especiais
    normalized_string = unidecode(input_string)
    
    # Substitui espaços em branco por "-"
    slug = re.sub(r'\s+', '-', normalized_string)
    
    # Remove caracteres especiais (exceto '-' e '_')
    slug = re.sub(r'[^a-zA-Z0-9-_]', '', slug)
    
    return slug.lower()


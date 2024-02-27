def validar_transacao(transacao):
    if 'valor' not in transacao or not isinstance(transacao['valor'], (int, float)):
        return False, 'O campo "valor" é obrigatório e deve ser um número.'
    if 'descricao' not in transacao or not isinstance(transacao['descricao'], str):
        return False, 'O campo "descricao" é obrigatório e deve ser uma string.'
    if 'tipo_da_transacao' not in transacao or transacao['tipo_da_transacao'] not in ['entrada', 'saida']:
        return False, 'O campo "tipo_da_transacao" é obrigatório e deve ser "entrada" ou "saida".'
    return True, None
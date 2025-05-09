def seguido (n):
    if '01' in str(n):
        return True
    elif '12' in str(n):
        return True
    elif '23' in str(n):
        return True
    elif '34' in str(n):
        return True
    elif '45' in str(n):
        return True
    elif '56' in str(n):
        return True
    elif '67' in str(n):
        return True
    elif '78' in str(n):
        return True
    elif '89' in str(n):
        return True
    else:
        return False

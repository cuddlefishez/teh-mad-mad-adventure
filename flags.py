def editflag(x,y,flags):
    """
     This funcation takes 3 parameters (x,y,flags). x being the value you wish to edit.
     y determines whether x is appended or removed (0 to remove, 1 to append).
     Finally flags is the list containing all active flags
    """
    count = flags.count(x)
    if y == 0 and count > 0:
        flags.remove(x)
    elif y == 0 and count == 0:
        print('The value', x ,'does not exist in flags.')
    elif y == 1 and count == 0:
        flags = flags.append(x)
    elif y == 1 and count > 0:
        print('The value', x ,'already exists in flags')
    else:
        print('editflag command was used incorrectly.')
    return(flags)
def flagcheck(x,y,flags):
    if y == 0:
        return(x not in flags)
    elif y == 1:
        return(x in flags)
    else:
        print('flagcheck command was used incorrectly.')

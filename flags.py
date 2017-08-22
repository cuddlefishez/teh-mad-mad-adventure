def editflag(x,y,flags):
    count = flags.count(x)
    if y == 0 and count > 0:
        flags.remove(x)
    elif y == 1:
        flags = flags.append(x)
    return(flags)
def check_bit4(input):
    num = input
    mask = 0b1000
    desired = num & mask
    if desired > 0:
        return "on"
    else:
        return "off"
print check_bit4(0b11000)

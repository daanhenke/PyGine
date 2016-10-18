import math


bit15_max_value = 0x7FFF
bit15_mask_red = 0x7C00
bit15_mask_green = 0x03E0
bit15_mask_blue = 0x001F

def bit15_to_tuple(bit15):
    red = (bit15 & bit15_mask_red) >> 10
    green = (bit15 & bit15_mask_green) >> 5
    blue = (bit15 & bit15_mask_blue)

    #print "5 BIT RGB VALUES:"
    #print red, green, blue

    red = math.floor(red * 8.25)
    green = math.floor(green * 8.25)
    blue = math.floor(blue * 8.25)

    #print "8 BIT RGB VALUES:"
    #print red, green, blue

    return (red, green, blue)

if __name__ == '__main__':
    bit15_to_tuple(0x7C1F)



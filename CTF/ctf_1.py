'''
1. Ce mesaj este ascuns in urmatoarea secventa de numere ?
5,0,6,1,7,2,6,15,6,12,6,1,2,0,6,12,6,1,2,0,6,1,6,3,6,5,6,1,7,3,7,4,6,1,2,0,7,0,7,2,6,15,6,2,6,12,6,5,6,13,6,1,2,0,6,5,7,3,7,4,6,5,2,0,2,7,6,1,6,2,7,2,6,1,6,11,6,1,6,4,6,1,6,2,7,2,6,1,2,7,
Problema online: 20 puncte, postata pe 03.Mai.2017 16:00
'''


message = [5, 0, 6, 1, 7, 2, 6, 15, 6, 12, 6, 1, 2, 0, 6, 12, 6, 1, 2, 0,
 6, 1 ,6, 3, 6, 5, 6, 1, 7, 3, 7, 4, 6, 1, 2, 0, 7, 0, 7 , 2, 6,
 15, 6, 2, 6, 12, 6, 5, 6, 13, 6, 1, 2, 0, 6, 5, 7, 3, 7, 4, 6, 5,
 2, 0, 2, 7, 6, 1, 6, 2, 7, 2, 6, 1, 6, 11, 6, 1, 6, 4, 6, 1, 6, 2,
 7, 2, 6, 1, 2, 7]

hex_hash = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }

def getHexs():
    hex_message = []
    for i in xrange(0, len(message), 2):
        hex_comp_1_str = hex_hash[message[i]] if message[i] > 9 else str(message[i])
        hex_comp_2_str = hex_hash[message[i+1]] if message[i+1] > 9 else str(message[i+1])
        hex_string = hex_comp_1_str + hex_comp_2_str
        hex_string = '0x' + hex_string
        hex_message.append(hex_string)
        i += 1
    return hex_message

if __name__ == '__main__':
    print getHexs()
    decs_s = map(lambda hex_c: int(hex_c, 16), getHexs())

    print ''.join(map(lambda c: chr(c), decs_s))

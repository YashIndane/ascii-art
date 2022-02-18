import os
import cv2
from colorama import Fore

#Maps pixel values to ASCII character
def mapper(r: int, g: int, b: int) -> str:
    PIXEL_DENSITY = '¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;"^:,..`'
    avg = (int(r) + int(g) + int(b))//3
    if 0<= avg <=60: return " "
    elif 60<= avg <=62: return "."
    elif 63<= avg <=65: return "."
    elif 66<= avg <=68: return  "."
    elif 69<= avg <=71: return  "."
    elif 72<= avg <=74: return  "."
    elif 75<= avg <=77: return   "."
    elif 78<= avg <=80: return   "."
    elif 81<= avg <=83: return    ";"
    elif 84<= avg <=86: return  "*"
    elif 90<= avg <=92: return "!"
    elif 93<= avg <=95: return  "²"
    elif 96<= avg <=98: return "¤"
    elif 99<= avg <=101: return "/"
    elif 102<= avg <=104: return "r"
    elif 105<= avg <=107: return "("
    elif 108<= avg <=110: return  "?" 
    elif 111<= avg <=113: return  "+"
    elif 114<= avg <=116: return  "¿"
    elif 117<= avg <=119: return  "c"
    elif 120<= avg <=122: return  "L"
    elif 123<= avg <=125: return  "ª"
    elif 126<= avg <=128: return  "7"
    elif 129<= avg <=131: return  "t"
    elif 132<= avg <=134: return  "1"
    elif 135<= avg <=137: return  "f"
    elif 138<= avg <=140: return  "J"
    elif 141<= avg <=143: return   "C"
    elif 144<= avg <=146: return   "Ý"
    elif 147<= avg <=149: return  "y"
    elif 150<= avg <=152: return   "¢"
    elif 153<= avg <=155: return   "z"
    elif 156<= avg <=158: return    "F"
    elif 159<= avg <=161: return   "3"
    elif 162<= avg <=164: return   "±"
    elif 165<= avg <=167: return  "%"
    elif 168<= avg <=170: return  "S"
    elif 171<= avg <=173: return    "2"
    elif 174<= avg <=176: return  "k"
    elif 177<= avg <=179: return   "ñ"
    elif 180<= avg <=182: return   "5"
    elif 183<= avg <=185: return   "A"
    elif 186<= avg <=188: return    "Z"
    elif 189<= avg <=191: return   "X"
    elif 192<= avg <=194: return   "G"
    elif 195<= avg <=197: return     "$"
    elif 198<= avg <=200: return    "À"
    elif 201<= avg <=203: return     "0"
    elif 204<= avg <=206: return     "Ã"
    elif 207<= avg <=209: return    "m"
    elif 210<= avg <=212: return    "&"
    elif 213<= avg <=215: return     "Q"
    elif 216<= avg <=218: return    "8"
    elif 219<= avg <=221: return      "#"
    elif 222<= avg <=224: return    "R"
    elif 225<= avg <=227: return    "Ô"
    elif 228<= avg <=230: return     "ß"
    elif 231<= avg <=233: return   "Ê"
    elif 234<= avg <=236: return   "N"
    elif 237<= avg <=239: return   "B"
    elif 240<= avg <=242: return    "å"
    elif 243<= avg <=245: return    "M"
    elif 246<= avg <=248: return     "Æ"
    elif 249<= avg <=251: return     "Ø"
    elif 252<= avg <=254: return     "@"
    elif 255<= avg <=257: return     "@"
    return "."


def map_driver(image) -> str:
    asc_string = ""
    for row in image:
        for pixel in row:
            r, g, b = pixel
            asc_string += mapper(r, g, b) + " "
        asc_string += "\n"  
    return asc_string  


if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    os.system("cls")

    while True:
        check, frame = cam.read()
        half = cv2.resize(frame, (0, 0), fx=0.1, fy=0.1)
        ascii_string = map_driver(half)
        os.system("cls")
        print(Fore.GREEN + ascii_string) 

        key = cv2.waitKey(1)
        if key == 13:
            break

    cam.release()
    cv2.destroyAllWindows()
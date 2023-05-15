import os
import cv2
from colorama import Fore

#Maps pixel values to ASCII character
def mapper(r: int, g: int, b: int) -> str:
    PIXEL_DENSITY = '¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;"^:,..`'
    avg = (int(r) + int(g) + int(b))//3
    if 0<= avg <=2: return "¶"
    elif 3<= avg <=5: return "@"
    elif 6<= avg <=8: return "Ø"
    elif 9<= avg <=11: return "Æ"
    elif 12<= avg <=14: return "M"
    elif 15<= avg <=17: return "å"
    elif 18<= avg <=20: return "B"
    elif 21<= avg <=23: return "N"
    elif 24<= avg <=26: return "Ê"
    elif 27<= avg <=29: return "ß"
    elif 30<= avg <=32: return "Ô"
    elif 33<= avg <=35: return "R"
    elif 36<= avg <=38: return "#"
    elif 39<= avg <=41: return "8"
    elif 42<= avg <=44: return "Q"
    elif 45<= avg <=47: return "&"
    elif 48<= avg <=50: return "m"
    elif 51<= avg <=53: return "Ã"
    elif 54<= avg <=56: return "0"
    elif 57<= avg <=59: return "À"
    elif 60<= avg <=62: return "$"
    elif 63<= avg <=65: return "G"
    elif 66<= avg <=68: return "X"
    elif 69<= avg <=71: return "Z"
    elif 72<= avg <=74: return "A"
    elif 75<= avg <=77: return "5"
    elif 78<= avg <=80: return "ñ"
    elif 81<= avg <=83: return "k"
    elif 84<= avg <=86: return "2"
    elif 87<= avg <=89: return "S"
    elif 90<= avg <=92: return "%"
    elif 93<= avg <=95: return "±"
    elif 96<= avg <=98: return "3"
    elif 99<= avg <=101: return "F"
    elif 102<= avg <=104: return "z"
    elif 105<= avg <=107: return "¢"
    elif 108<= avg <=110: return "y"
    elif 111<= avg <=113: return "Ý"
    elif 114<= avg <=116: return "C"
    elif 117<= avg <=119: return "J"
    elif 120<= avg <=122: return "f"
    elif 123<= avg <=125: return "1"
    elif 126<= avg <=128: return "t"
    elif 129<= avg <=131: return "7"
    elif 132<= avg <=134: return "ª"
    elif 135<= avg <=137: return "L"
    elif 138<= avg <=140: return "c"
    elif 141<= avg <=143: return "¿"
    elif 144<= avg <=146: return "+"
    elif 147<= avg <=149: return "?"
    elif 150<= avg <=152: return "("
    elif 153<= avg <=155: return "r"
    elif 156<= avg <=158: return "/"
    elif 159<= avg <=161: return "¤"
    elif 162<= avg <=164: return "²"
    elif 165<= avg <=167: return "!"
    elif 168<= avg <=170: return "*"
    elif 171<= avg <=173: return ";"
    elif 174<= avg <=176: return "."#'"'
    elif 177<= avg <=179: return "."#'^'
    elif 180<= avg <=182: return "."#':'
    elif 183<= avg <=185: return "."#','
    elif 186<= avg <=188: return "."#'.'
    elif 189<= avg <=191: return "."#'.'
    elif 192<= avg <=194: return "."#'`'
    else: return " "


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
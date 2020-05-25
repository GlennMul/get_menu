import json
import time


def upload_menu(menu, num):
    data = menu
    print(data['Category'][num], ":", data['Menu_Item'][num], ":", data['Description'][num], ":", data['Price'][num], ":", data['Image_URL'][num])
    time.sleep(1)
    return menu

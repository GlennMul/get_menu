import json
import time


def upload_menu(menu):
    data = menu
    for i in range(len(data['Category'])):
        print(data['Category'][i], ":", data['Menu_Item'][i], ":", data['Description'][i], ":", data['Price'][i], ":", data['Image_URL'][i])
        time.sleep(1)
    return menu

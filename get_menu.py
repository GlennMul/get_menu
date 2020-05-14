import json
import timeit
import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import Response


# noinspection PyBroadException
def get_menu(url):
    start_time = timeit.default_timer()
    try:
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

        r = requests.get(url, headers=hdr)

        doc = BeautifulSoup(r.text, "html.parser")

        redux_state = doc.find("script", {"id": "__REDUX_STATE__"})

        contents = str(redux_state.contents[0])

        utf_s = contents.replace(r'\u0022', '"')

        json_data = json.loads(utf_s)

        stores = json_data['stores']

        uuid = next(iter(stores.keys()))  # this assumes there is only one key in this dict BAD JUUJUU

        section = next(iter(stores[uuid]['data']['sectionEntitiesMap'].keys()))

        subsect = []
        title = []
        description = []
        price = []
        imageUrl = []

        subs = stores[uuid]['data']['sections'][0]['subsectionUuids']

        for sub in subs:
            category = stores[uuid]['data']['subsectionsMap'][sub]['title']
            items = stores[uuid]['data']['subsectionsMap'][sub]['itemUuids']

            for item in items:
                subsect.append(category)
                title.append(stores[uuid]['data']['sectionEntitiesMap'][section][item]['title'])
                description.append(stores[uuid]['data']['sectionEntitiesMap'][section][item]['description'])
                price.append(
                    "{:.2f}".format((stores[uuid]['data']['sectionEntitiesMap'][section][item]['price']) / 100))
                imageUrl.append(stores[uuid]['data']['sectionEntitiesMap'][section][item]['imageUrl'])

        data = {'Category': subsect,
                'Menu_Item': title,
                'Description': description,
                'Price': price,
                'Image_URL': imageUrl
                }
        df = pd.DataFrame(data)

        print(timeit.default_timer() - start_time)

        # resp = make_response(df.to_csv())
        # resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
        # resp.headers["Content-Type"] = "text/csv"

        return df

    except:
        df = pd.DataFrame({"Invalid URL": []})
        print(timeit.default_timer() - start_time)
        return df

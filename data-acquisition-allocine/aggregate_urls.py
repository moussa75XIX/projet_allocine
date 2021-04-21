# -*- coding: utf-8 -*- #


import os
import glob
import json
import time


PATH_SERIES_COLLECTED = os.path.join(os.curdir, 'urls_series_collected')
PATH_SERIES_AGGREGATED = os.path.join(os.curdir, 'urls_series_aggregated')


def aggregate_series_urls():
    """
    Gathers all the JSON files from the 'urls_series_collected' folder and will
    aggregate them into a single file which will be saved in the 'urls_series_aggregated' folder.
    """

    aggregated_series_urls = []

    # Open all the json file in the folder `PATH_URLS_PRODUCTS_REVIEWS_COLLECTED`
    for json_file in glob.glob(os.path.join(PATH_SERIES_COLLECTED, '*.json')):
        urls_series_collected_files = json.load(open(json_file, 'r'))

        # Save the file with series urls in one aggregated list
        for urls_series_collected_file in urls_series_collected_files:
            aggregated_series_urls.append(urls_series_collected_file)

    with open(os.path.join(PATH_SERIES_AGGREGATED, str(time.strftime("%Y_%m_%d")) + '_aggregated_series_urls_list.json'), 'w') as file_to_dump:
        json.dump(aggregated_series_urls, file_to_dump, indent=4, ensure_ascii=False)


def main():
    aggregate_series_urls()


if __name__ == "__main__":
    main()

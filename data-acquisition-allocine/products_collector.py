# -*- coding: utf-8 -*- #
import time


def init_product_dict():
    """
   Initializes the dictionary with the product data.
   # Returns:
       product_dict: dict, dictionary with the product data.
    """

    product_dict = {
        'url': None,
        'original_title': None,
        'date': None,
        'running_time': None,
        'genres': [],
        'created_by': [],
        'spectators_mean_rating': None,
        'press_mean_rating': None,
        'actors': [],
        'country_of_origin': None,
        'nb_seasons': None,
        'nb_episodes': None,
        'synopsis': None,
        'collect_date': str(time.strftime("%Y_%m_%d")),
    }

    return product_dict


def collect_product_data(driver, url):
    """
    Collects the data of the product on the page `url`.
    # Args:
        driver: selenium driver
        url: str, url of a product.
    # Returns:
        product_dict: dict, dictionary with product's data.
    """

    # Initialize the serie data dictionary
    product_dict = init_product_dict()

    # Url
    try:
        product_dict['url'] = url
    except:
        pass

    # Original title
    try:
        product_dict['original_title'] = driver.find_element_by_class_name('titlebar-link').get_attribute('textContent')
    except:
        pass

    # Date
    try:
        product_dict['date'] = driver.find_element_by_class_name('meta-body-info').get_attribute('textContent').split('/')[0].strip()
    except:
        pass

    # Running time
    try:
        product_dict['running_time'] = driver.find_element_by_class_name('meta-body-info').get_attribute('textContent').split('/')[1].strip()
    except:
        pass

    # Genres
    try:
        genres = driver.find_element_by_class_name('meta-body-info').find_elements_by_class_name('xXx')
        for genre in genres:
            product_dict['genres'].append(genre.get_attribute('textContent').strip())

    except:
        pass

    # Created by
    try:
        creators = driver.find_element_by_xpath('//div[@class="meta-body-item meta-body-direction" and contains(.,"De")]').find_elements_by_class_name('blue-link')
        for creator in creators:
            product_dict['created_by'].append(creator.get_attribute('textContent').replace("\n", "").strip())
    except:
        pass

    # Spectators mean rating
    try:
        product_dict['spectators_mean_rating'] = driver.find_element_by_xpath('//div[@class="rating-item" and contains(.," Spectateurs ")]').find_element_by_class_name('stareval-note').get_attribute('textContent')
    except:
        pass

    # Press mean rating
    try:
        product_dict['press_mean_rating'] = driver.find_element_by_xpath('//div[@class="rating-item" and contains(.," Presse ")]').find_element_by_class_name('stareval-note').get_attribute('textContent')
    except:
        pass

    # Actors
    try:
        actors = driver.find_element_by_xpath('//section[@class="section ovw" and contains(.,"Casting")]').find_elements_by_class_name('meta-title-link')
        for actor in actors:
            product_dict['actors'].append(actor.get_attribute('textContent').replace("\n","").strip())
    except:
        pass

    # Country of origin
    try:
        product_dict['country_of_origin'] = driver.find_element_by_class_name('nationality').get_attribute('textContent').strip()
    except:
        pass

    # Wait for the data to load correctly
    time.sleep(5)

    # Number of seasons
    try:
        try:
            product_dict['nb_seasons'] = int(driver.find_element_by_xpath('//div[@class="stats-numbers-row-item" and contains(.,"Saison")]').find_element_by_class_name('stats-number').get_attribute('textContent'))
        except:
            product_dict['nb_seasons'] = int(driver.find_element_by_xpath('//div[@class="stats-numbers-row stats-numbers-seriespage" and contains(.,"Saisons")]').find_element_by_class_name('stats-number').get_attribute('textContent'))
    except:
        pass

    # Number of episodes
    try:
        product_dict['nb_episodes'] = int(driver.find_element_by_xpath('//div[@class="stats-numbers-row-item" and contains(.,"Episodes")]').find_element_by_class_name('stats-number').get_attribute('textContent'))
    except:
        pass
    # Synopsis
    try:
        product_dict['synopsis'] = driver.find_element_by_class_name('content-txt').get_attribute('textContent').replace("\n","").strip()
    except:
        pass

    return product_dict

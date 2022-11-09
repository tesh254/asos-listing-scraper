import sys

from asos_listing_scraper import Scraper
from store import Store

def main():
    store = Store()

    store.initialize_database()

    if (len(sys.argv) >= 2):
        if (sys.argv[1] == '--asos' and sys.argv[2]):
            scraper = Scraper(sys.argv[2])

            scraper.run()

            store.save_to_db(scraper.product_details)
        if (sys.argv[1] == '--read'):
            store.read_data_from_db()

if __name__ == '__main__':
    main()
# Automated-Price-Scraper
Software automation for scraping a specified item's price from E-Commerce portals

Recommended for use in a development environment, this automated price scraper utilizes the Selenium software automation Python package for data extraction. Apart from the config file, the price scraper and price notify scripts can be used in tandem to achieve the following objectives -

- Extracting the price of an item from an E-Commerce portal
- Inserting the data obtained to a database
- Sending an email to the user when there's a reduction in the price of the selected item

With the assistance of tools like Windows Task Scheduler/Cron, the scripts can be executed automatically everyday(price_scraper.py, followed by price_notify.py) without the need of the use checking the website at regular intervals.

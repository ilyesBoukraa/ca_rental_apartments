import scrapy
from scrapy.crawler import CrawlerProcess
import json 
import re
import random
import time

class MyScraper(scrapy.Spider):
    name = "my_real_estate_scraper"
    def __init__(self):
         self.start_urls = ["https://www.realestate.com.au/international/us/los-angeles-ca/rent/",]
         self.found_apartments = []
         self.stop_criteria = 0

    def parse(self, response):
        apartments = response.xpath('//div[@class="basic-info"]')
         
        for apartment in apartments:
            apartment_details = {}
            apartment_details['property_type'] = apartment.xpath(
                './/div[@class="multi-features "]//div[@class="propertytype"]/text()'
                ).get()
            if apartment_details['property_type']:
               apartment_details['property_type'] = apartment_details['property_type'].strip()

            apartment_details['bedrooms'] = apartment.xpath(
                './/li[@title="Bedrooms"]//strong/text()'
                ).get()
            
            # So I won't get blocked
            delay = random.uniform(0.7, 3.0) 
            time.sleep(delay)

            apartment_details['bathrooms'] = apartment.xpath(
                './/li[@title="Bathrooms"]//strong/text()'
            ).get()
            apartment_details['car_spaces'] = apartment.xpath(
                './/li[@title="Car Spaces"]//strong/text()'
            ).get()

            apartment_details['hous_size_m2'] = apartment.xpath(
                './/li[@title="House Size"]//strong/text()'
                                                             ).get()
            
            
            apartment_details['location'] = apartment.xpath(
                './/address[@class="address"]//a/text()'
                ).get().strip()
             
            
            price_text = apartment.xpath(
                './/div[@class="price"]//p[@class="listing-price specified"]//strong/text()'
            ).get()
            
            # a regular expression to extract the numerical value only 
            #print('price_text: ', price_text)
            price_numeric = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', price_text).group()
            
            #print('price_numeric:',price_numeric)

            apartment_details['price_usd'] = price_numeric
            
            apartment_details['link'] = 'https://www.realestate.com.au/' + apartment.xpath(
                './/div[@class="detail-link-box"]/a/@href'
            ).get()
            
            self.found_apartments.append(apartment_details)


        next_page_url = 'https://www.realestate.com.au' if  self.stop_criteria != 10 else None
        #new_page = response.xpath('//a[@class="next active"]/@href').get() if  self.stop_criteria != 10 else None
        new_page = response.xpath('//link[@rel="next"]/@href').get() if  self.stop_criteria != 10 else None
        
        print(f'new_page: {new_page}')
        next_page_url = next_page_url + new_page if new_page else None  
        print("###########################################################")
        print(f"next_page_url: {next_page_url}")
        print("###########################################################")
        # So I won't get blocked
        delay = random.uniform(0.5, 3.0) 
        time.sleep(delay)

        if next_page_url:
            self.stop_criteria = self.stop_criteria + 1
            print(f'stop_criteria: {self.stop_criteria}')
            yield response.follow(next_page_url, callback=self.parse)
        else:
            self.save_data_as_json()
            
    def save_data_as_json(self):
        with open('apartments.json', 'w') as file:
            json.dump(self.found_apartments, file, indent=4)

                     

            
if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(MyScraper)
    spider = next( iter(process.crawlers) ).spider
    process.start()

    #print( json.dumps(spider.found_apartments ,indent=4) )
    # # Read data from the JSON file
    with open('apartments.json', 'r') as file:
        data = json.load(file)

    # Access and use the data
    for apartment in data:
        print("--------------------")
        print("Property Type:", apartment['property_type'])
        print("Bedrooms:", apartment['bedrooms'])
        print("Bathrooms:", apartment['bathrooms'])
        print("Car Spaces:", apartment['car_spaces'])
        print("House Size (m2):", apartment['hous_size_m2'])
        print("Location:", apartment['location'])
        print("Price (USD):", apartment['price_usd'])
        print("Link:", apartment['link'])
        print("--------------------") 
# California Rental Real Estate:
Note: For the time being, I am still using static websites exclusively until I have properly learned __Selenium__(next project probably).

Tried her to create some real-world example, if you're looking to gather information about rental properties in __California__ such as Property Type, number of Bedrooms, Bathrooms, Car Spaces, House Size (m2), Location, and Price (USD), web scraping and storing the data in a JSON file 
can provide a convenient way to access and analyze the information. By scraping the relevant websites and extracting these details, 
you can create a structured dataset that can be easily queried and filtered using SQL queries.

# Project description:
1. Used __Scrapy__ library to scrap a [real-estate-website](https://www.realestate.com.au/international/us/los-angeles-ca/rent/) which contain informations about __Rent offers__ in California (The scraping process was performed on 11 pages as an example).
2. Implemented random delays during the scraping process to avoid potential blocking by the website. (in this one I didn't had to, but it is good for practicing).
3. Saved the required rental property information in __JSON__ format (check [apartments.json](https://github.com/ilyesBoukraa/ca_rental_apartments/blob/master/apartments.json) ), facilitating easy integration with databases like MySQL later on.
4. Implemented targeted data extraction by using appropriate XPath expressions, ensuring the retrieval of relevant details such as property type, <br> bedrooms, bathrooms, car spaces, house size (m2), location, price (USD), and a link to the offre.
5. Employed the __re__ library and __regular expressions__ to extract and clean specific information, such as isolating the numerical value of the price.
6. Gained proficiency in working with XML queries to extract the desired data accurately from the website.
7. Created a separate file named [test_xpath.py](https://github.com/ilyesBoukraa/ca_rental_apartments/blob/master/test_xpath.py) for testing and verifying the correctness of the XPath expressions used in the project.


![an image containing a part of the code](/imgs/scrapy_code.png)

### This image was created by [Carbon](https://carbon.now.sh/).

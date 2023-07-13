import scrapy

html_code = """
 <link rel="next" href="/international/us/los-angeles-ca/rent/p2/"/> 
"""

response = scrapy.Selector(text=html_code)
text = response.xpath('//link[@rel="next"]/@href').get()
print(text)
print(type(text))

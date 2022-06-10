import scrapy

class WhiskeySpider(scrapy.Spider):
    name = "whiskey"
    start_urls = [
        "https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock"
    ]

    def parse(self, response):
        for product in response.css("div.product.details.product-item-details"):
            yield {
                "product_name" : product.css("a.product-item-link::text").get(),
                "product_link" : product.css("a").attrib["href"],
                "prodcut_price" : product.css("span.price::text").get()
            }
        
        next_page = response.css("a.action.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, self.parse)
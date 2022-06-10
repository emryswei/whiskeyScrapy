import scrapy

class WhiskeySpider(scrapy.Spider):
    name = "whiskey"
    start_urls = [
        "https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock"
    ]

    def parse(self, response):
        product_info = response.css("div.product-item-info")
        for product in product_info:
            try:
                yield {
                    "product_name" : product.css("a.product-item-link::text").get(),
                    "product_link" : product.css("a").attrib["href"],
                    "prodcut_price" : product.css("span.price::text").get(),
                    "product_img_url" : product.css("img").attrib["src"]
                }
            except:
               yield {
                    "product_name" : product.css("a.product-item-link::text").get(),
                    "product_link" : product.css("a").attrib["href"],
                    "prodcut_price" : product.css("span.price::text").get(),
                    "product_img_url" : "unknown"
                } 
        # yield {
        #     "product_name" : product_info[8].css("a.product-item-link::text").get(),
        #     "product_link" : product_info[8].css("a").attrib["href"],
        #     "prodcut_price" : product_info[8].css("span.price::text").get(),
        #     "product_img_url" : product_info[8].css("img").attrib["src"]
        # } 
        next_page = response.css("a.action.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, self.parse)
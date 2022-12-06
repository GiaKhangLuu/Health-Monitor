import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'images'
    start_urls = [
            'https://websosanh.vn/s/omron+hem+7600t.html'
            ]

    def __init__(self):
        self.img_srcs = []
        super().__init__()

    def parse(self, response):
        for product_img in response.css('li.product-item a div.product-item-content span.product-img'):
            img = product_img.css('img.lazyload::attr(data-src)')
            if len(img) == 0:
                img = product_img.css('img::attr(src)')
            img = img.get().split('?compress')[0]

            yield {'src': img}

        next_page = response.css('li a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            


from pathlib import Path
import scrapy



class QuotesSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = [
            "https://www.amazon.in/s?k=mobile"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"amazon-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        for no in range(1, 10):
            # With Rating and Amazon tag
            a = response.xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span/text()').get()

            # With Rating, Without Amazon tag
            b = response.xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/text()').getall()

            if a is not None:
                with open('List_1.txt', 'a') as f:
                    f.writelines(str(a) + '\n')
            if b is not None:
                with open('List_2.txt', 'a') as f:
                    f.writelines(str(b) + '\n')
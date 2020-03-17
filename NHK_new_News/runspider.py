# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main(spider_name):
    settings = get_project_settings()  # FEED_URI='results.json')
    process = CrawlerProcess(settings)
    process.crawl(spider_name)
    process.start()
    print("end")


if __name__ == "__main__":
    test_spider_name = "NHK_new_News"
    main(test_spider_name)

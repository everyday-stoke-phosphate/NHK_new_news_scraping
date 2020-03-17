# -*- coding: utf-8 -*-
import datetime
import json
import urllib.parse

import scrapy


class NhkNewNewsListSpider(scrapy.Spider):
    name = 'NHK_new_News'
    allowed_domains = ['www3.nhk.or.jp']
    start_urls = ['https://www3.nhk.or.jp/news/catnew.html?utm_int=news_contents_news-main_more#!/10/']

    # seleniumを使うために追加
    def __init__(self, *args, **kwargs):
        super(NhkNewNewsListSpider, self).__init__(*args, **kwargs)
        # 初期変数を作成
        self.json_number = 1
        self.time_stamp = int(datetime.datetime.now().timestamp() * 1000)

    def start_requests(self):  # response追加
        # 開始するURLをリストに
        url = self.make_next_url()
        yield scrapy.Request(url)
        # seleniumの前処理

    def make_next_url(self, number=None, timestamp=None):
        # url = "https://www3.nhk.or.jp/news/json16/new_001.json?_=1584420975519"
        # 目的のjsonのURLを返す関数
        if number is None:
            number = self.json_number
        if timestamp is None:
            timestamp = self.time_stamp

        query = urllib.parse.urlencode({"_": str(timestamp)})
        # urlunparseに渡すデータ作成(リストもしくはタプルで　辞書は壊れる)
        # パラメータまとめると見にくいので分割
        SCHEME: str = 'https'
        NETLOC: str = 'www3.nhk.or.jp'
        PATH: str = '/news/json16/new_' + str(str(number).zfill(3)) + ".json"
        FRAGMENT = None
        PARAMS = None
        # urlunparseに渡す順番を変えると壊れるので順番は変えないこと
        url_data: list = [SCHEME, NETLOC, PATH, FRAGMENT, query, PARAMS]
        return urllib.parse.urlunparse(url_data)

    def parse(self, response):
        # jsonを日本語に
        json_response = json.loads(response.body_as_unicode())
        # データ格納
        for data in json_response["channel"]["item"]:
            yield {
                "url": "https://www3.nhk.or.jp/news/" + data["link"],
                "title": data["title"],
                "word": "".join([i["title"] for i in data["word"]])
            }

        # 次のjsonがあるか確認してあったら読み込み
        if json_response["channel"]["hasNext"]:
            self.json_number = self.json_number + 1
            yield scrapy.Request(
                self.make_next_url(number=self.json_number, timestamp=self.time_stamp),
                callback=self.parse
            )

        pass

from bbc.settings import MIN_ARTICLE_LENGTH
from scrapy.exceptions import DropItem
import re

class BbcPipeline(object):
    def process_item(self, item, spider):
        return item

class DropShortArticlesPipeline(object):
    def process_item(self, item, spider):
        if len(item["content"]) < MIN_ARTICLE_LENGTH:
            raise DropItem("Article text is too short.")

        return item
from scrapy.item import Item, Field


class BbcItem(Item):
    URL = Field()
    content = Field()
    heading = Field()
    image = Field()
    link_external = Field()
    link_internal = Field()
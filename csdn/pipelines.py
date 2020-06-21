from scrapy.exporters import JsonLinesItemExporter

class CsdnPipeline(object):
    def process_item(self, item, spider):
        self.fp = open("cainiao.json", "wb")
        self.ft = open("cainiao.txt", "a", encoding="utf-8")
        self.ft.write(str(item["name"]) + '\n')
        self.ft.write(str(item["content"]) + '\n\t')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        self.ft.close()
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.conf import settings
import os
import os.path

class ScrapyDot(object):
    def __init__(self):
        dispatcher.connect(self.request_received, signal=signals.request_received)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        if not os.path.exists(settings['DOT_OUTPUT_DIRECTORY']):
            os.makedirs(settings['DOT_OUTPUT_DIRECTORY'])
        self.output = {}

    def spider_opened(self, spider):
        self.output[spider.name] = open("%s/%s.dot" % (settings['DOT_OUTPUT_DIRECTORY'], spider.name), 'w+')
        self.output[spider.name].write("digraph %s {\n" % (spider.name))


    def request_received(self, request, spider):
        if request.headers.has_key('Referer'):
            out = "\"%s\" -> \"%s\";\n" % (request.headers['Referer'], request.url)
            self.output[spider.name].write(out)

    def spider_closed(self,spider):
        self.output[spider.name].write("}\n")
        self.output[spider.name].close()


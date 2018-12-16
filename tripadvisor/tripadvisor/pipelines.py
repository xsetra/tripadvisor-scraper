# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TripadvisorPipeline(object):
    def open_spider(self, spider):
        self.file = open(getattr(spider, 'output_file', 'output.txt'), 'a')

    def close_spider(self, spider):
        self.file.close()

    def clean_html(self, item):
        item['entry'] = item['entry'].strip('\r\n')
        line_sentences = item['entry'].split('.')
        for sentence in line_sentences:
            sentence = sentence.strip('. ')
            sentence = sentence.replace('\n', ' ')
            sentence = sentence.lstrip().rstrip()
            if sentence != '':
                yield sentence

    def process_item(self, item, spider):
        for cleaned in self.clean_html(item):
            self.file.write(cleaned + ".\n")
        return item

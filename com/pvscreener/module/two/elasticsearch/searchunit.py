# coding=utf-8
from elasticsearch import Elasticsearch
import com.pvscreener.module.general.CommonSearch as CommonSearch
import os
import sys

# Класс для поиска и фильтрации данных:
class SearchUnit(CommonSearch):

    def __init__(self, initial_directory = None):
        """initialize"""
        __elasticSearch = Elasticsearch()
        indexName = "nya" #the index name
        docType = "drug_safety"
        __elasticSearch.indices.create(index=indexName)

        drugMapping = {
            'properties': {
#                'name': {'type': 'string'},
                'title': {'type': 'string'},
                'fulltext': {'type': 'string'}
            }
        }

        __elasticSearch.indices.put_mapping(index=indexName, doc_type=docType, body=drugMapping)

        # 1. Import filenames and their contents
        # 2. For each title and content make an index

        initial_directory = ""

        for root, subdirs, files in os.walk(initial_directory):
            for filename in files:
                file_path = os.path.join(root, filename)

                with open(file_path, 'rb') as f:
                    f_content = f.read()
                    try:
                        __elasticSearch.index(index=indexName, doc_type=docType, body={
                            'title': filename,
                            'fulltext': f_content
                        })
                    except Exception,e:
                        print str(e)
#!/bin/bash
scrapy crawl first -o output.json

cd Images/

python images_download.py 

rm output.json



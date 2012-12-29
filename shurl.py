#!/usr/bin/env python2.7

import web
import urlparse
import hashlib

URLS = (
  '/new', 'NewUrl',
  '/([0-9a-f]{5})', 'Resolve',
)

"""
Example DB Scheme

CREATE TABLE IF NOT EXISTS `url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` text NOT NULL,
  `short` varchar(5) NOT NULL,
  `added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ;
"""

DB = web.database(dbn='mysql', db='', user='', pw='')
BASE_URL = "http://localhost:8080/"

class NewUrl:

  def get_or_create_short_url(self, url):
    res = DB.where('url', url=url)
    
    if len(res) > 0:
      return BASE_URL + res[0]['short']

    short = hashlib.md5(url).hexdigest()[:5]

    # check if hash already exists
    res = DB.where('url', short=short)
    while len(res) > 0:
      short = hashlib.md5(url + random.randint(1,100000)).hexdigest()[:5]
      res = DB.where('url', short=short)

    DB.insert('url', url=url, short=short)
    return BASE_URL + short

  def POST(self):
    data = web.input()
    url_parsed = urlparse.urlparse(data.url)
    if url_parsed.scheme not in ['http', 'https']:
      return "error"

    return self.get_or_create_short_url(data.url)

class Resolve:

  def GET(self, short):
    res = DB.where('url', short=short)

    if len(res) > 0:
      raise web.redirect(res[0]['url'])
    else:
      return "Unknown url."

if __name__ == "__main__":
  app = web.application(URLS, globals())
  app.run()

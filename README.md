Shurl
=====
Shurl is a minimal URL shortener service using Python and web.py. URLs are stored in a database. There is no user interface for entering URLs, URLs are shortened through a POST request to http://youraddress/new. Writing a simple HTML form for this should be trivial. There is no automatic purging of URLs, you have to do this yourself.

Requirements
------------
* Python (>= 2.7, may work on older versions)
* web.py (>= 0.37, may work on older versions)
* MySQLdb/psycopg2/whatever (depends on the db backend you choose)


Installation
------------
Shurl should run fine using CGI modules for your http server of choice. See http://webpy.org/install for more details.

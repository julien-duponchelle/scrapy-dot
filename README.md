Description
===========
A Scrapy extensions which export a graph of link between crawled items by scrapy
in dot file format.

Dot file can be convert to graph with graphviz or tools like gephi.

Sample output with gephi:

<img src="http://github.com/noplay/scrapy-dot/blob/master/images/sample.png?raw=true"/>


Install
=======
   pip install "ScrapyDot"

Configure your settings.py:
----------------------------
    EXTENSIONS = {
        "scrapydot.ScrapyDot": 1000
    }

    DOT_OUTPUT_DIRECTORY = "dot"


Changelog
=========
0.1

* Initial version

Licence
=======
Copyright 2011 Julien Duponchelle

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

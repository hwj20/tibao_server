from whoosh.fields import Schema, TEXT
from whoosh.query import *
import os.path
from whoosh.index import create_in


# https://www.osgeo.cn/whoosh/quickstart.html   whoosh -- 搜索引擎

schema = Schema(title=TEXT, content=TEXT)

# 创建索引文件
if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

# # 写入
# writer = ix.writer()
# writer.add_document(title=u"My document", content=u"This is my document!")
# writer.add_document(title=u"Second try", content=u"This is the second example.")
# writer.add_document(title=u"Third time's the charm", content=u"Examples are many.")
# writer.commit()


with ix.searcher() as searcher:
    myQuery = And([Term("content", u"apple"), Term("content", "bear")])
    results = searcher.search(myQuery)

    print(results)

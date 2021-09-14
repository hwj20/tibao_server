import jieba

seg_list = jieba.cut_for_search("我爱自然语言处理")

print("search mode:" + " ".join(seg_list))

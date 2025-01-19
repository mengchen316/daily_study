from xmindparser import xmind_to_dict
import xmindparser

# xmindparser配置
xmindparser.config = {
    'showTopicId': True,  # 是否展示主题ID
    'hideEmptyValue': True  # 是否隐藏空值
}


# [*补丁号,[*提单号,[路径[用例名称[步骤，预期结果]
#
# 递归方法
def topic1(topics, t=None):
    if t is None:
        t = []
    for topic in topics:
        if 'topics' not in topic:
            return t.append(topic["title"])
        topics2 = topic["topics"]
        t += topic["title"]
        return t[-1] + topic1(topics, t)


t = []
# 任务名：
#  补丁号 ：symbol-pin
#  提单号 ：symbol-lightning
#  模块 ：c_symbol_telephone
# 用例： priority-1
file1 = r'test.xmind'

json_data = xmind_to_dict(file1)
print(json_data[0]['topic'])
topic = json_data[0]['topic']
test_cases = []
for i in topic['topics']:
    # 版本号
    rwm = i['title']
    print(i)
    print(rwm)
    for j in i["topics"]:
        bdh = j['title']  # 补丁号
        print(j)
        print(bdh)
        for k in j["topics"]:
            tdh = k['title']  # 提单号
            print(k)
            print(tdh)
            for t in k["topics"]:
                model = t['title']  # 模块
                print(t)
                print(model)
                for h in t["topics"]:
                    case_title = h['title']  # 用例
                    print(case_title)
                    print(h)
                    if 'priority-1' in h['makers']:
                        lv = 'p0'
                    elif 'priority-2' in h['makers']:
                        lv = 'p1'
                    elif 'priority-' in h['makers']:
                        lv = 'p2'
                    else:
                        lv = 'p3'
                    for u in h["topics"]:
                        qztj = u['title']  # 前置条件
                        print(qztj)
                        print(u)
                        for v in u['topics']:
                            czbz = v['title']  # 操作步骤
                            print(czbz)
                            print(v)
                            for w in v['topics']:
                                yqjg = w['title']  # 预期结果
                                print(yqjg)

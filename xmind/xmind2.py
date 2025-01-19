import xmindparser
import pandas as pd


def xmind_to_excel(xmind_file, excel_file):
    # 解析 XMind 文件
    try:
        xmind_data = xmindparser.xmind_to_dict(xmind_file)
    except Exception as e:
        print(f"无法解析 XMind 文件：{e}")
        return

    # 提取第一个主题 (sheet)
    if not xmind_data:
        print("没有找到任何数据，请检查 XMind 文件是否正确")
        return

    sheet = xmind_data[0]
    root_topic = sheet.get("topic", {})

    {
        "版本": "2月版本",
        "补丁": "补丁",
        "提单": "分支xx",
        "用例": "用例1",
        "前置条件": "前置条件",
        "操作步骤": "操作步骤",
        "预期结果": "预期结果",
    }
    # 遍历主题，递归提取数据
    # def parse_topic(topic, parent=""):
    #     title = topic.get("title", "无标题")
    #     makers = topic.get("makers", [])
    #     if 'star-red' in makers:
    #         rows.append({"版本": parent, "当前主题": title})
    #
    #     children = topic.get("topics", [])
    #     rows.append({"父主题": parent, "当前主题": title})
    #     for child in children:
    #         parse_topic(child, parent=title)

    # 将嵌套结构数据转换为表格形式
    def parse_topic(topic, parent_titles=[]):
        """递归解析主题"""
        rows = []
        current_title = topic.get('title', '')
        makers = topic.get("makers", [])
        if len(parent_titles)<6 and not makers:
            raise Exception('"{}"没有makers'.format(current_title))

        if 'priority-1' in makers:
            lv = 'p0'
            parent_titles.append(lv)
        elif 'priority-2' in makers:
            lv = 'p1'
            parent_titles.append(lv)
        elif 'priority-3' in makers:
            lv = 'p2'
            parent_titles.append(lv)

        children = topic.get('topics', [])

        if not children:  # 没有子主题，生成一行数据
            rows.append(parent_titles + [current_title])
        else:
            for child in children:
                rows.extend(parse_topic(child, parent_titles + [current_title]))
        return rows

    # 从根主题开始解析
    rows = parse_topic(root_topic)
    header = ["迭代用例", "版本", "补丁号", "提单号", "模块",'用例等级', "用例名称", "前置条件", "操作步骤", "预期结果"]

    # 将数据转换为 Excel 表格
    try:
        df = pd.DataFrame(rows, columns=header)
        df.to_excel(excel_file, index=False, engine='openpyxl')
        print(f"成功将 XMind 文件转换为 Excel: {excel_file}")
    except Exception as e:
        print(f"保存 Excel 文件失败：{e}")


    # 打开现有的 Excel 文件
    input_file = "output.xlsx"  # 替换为你的 Excel 文件路径
    output_file = "测试用例_更新.xlsx"

    # 读取 Excel 数据
    df = pd.read_excel(input_file,engine="openpyxl")

    # 插入新列，假设插入在第二列（索引为1）
    new_column_name1 = "新列名称1"
    new_column_name2 = "新列名称2"
    new_column_name3 = "新列名称3"
    new_column_values = ["默认值"] * len(df)  # 默认值填充每行

    # 在指定位置插入新列
    df.insert(1, new_column_name1, new_column_values)
    df.insert(1, new_column_name2, new_column_values)
    df.insert(1, new_column_name3, new_column_values)

    # 保存更新后的 Excel 文件
    df.to_excel(output_file, index=False, engine="openpyxl")
    print(f"插入新列后的 Excel 文件已保存为: {output_file}")


# 调用函数
xmind_file = "test.xmind"  # 替换为你的 XMind 文件路径
excel_file = "output.xlsx"  # 输出的 Excel 文件路径
xmind_to_excel(xmind_file, excel_file)

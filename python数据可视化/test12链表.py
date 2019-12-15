import pandas as pd

# 创建透视表
def create_pivottalbe(data):

    ########## Begin ##########
    data1 = data.pivot_table(index=["day"], columns=["time"], values=["tip"],
                             aggfunc=sum, margins=True)
    return data1

# 创建交叉表
def create_crosstab(data):
    ########## Begin ##########
    data2 = pd.crosstab(index=data["day"], columns=data["time"], values=data["tip"],
                        aggfunc=sum, margins=True)

    return data2
    ########## End ##########
    # piv_result = data1
    # cro_result = data2
def main():
    # 读取csv文件数据并赋值给data
    ########## Begin ##########
    data = pd.read_csv('shuju.csv')
    # print(data.head())

    d = data.pivot_table(index=["day"],columns=["time"],values=["tip"], aggfunc=sum, margins=True)
    # print(d.head())

    piv_result = create_pivottalbe(data)
    cro_result = create_crosstab(data)
    print("透视表：\n{}".format(piv_result))
    print("交叉表：\n{}".format(cro_result))

main()
# data = {'A': [1, 2, 2, 3, 2, 4],
#         'B': [2014, 2015, 2014, 2014, 2015, 2017],
#         'C': ["a", "b", "c", "d", "e", "f"],
#         'D': [0.5, 0.9, 2.1, 1.5, 0.5, 0.1]
#         }
# df = pd.DataFrame(data)
# print(df.sort_values(by="B"))
# d = df.pivot_table(index=["B"])
# print(d)
#
# d = df.pivot_table(columns=["C"])
# print(d)
#
# d = df.pivot_table(index=["B"],columns=["C"])
# print(d)
#
# d = df.pivot_table(index=["B"],columns=["C"],values=["A"], aggfunc=sum, margins=True)
# print(d)
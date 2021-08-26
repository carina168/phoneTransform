"""
 author:oucuirong
 date:2021/08/25
"""
# 电话号码字典
phone_dict = {
    '0': ' ',
    '1': ' ',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}


def phone_num_transform_english(digits, phone_dict):
    # 存储结果list
    result_list = []
    deep(digits, "", result_list)
    return result_list


def deep(digits, tmp, result_list):
    if not digits:
        result_list.append(tmp)
        return
    for c in phone_dict[digits[0]]:
        deep(digits[1:], tmp+c, result_list)


if __name__ == '__main__':
    # 输入list
    input_list = []
    # input
    input_num = str(input("请输入号码："))
    input_list.append(input_num)
    for num in input_list:
        List = phone_num_transform_english(num, phone_dict)
        print(List)



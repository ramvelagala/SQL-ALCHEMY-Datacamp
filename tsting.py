import re


def format_generation():
    data1 = [1, -2, 3.0, -4.0, -5.1, 6.2, 7.369, -8.356, 4565242, -123.7778888]
    data = [1, 23, 456, -7891]
    res_list = []
    data1 = [str(num) for num in data1]
    for num in data1:
        a = num.split('.')
        x = ''
        y = ''
        dd = re.sub(r'[^\w]', '', a[0])
        x = re.sub(r"\d+", len(dd) * '9', dd)
        # print(x)
        if len(a) == 2:
            y = re.sub(r"\d+", len(a[1]) * '9', dd)
            y = '.' + y
        else:
            pass
        if a[0].startswith('-'):
            x = '-' + x
        res = x + y
        res_list.append(res)
    return data1, res_list


print(format_generation())

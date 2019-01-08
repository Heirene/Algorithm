import copy
def rotate(nums, k):
    """
    189: Rotate array
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    这个算法超时
    https://blog.csdn.net/v_JULY_v/article/details/6322882   https://www.xuebuyuan.com/1046723.html
    """
    length = len(nums)
    k %= length
    for i in range(1, k+1):
        temp = nums[length - 1]
        for j in range(1, length)[::-1]:
            nums[j] = nums[j-1]
            print(j, ':', nums)
        nums[0] = temp
    return nums

def max_array_number(nums):
    """
    :param nums: number list eg:[123, 45, 76]
    :return: string of number eg:'7654321'
    """
    for i in range(len(nums)):
        nums[i] = sort_number(nums[i])
    return ''.join(sort_by_first_digital(nums))


def sort_number(number):
    """
    :param number: unsorted number
    :return: string of sorted number
    """
    number_array =list(str(number))
    #print(number_array)
    return ''.join(sort(number_array))


def sort(number_array):
    """
    :param number_array: digital list
    :return: digital list sorted desc
    """
    for i in range(len(number_array)):
        index = i
        for j in range(i + 1, len(number_array)):
            if int(number_array[j]) > int(number_array[index]):
                index = j
        number_array[i], number_array[index] = number_array[index], number_array[i]
        print('after sort each number:',number_array)
    return number_array


def sort_by_first_digital(nums):
    """
    sort by first digital in each number
    :param nums: string list
    :return: string list nums
    """
    for i in range(len(nums)):
        index = i
        for j in range(i + 1, len(nums)):
            if int(nums[j][0]) > int(nums[index][0]):
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums


# 以下 test 开头的函数是单元测试
def test_rotate():
    """
    parsed_url 函数很容易出错, 所以我们写测试函数来运行看检测是否正确运行
    """
    '''http = 'http'
    https = 'https'
    host = 'g.cn'
    path = '/'
    test_items = [
        ('http://g.cn', (https, host, 80, path)),
        ('http://g.cn/', (http, host, 80, path)),
        ('http://g.cn:90', (http, host, 90, path)),
        ('http://g.cn:90/', (http, host, 90, path)),
        #
        ('https://g.cn', (https, host, 443, path)),
        ('https://g.cn:233/', (https, host, 233, path)),
    ]
    for t in test_items:
        url, expected = t
        u = parsed_url(url)
        # assert 是一个语句, 名字叫 断言
        # 如果断言成功, 条件成立, 则通过测试
        # 否则为测试失败, 中断程序报错
        e = "parsed_url ERROR, ({}) ({}) ({})".format(url, u, expected)
    '''
    test_case = [([-1, -100, 3, 99], 1, [99,-1,-100,3]), ([-1, -100, 3, 99], 2, [3,99,-1,-100])]
    for item in test_case:
        nums, k, correct_case = item
        before_rotate = copy.deepcopy(nums)
        print(before_rotate)
        rotate_array = rotate(nums, k)
        error = "rotate faily: {}, {}, expected:{}, rotate:{}".format(before_rotate, k,correct_case, rotate_array)
        assert correct_case == rotate_array, error
        print("test successfully")

def test_max_array_number():
    test_case = [([13, 45, 67], '765431')]
    print(test_case)
    for item in test_case:
        input_list, expected_value = item
        input_value = copy.deepcopy(input_list)
        max_number = max_array_number(input_list)
        error = 'input:{} expected: {} output:{}'.format(input_value, expected_value, max_number)
        assert expected_value == max_number, error
        print("test successfully")


if __name__ == '__main__':
    #test_rotate()
    #print('test')
    test_max_array_number()



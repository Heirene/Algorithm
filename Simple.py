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

#选择排序
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





def reverse_bin(integer):
    """
    :param integer: input an integer
    :return: reversion of 32-bit binnary string converted from integer.
    leetcode 190:颠倒二进制位 eg interger = 5 , it's bin is: 00000000 00000000 00000000 00000101  then return：10100000 00000000 00000000 00000000
    """
    bin_str = bin(integer).replace('0b', '').zfill(32)
    reverse_bin_str = ''.join(reverse(list(bin_str)))
    return  reverse_bin_str


def reverse(list_str):
    start = 0
    end = len(list_str) - 1
    print(list_str)
    while start < end:
        temp = list_str[start]
        list_str[start] = list_str[end]
        list_str[end] = temp
        start += 1
        end -= 1
    print(list_str)
    return  list_str


def reverseBits(n):
    bin_str = bin(n).replace('0b', '').zfill(32)
    bin_str = list(bin_str)
    start = 0
    end = len(bin_str) - 1
    print(bin_str)
    while start < end:
        temp = bin_str[start]
        bin_str[start] = bin_str[end]
        bin_str[end] = temp
        start += 1
        end -= 1
    reverse_bin_str = ''.join(bin_str)
    return reverse_bin_str


def decorator_test(fun):
    def wrapper():
        print('start function')
        fun()
        print('test successfully')
    return wrapper

def fib(n):
    """

    :param n:
    :return: 返回索引为n 的斐波那契数列
    """
    #print('before', n)
    if n == 0 or n == 1:
        #print(n)
        return 1
    else:
        #print('after else', n)
        return fib(n-1) + fib(n-2)

def fibAll(n):
    """

    :param n:
    :return: 生成器生成索引为1至n的斐波那契数列
    """
    while n >= 0:
        #print(fib(n) , ' ')
        yield  fib(n)
        n = n-1

def fibSelectBy(max):
    """

    :param max:
    :return: 斐波那契数列中和max 相差最小的数
    """
    n = 0
    fib(n)
    while fib(n) < max:
        n = n + 1
        fib(n)
    if max - fib(n) > fib(n+1) - max:
        return fib(n+1)
    else:
        return fib(n)


# 以下 test 开头的函数是单元测试
@decorator_test
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
        #print("test successfully")
@decorator_test
def test_max_array_number():
    test_case = [([13, 45, 67], '765431')]
    print(test_case)
    for item in test_case:
        input_list, expected_value = item
        input_value = copy.deepcopy(input_list)
        max_number = max_array_number(input_list)
        error = 'input:{} expected: {} output:{}'.format(input_value, expected_value, max_number)
        assert expected_value == max_number, error
        #print("test successfully")

@decorator_test
def test_reverse_bin():
    test_case = [(5, '10100000000000000000000000000000')]
    for items in test_case:
        input_integer, expected = items
        reverse_bin_str = reverse_bin(input_integer)
        # reverse_bin_str = reverseBits(input_integer)
        error = 'input integer: {}, expected value: {}, actual value: {}'.format(input_integer, expected, reverse_bin_str)
        assert expected == reverse_bin_str, error

if __name__ == '__main__':
    # test_rotate()
    # print('test')
    # test_max_array_number()
    #test_reverse_bin()
    for x in fibAll(6):
        #print(x)
        #print('done')
        print(x)

    gen = fibAll(7)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    #print(fib(6))


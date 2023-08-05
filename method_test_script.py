"""
@Project ：new_fms_test
@File    ：method_test_script.py
@IDE     ：PyCharm
@Author  ：FMS
@Date    ：2023/8/4 11:55
@Des     ：
"""
def test_method(data):
    print("1:------"+data)
    bin_str = bytes.fromhex(data)
    print(bin_str)
    for i in bin_str:
        print(i)



if __name__ == '__main__':
    pass

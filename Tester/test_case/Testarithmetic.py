from Tester.example.arithmetic import judge_num

# 成功的测试用例
def test_true():
    assert judge_num(150)

#失败的测试用例
def test_false():
    assert judge_num(30)
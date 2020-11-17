# import os
# import sys
#
# BASE_PATH = os.path.dirname(
#    os.path.dirname(os.path.abspath(__file__))
# )
# sys.path.insert(0, BASE_PATH)
#
# from report.common import OpCase
# from test_demo import setting
#
#
# class CaseRun(object):
#    def find_cases(self):
#       op = OpCase()
#       for f in os.listdir(setting.CASE_PATH):#每次循环的时候读一个excel
#          abs_path = os.path.join(setting.CASE_PATH, f)
#          case_list = op.get_case(abs_path)
#          res_list = []
#          pass_count, fail_count = 0, 0
#          for case in case_list:#循环每个excel里面所有用例
#             url, method, req_data, cookie, header, check = case
#             res = op.my_request(url, method, req_data, cookie, header)  # 调用完接口返回的结果
#             status = op.check_res(res, check)
#             res_list.append([res, status])
#             if status == '成功':
#                pass_count += 1
#             else:
#                fail_count += 1
#          op.write_excel(res_list)  #写入excel
#          msg = '''
#          xx你好：
#             本次共运行%s条用例，通过%s条，失败%s条。
#          '''%(len(res_list), pass_count, fail_count)
#          # sendmail('测试用例运行结果',content=msg,attrs=abs_path)
# CaseRun().find_cases()
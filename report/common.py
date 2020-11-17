# import copy
# import xlrd
# from report.log import atp_log
# import requests
#
#
# class OpCase(object):
#    def get_case(self, file_path):
#       cases = [] #存放所有的case
#       if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
#          try:
#             book = xlrd.open_workbook(file_path)
#             sheet = book.sheet_by_index(0)
#             for i in range(1,sheet.nrows):
#                row_data = sheet.row_values(i)
#                cases.append(row_data[4:11])
#             atp_log.info('共读取%s条用例' % (len(cases)))
#             self.file_path = file_path
#          except Exception as e:
#             atp_log.error('【%s】用例获取失败，错误信息：%s' % (file_path, e))
#       else:
#          atp_log.error('用例文件不合法的，%s' % file_path)
#       return cases
#
#    def my_request(self, url, method, data=None, cookie=None, header=None, is_json=False):
#       method = method.upper()
#       data = self.dataToDict(data)
#       cookie = self.dataToDict(cookie)
#       header = self.dataToDict(header)
#       data = data if data else {}
#       cookie = cookie if cookie else {}
#       header = header if header else {}
#       try :
#          if method == 'POST':
#             try:
#                if is_json:
#                   res = requests.post(url, json=data, cookies=cookie, headers=header, verify=False).text
#                else:
#                   res = requests.post(url, data=data, cookies=cookie, headers=header, verify=False).text
#                atp_log.debug('【接口返回数据：%s】' % res)
#                print('res...', res)
#             except Exception as e:
#                res = str(e)  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
#                atp_log.error('异常信息：接口调用失败！ url 【%s】 data 【%s】 实际结果是 【%s】' % (url, data, res))
#          elif method == 'GET':
#             try:
#                # verify=False 的意思就是https能访问
#                res = requests.get(url, params=data, cookies=cookie, headers=header, verify=False).text
#                atp_log.debug('【接口返回数据：%s】' % res)
#             except Exception as e:
#                res = str(e)  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
#                atp_log.error('异常信息：接口调用失败！ url 【%s】 data 【%s】实际结果是 【%s】' % (url, data, res))
#             return res
#          else:
#             atp_log.warning('该请求方式暂不支持。。')
#             res = '该请求方式暂不支持。。'
#       except Exception as e:
#          msg = '【%s】接口调用失败，%s'% (url, e)
#          atp_log.error(msg)
#          res = msg
#       return res
#
#    def check_res(self, res, check):
#       res = res.replace('": "', '=').replace('": ', '=')
#       for c in check.split(','):
#          if c not in res:
#             atp_log.info('结果校验失败，预期结果：【%s】，实际结果【%s】' % (c, res))
#             return '失败'
#       return '成功'
#
#    def write_excel(self, cases_res):
#       # [ ['dsfd',"通过"] ,['sdfsdf','失败'] ]
#       book = xlrd.open_workbook(self.file_path)
#       new_book = copy.copy(book)
#       sheet = new_book.get_sheet(0)
#       row = 1
#       for case_case in cases_res:
#          sheet.write(row, 11, case_case[0]) #写第11列
#          sheet.write(row, 12, case_case[1]) #写第12列
#          row += 1
#       new_book.save(self.file_path.replace('xlsx', 'xls'))
#
#    def dataToDict(self, data=None):
#       if data:
#          #把数据转成字典
#          res = {}
#          data = data.split(',')
#          for d in data:
#             #a=
#             k, v = d.split('=')
#             res[k] = v
#          return res
#
#

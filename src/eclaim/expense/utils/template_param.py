# -*- coding: utf-8 -*-

def common_parameter(page_title='eclaim', head_title='', **kwargs):

    page_title = page_title
    if head_title:
        page_title = page_title + '-' + head_title

    head_title = head_title

    param = locals()
    param.update(kwargs)
    del param['kwargs']
    return param


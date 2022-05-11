# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:15:05 2022

@author: 1
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_eqdatas(txtSDate):
    form_data={
        'draw': '1',
        'columns[0][data]': '0',
        'columns[0][name]': 'EventNo',
        'columns[0][searchable]': 'false',
        'columns[0][orderable]': 'true',
        'columns[0][search][value]': '',
        'columns[0][search][regex]': 'false',
        'columns[1][data]': '1',
        'columns[1][name]': 'MaxIntensity',
        'columns[1][searchable]': 'true',
        'columns[1][orderable]': 'true',
        'columns[1][search][value]': '',
        'columns[1][search][regex]': 'false',
        'columns[2][data]': '2',
        'columns[2][name]': 'OriginTime',
        'columns[2][searchable]': 'true',
        'columns[2][orderable]': 'true',
        'columns[2][search][value]': '',
        'columns[2][search][regex]': 'false',
        'columns[3][data]': '3',
        'columns[3][name]': 'MagnitudeValue',
        'columns[3][searchable]': 'true',
        'columns[3][orderable]': 'true',
        'columns[3][search][value]': '',
        'columns[3][search][regex]': 'false',
        'columns[4][data]': '4',
        'columns[4][name]': 'Depth',
        'columns[4][searchable]': 'true',
        'columns[4][orderable]': 'true',
        'columns[4][search][value]': '',
        'columns[4][search][regex]': 'false',
        'columns[5][data]': '5',
        'columns[5][name]': 'Description',
        'columns[5][searchable]': 'true',
        'columns[5][orderable]': 'true',
        'columns[5][search][value]': '',
        'columns[5][search][regex]': 'false',
        'columns[6][data]': '6',
        'columns[6][name]': 'Description',
        'columns[6][searchable]': 'true',
        'columns[6][orderable]': 'true',
        'columns[6][search][value]':'', 
        'columns[6][search][regex]': 'false',
        'order[0][column]': '2',
        'order[0][dir]': 'desc',
        'start': '0',
        'length': '99999',
        'search[value]': '',
        'search[regex]': 'false',
        'Search': '',
        'txtSDate': txtSDate,
        'txtEDate': '',
        'txtSscale': '',
        'txtEscale': '',
        'txtSdepth': '',
        'txtEdepth': '',
        'txtLonS': '',
        'txtLonE': '',
        'txtLatS': '',
        'txtLatE': '',
        'ddlCity': '',
        'ddlTown': '',
        'ddlCitySta': '',
        'ddlStation': '',
        'txtIntensityB': '',
        'txtIntensityE': '',
        'txtLon': '',
        'txtLat': '',
        'txtKM': '',
        'ddlStationName': '------',
        'cblEventNo':'' ,
        'txtSDatePWS': '',
        'txtEDatePWS': '',
        'txtSscalePWS': '',
        'txtEscalePWS': '',
        'ddlMark':''
    }
    #爬找
    resp=requests.post('https://scweb.cwb.gov.tw/zh-tw/earthquake/ajaxhandler',data=form_data)
    datas=json.loads(resp.text)
    
    #建df
    eqdatas=[]
    for data in datas['data']:
        eqdatas.append([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[5][:2]])
    df=pd.DataFrame(eqdatas,columns=(['id','編號','臺灣時間','規模','深度','相對位置','最大震度','經度','緯度','區域']))
    
    #整理df
    df.drop_duplicates()
    indexes=(df.index[df['最大震度']==''].to_list())
    df=df.drop(index=indexes)
    for x in ('規模','深度','最大震度','經度','緯度'):
        df[x]=df[x].astype(float,errors='ignore')
    df['臺灣時間']=pd.to_datetime(df['臺灣時間'])
    
    return df
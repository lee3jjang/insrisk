import os
import re
import pandas as pd
from ..tools import *

def load_fssrpt(filepath, code):
    """금감원 업무보고서 파일별 추출 및 가공
               
    :param filepath: 업무보고서 파일 경로
    :type filepath: str
    :param code: 업무보고서 코드(AI004, AI009, ...)
    :type code: str
    :return: 정제된 업무보고서
    :rtype: DataFrame
    
    .. ipython:: python

        from insrisk.data import fssrpt
        ai059 = fssrpt.load_fssrpt('data/업무보고서_201701.xlsx', 'AI059')
    
    """
    code_upper = code.upper()
    locations = {
        'AI004': (11, 2),
        'AI009': (11, 2),
        'AI057': (11, 2),
        'AI059': (13, 3),
        'AI060': (13, 2),
        'AI062': (11, 2),
        'AI135': (12, 2),
        'AI163': (12, 3),
    }
    if code_upper not in locations.keys():
        raise Exception('코드 입력 에러')
    else:
        x, y = locations.get(code_upper)
    df = pd.read_excel(filepath, sheet_name=code_upper)
    index = df.iloc[x:, 0].str.replace('\r\n', '').values
    columns = df.iloc[9, y:].values
    rpt = pd.DataFrame(df.iloc[x:, y:].values, index=index, columns=columns).fillna(0).astype(float)
    return rpt

def load_fssrpt_all(folderpath, code):
    """금감원 업무보고서 폴더별 추출 및 가공

    Parameters
    ----------
    folderpath : str
        업무보고서 폴더 경로
    code : str
        업무보고서 코드 (AI059, AI004 등)
    
    Returns
    -------
    dict
        key: 기준년월, value: 보고서(DataFrame) 인 dictionary
    
    Examples
    --------
    >>> from insrisk.data import fssrpt
    >>> rpt = fssrpt.load_fssrpt_all('data', 'AI059')
    
    Warnings
    --------
    파일명 "업무보고서_yyyymm.xlsx" 형태로 되어 있어야 함

    """
    
    # 기준년월 생성 및 데이터 목록 유효성 검증
    m = re.compile('^업무보고서_\d{6}.xlsx$')
    data = [f for f in os.listdir(folderpath) if m.search(f)]
    yyyymm_list_data = list(map(lambda x: x[6:12], data))
    yyyymm_list_data.sort()
    start_yymm, end_yymm = yyyymm_list_data[0], yyyymm_list_data[-1]
    start_year, start_month = int(start_yymm[:4]), int(start_yymm[-2:])
    end_year, end_month = int(end_yymm[:4]), int(end_yymm[-2:])
    yyyymm_list = generate_yyyymm((start_year, start_month), (end_year, end_month))
    if yyyymm_list_data != yyyymm_list:
        raise('생성된 기준년월 리스트와 데이터 목록상 기준년월 불일치')

    # 데이터 로드
    rpt = {}
    for yyyymm in yyyymm_list:
        rpt[yyyymm] = load_fssrpt(os.path.join(folderpath, '업무보고서_{}.xlsx'.format(yyyymm)), code)
        
    return rpt

def fssrpt_value_inc_ts(rpt, row, column):
    """
        Description
        -----------
        dict 형태의 업무보고서 중 특정 변수의 월별 증감액을 출력
        ※ 기준월 1월로 시작해야 함
        
        Input
        -----
        rpt : load_rpt_all의 output
        row : 행 Key
        column : 열 Key
        
        Output
        ------
        series (key: 기준년월, value: 특정변수)
        
        Example
        -------
        # 손익계산서 불러오기
        rpt = load_rpt_all('data', 'AI009')

        # 데이터 불러오기
        earned_prem_ts = rpt_value_inc_ts(rpt, 'A', 'H') # 경과보험료(총괄)
        loss_ts = rpt_value_inc_ts(rpt, 'B', 'H') # 발생손해액(총괄)
        net_expense_ts = rpt_value_inc_ts(rpt, 'D', 'H') # 순사업비(총괄)
        ins_profit_ts = rpt_value_inc_ts(rpt, 'H', 'H') # 보험영업이익(총괄)
        inv_profit_ts = rpt_value_inc_ts(rpt, 'K', 'H') # 투자영업이익(총괄)
        net_income_ts = rpt_value_inc_ts(rpt, 'U', 'H') # 당기순이익(총괄)
        tot_income_ts = rpt_value_inc_ts(rpt, 'X', 'H') # 총포괄손익(총괄)
    """

    if list(rpt.keys())[0][-2:] != '01':
        raise Exception('기준월 1월로 시작해야 함')
          
    # 누적
    values = {}
    for yyyymm in rpt.keys():
        values[yyyymm] = rpt[yyyymm].loc[row, column]
    values_ts = pd.Series(values)
    values_ts.index = pd.to_datetime(values_ts.keys(), format='%Y%m')

    # 월별
    values_inc_ts = values_ts.copy()
    for i in range(len(values_ts)):
        values_inc_ts[i] = values_ts[i] if values_ts.index[i].month==1 else values_ts[i] - values_ts[i-1]

    return values_inc_ts

def fssrpt_value_ts(rpt, row, column):
    """
        Description
        -----------
        dict 형태의 업무보고서 중 특정 변수의 시점값을 출력
        
        Input
        -----
        rpt : load_rpt_all의 output
        row : 행 Key
        column : 열 Key
        
        Output
        ------
        series (key: 기준년월, value: 특정변수)
        
        Example
        -------
        # 손익계산서 불러오기
        rpt = load_rpt_all('data', 'AI004')

        # 데이터 불러오기
        op_asset_ts = rpt_value_ts(rpt, 'A1', 'H') # 운용자산(총괄)
    """
          
    values = {}
    for yyyymm in rpt.keys():
        values[yyyymm] = rpt[yyyymm].loc[row, column]
    values_ts = pd.Series(values)
    values_ts.index = pd.to_datetime(values_ts.keys(), format='%Y%m')

    return values_ts
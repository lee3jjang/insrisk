from insrisk.tools import *
from insrisk.data import fssrpt, tb

FOLDERPATH = 'C:/Users/11700205/Documents/Dev/12. 위기상황분석/2020.11 위기상황분석 기초데이터 생성 프로그램 개발/data'
# result = fssrpt.load_fssrpt_all(FOLDERPATH, 'AI004')
result = tb.load_tb_all(FOLDERPATH)
print(result)

# python setup.py bdist_wheel
# pip install --force-reinstall dist\
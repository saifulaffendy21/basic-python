#data_bad.py#
#Python 3.8.1
#pip install pandas
#pip install openpyxl
#pip install xlsxwriter
#pip install xlrd
#python -m pip install --upgrade pip

import pandas as pd
import xlsxwriter
import datetime
import os

# Request input PATH and directory name from USER 
# Example: D:\python\big data\2512
location = input('\nDirectory PATH of the excels? :')
# Example: 2511
date_name = input('\nDate of the data? :')

# Filter
files = os.listdir(location)
excel_file = []
for file in files:
    if file.endswith(".xlsx"):
        excel_file.append(file)        

#print(excel_file)

# Filter
filtered_excel_file = []
x = ''
i = 0
for file in excel_file:
    x = str(os.path.splitext(excel_file[i])[0])
    i+=1
    filtered_excel_file.append(x)
#skip
#print(filtered_excel_file)

# Create a new directory for the excel data
data_dir = ''
data_dir = (str(os.getcwd())+'/'+date_name)        
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)
    print("\nData directory %s was created." %data_dir)

#Change the new directory to new PATH
os.chdir(data_dir) 
print("\nDirectory changed !!!")

#loop kena ada
for data in filtered_excel_file:

    excel_file = location + '/' + data+'.xlsx'
    raw_df = pd.read_excel(excel_file, skiprows=12, index_col=0)

    filtered_df = raw_df[['Transaction No.','Action','Card Class','Card Type','Payment Method','Amount','Card No. ','Member ID','Transaction Date']].copy()
    #print(filtered_df.iloc[10])

    
    writer = pd.ExcelWriter(data+' '+date_name+'.xlsx', engine='xlsxwriter')
    filtered_df.to_excel(writer, index=False, sheet_name='Sheet2')

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['Sheet2']

    # Add some cell formats.
    number_fmt = workbook.add_format({'num_format': '0'})
    header_fmt = workbook.add_format({'bold': True})
    money_fmt  = workbook.add_format({'num_format': '#,##0.00'})

    #Edit excel file format
    worksheet.set_row(0, None, header_fmt)
    worksheet.set_column('A:A', None, number_fmt)
    worksheet.set_column('G:G', None, number_fmt)
    worksheet.set_column('F:F', None, money_fmt)

    #Exit writer and save excel
    print('\nDone printing for '+data)
    writer.save()

#End of program
print("\n***End of program!!!***")


"""
side note

>>> import pandas as pd
>>> pd.show_versions()

INSTALLED VERSIONS
------------------
commit           : None
python           : 3.8.1.final.0
python-bits      : 64
OS               : Windows
OS-release       : 10
machine          : AMD64
processor        : Intel64 Family 6 Model 61 Stepping 4, GenuineIntel
byteorder        : little
LC_ALL           : None
LANG             : None
LOCALE           : English_United States.1252

pandas           : 0.25.3
numpy            : 1.18.0
pytz             : 2019.3
dateutil         : 2.8.1
pip              : 19.3.1
setuptools       : 41.2.0
Cython           : None
pytest           : None
hypothesis       : None
sphinx           : None
blosc            : None
feather          : None
xlsxwriter       : 1.2.7
lxml.etree       : None
html5lib         : None
pymysql          : None
psycopg2         : None
jinja2           : None
IPython          : None
pandas_datareader: None
bs4              : None
bottleneck       : None
fastparquet      : None
gcsfs            : None
lxml.etree       : None
matplotlib       : None
numexpr          : None
odfpy            : None
openpyxl         : 3.0.2
pandas_gbq       : None
pyarrow          : None
pytables         : None
s3fs             : None
scipy            : None
sqlalchemy       : None
tables           : None
xarray           : None
xlrd             : 1.2.0
xlwt             : 1.3.0
xlsxwriter       : 1.2.7

"""
#Hello

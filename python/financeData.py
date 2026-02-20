import requests
import pandas as pd
from io import StringIO


def get_financeRatio_def(stock_code):
    url = f'https://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A{stock_code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701'
    resp = requests.get(url)
    df = pd.read_html(StringIO(resp.text))[0]
    
    def temp(x):
        return x.replace('계산에 참여한 계정 펼치기', '')
    
    df.index = df.iloc[ : , 0].apply(temp)
    df2 = df.T
    use_cols = ['영업이익률', 'EBITDA마진율', 'ROA', 'ROE', 'ROIC']
    df3 = df2[use_cols]
    df4 = df3.reset_index()
    df4.columns = ['DATE', '영업이익률', 'EBITDA마진율', 'ROA', 'ROE', 'ROIC']
    return df4.drop(0)


def get_investRatio_df(stock_mode):
    url = f'https://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A{stock_mode}&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701'
    resp = requests.get(url)
    df = pd.read_html(StringIO(resp.text))[1]
    def temp(x):
        return x.replace('계산에 참여한 계정 펼치기', '')
        
    df.index = df.iloc[ : , 0].apply(temp)
    df2 = df.T
    df3 = df2[['PER', 'PBR', 'PSR', 'PCR']]
    df4 = df3.reset_index()
    df4.columns = ['DATE', 'PER', 'PBR', 'PSR', 'PCR']
    return df4.drop(0)


def merge_df(stock_code, stock_name, market):
    f_df = get_financeRatio_def(stock_code)
    inv_df = get_investRatio_df(stock_code)
    total_df = pd.merge(f_df, inv_df, on='DATE', how='outer')
    total_df['종목코드'] = stock_code
    total_df['종목명'] = stock_name
    total_df['시장구분'] = market
    return total_df


def get_stockCode(path):
    code_df = pd.read_csv(path, encoding='cp949')
    code_df = code_df[['단축코드', '한글 종목약명', '시장구분']]
    return code_df


if __name__ == "__main__":
    path = r'C:\Users\KDA\Downloads\입력데이터_종목코드.csv'
    code_df = get_stockCode(path)

    stock_df_list = []
    for idx, row in code_df[:10].iterrows():
        try: 
            df = merge_df(row['단축코드'], row['한글 종목약명'], row['시장구분'])
            stock_df_list.append(df)
        except:
            print(row['한글 종목약명'], '<-에러남')

    final_df =  pd.concat(stock_df_list)
    final_df.to_csv(r'C:\Users\KDA\Downloads\새로운 종목 데이터.csv', index=False)
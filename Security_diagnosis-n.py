import logging

import streamlit as st

import ip_func

# ログの設定
logging.basicConfig(
    filename='application.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# loggingハンドラーが重複して存在していないか判定する
if not logger.hasHandlers():
    file_handler = logging.FileHandler('application.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)




# body
st.title('セキュリティ診断用')
st.title('AbuseIPDBリンク表示ツール')
st.write('  \n')
st.text('by bf oyama')

raw_data = st.text_area(
    'IPアドレスを含むログ等をそのまま貼り付けて、'
    'Ctrl + Enterを押してください',
    help='"netstat -ano"やHGW、4BRU、YAMAHAルーターのログをそのまま貼り付けてOKです。'
)

if raw_data:
    st.write('勉強不足でプライベートIPアドレスを取り除けていない点については\n'
             'ご容赦ください...')
    ip_list = ip_func.extract_ip_addresses(raw_data)

    if not ip_list:
        st.text('---------------------------------------------  \n'
                 'IPアドレスを確認できませんでした。  \n'
                 'IPアドレスを含むテキストなのにこの表示が出る場合は、  \n'
                 'ご連絡をお願いします。  \n'
                 '---------------------------------------------')

    url_list = ip_func.create_url(ip_list)
    for url in url_list:
        st.write(url)
    logger.info('Someone used this service.')

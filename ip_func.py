import re
import ipaddress

def extract_ip_addresses(input_text):
    """
    テキストエリアに入力されたテキストの中から
    正規表現でIPアドレスを抽出し、リスト化して返す
    """
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = set()
    rows = input_text.strip().split('\n')

    # ipアドレスを抽出してリスト化
    for row in rows:
        for cell in row.split(','):
            ips = re.findall(ip_pattern, cell)
            ip_addresses.update(ips)

    ip_address_list = list(ip_addresses)
    ip_address_list.sort()
    remove_address = ['127.0.0.1', '0.0.0.0']
    if remove_address in ip_address_list:
        for r in remove_address:
            ip_address_list.remove(r)
    return ip_address_list

def remove_private_ips(ip_list):
    return [ip for ip in ip_list if not ipaddress.ip_address(ip).is_private]

def create_url(ip_adrress_list):
    """
    IPアドレスのリストからURLのリストを生成して返す
    """
    url_list = []
    abuseipdb_url = 'https://www.abuseipdb.com/check/'
    for ip_addr in ip_adrress_list:
        url_list.append(abuseipdb_url + ip_addr)
    return url_list
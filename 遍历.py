import requests
from bs4 import BeautifulSoup

# 目标网站URL
url = 'http://x.x/x'  # 替换为你要遍历的网址

# 发送HTTP请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找包含 "Parent Directory" 和其他链接的a标签
    links = soup.find_all('a')

    print("Found the following directories/files:")
    for link in links:
        href = link.get('href')
        if href and ('Parent Directory' not in link.text):  # 排除 "Parent Directory" 链接
            print(href)
else:
    print(f"Failed to retrieve the URL. Status code: {response.status_code}")

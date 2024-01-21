import requests
response = requests.get("https://www.luochen.com")
# 默认情况下，requests 会尝试从 HTTP 响应头部的 Content-Type 字段中猜测正确的字符编码，
# 如果没有指定或者猜测不正确，那么可能会导致解码后的文字出现乱码。
# 通过设置 response.encoding = 'utf-8'，你可以覆盖 requests 的原始猜测，强制解码使用 'utf-8' 编码。
response.encoding = 'utf-8'
print(response.text)

# try:
#     print(response.text)
# except UnicodeEncodeError:
# encode('gbk', 'ignore')将原始的 Unicode 字符串（response.text）按照 GBK 编码规则转换成字节串。
# 这里的 'ignore' 参数会让编码操作忽略掉那些无法被GBK编码的字符，而不是抛出错误
# 不使用 'ignore'，当文本中包含不能用GBK编码表示的字符时，就会抛出 UnicodeEncodeError 错误
# 使用 'ignore' 后，那些无法编码的字符就会在编码过程中被忽略，不会出现在最终的字节串中

# .decode('gbk')：这一步将 GBK 编码的字节串重新解码成 Unicode 字符串。
# 因为在编码步骤中使用了 'ignore'，可能会导致某些字符被遗漏，所以解码回来的字符串可能少了这部分字符
# 这个方法常见于当系统环境不支持 Unicode 编码，或者为了避免编码错误而做的临时性处理。
# 使用 'ignore' 选项可能会导致数据丢失。更好的做法是确保所有环境都支持 UTF-8 编码
#     print(response.text.encode('gbk', 'ignore').decode('gbk'))
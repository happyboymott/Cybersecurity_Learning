# 1. 填入十六进制密文（有无空格均可）
hex_str = "62 19 46 46 45 75 69 58 4b 49 41 47 4f"

# 2. 填入单字节异或密钥
key = 0x2A

# 3. 将十六进制字符串转为字节数组
cipher_bytes = bytes.fromhex(hex_str)

# 4. 逐字节异或并转换为字符串
plain_bytes = bytes([b ^ key for b in cipher_bytes])
flag_content = plain_bytes.decode("utf-8", errors="ignore")

print(f"解密结果: {flag_content}")
print(f"完整 Flag: CMO{{{flag_content}}}")

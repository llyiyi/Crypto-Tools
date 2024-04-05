from SM3 import SM3
from SHA256 import SHA256
def HMAC(key, message, hashfunc):
    if isinstance(message, str):
        message = message.encode('UTF-8')
    if isinstance(key, str):
        key = key.encode('UTF-8')
    # 预处理密钥
    block_size = 64
    if len(key) > block_size:
        key = hashfunc(key)
    elif len(key) < block_size:
        key += b'\x00' * (block_size - len(key))

    # 创建内部和外部填充
    ipad = bytes([key_byte ^ 0x36 for key_byte in key])  
    opad = bytes([key_byte ^ 0x5C for key_byte in key])

    inner_hash = hashfunc(ipad + message)
    hmac = hashfunc(opad + bytes.fromhex(inner_hash))

    return hmac

# 测试
if __name__ == '__main__':
    sm3 = SM3()
    sha256 = SHA256()
    print("key=\"key\", message=\"abc\", HMAC-SM3: ",HMAC("key","abc",sm3.hash))
    print("key=\"key\", message=\"abc\", HMAC-SHA256: ",HMAC("key","abc",sha256.hash))
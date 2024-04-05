class SHA256:
    def __init__(self):
        # 哈希常量K
        self.K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    # 循环右移
    def right_rotate(self, x, n):
        return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

    # sha256算法
    def hash(self, message):
        if isinstance(message, str):
            message = message.encode('UTF-8')
        # 哈希初值H
        H = [
        0x6a09e667, 
        0xbb67ae85, 
        0x3c6ef372, 
        0xa54ff53a,
        0x510e527f, 
        0x9b05688c, 
        0x1f83d9ab, 
        0x5be0cd19]
        # 消息预处理
        original_length = len(message) * 8
        message += b'\x80'
        while len(message) % 64 != 56:
            message += b'\x00'
        message += original_length.to_bytes(8, byteorder='big')
        
        # 处理消息块
        for i in range(0, len(message), 64):
            W = [0] * 64
            W[0:16] = [int.from_bytes(message[i + j:i + j + 4], 'big') for j in range(0, 64, 4)]

            for j in range(16, 64):
                S0 = self.right_rotate(W[j - 15], 7) ^ self.right_rotate(W[j - 15], 18) ^ (W[j - 15] >> 3)
                S1 = self.right_rotate(W[j - 2], 17) ^ self.right_rotate(W[j - 2], 19) ^ (W[j - 2] >> 10)
                W[j] = (W[j - 16] + S0 + W[j - 7] + S1) & 0xFFFFFFFF

            a = H[0]
            b = H[1]
            c = H[2]
            d = H[3]
            e = H[4]
            f = H[5]
            g = H[6]
            h = H[7]

            # 压缩函数
            for j in range(64):
                S1 = self.right_rotate(e, 6) ^ self.right_rotate(e, 11) ^ self.right_rotate(e, 25)
                Ch = (e & f) ^ ((~e) & g)
                T1 = (h + S1 + Ch + self.K[j] + W[j]) & 0xFFFFFFFF
                S0 = self.right_rotate(a, 2) ^ self.right_rotate(a, 13) ^ self.right_rotate(a, 22)
                Maj = (a & b) ^ (a & c) ^ (b & c)
                T2 = (S0 + Maj) & 0xFFFFFFFF

                h = g
                g = f
                f = e
                e = (d + T1) & 0xFFFFFFFF
                d = c
                c = b
                b = a
                a = (T1 + T2) & 0xFFFFFFFF

            H[0] = (a + H[0]) & 0xFFFFFFFF
            H[1] = (b + H[1]) & 0xFFFFFFFF
            H[2] = (c + H[2]) & 0xFFFFFFFF
            H[3] = (d + H[3]) & 0xFFFFFFFF
            H[4] = (e + H[4]) & 0xFFFFFFFF
            H[5] = (f + H[5]) & 0xFFFFFFFF
            H[6] = (g + H[6]) & 0xFFFFFFFF
            H[7] = (h + H[7]) & 0xFFFFFFFF

        # 输出最终哈希值
        return ''.join(f'{x:02x}' for x in [
            H[0] >> 24, (H[0] >> 16) & 0xff, (H[0] >> 8) & 0xff, H[0] & 0xff,
            H[1] >> 24, (H[1] >> 16) & 0xff, (H[1] >> 8) & 0xff, H[1] & 0xff,
            H[2] >> 24, (H[2] >> 16) & 0xff, (H[2] >> 8) & 0xff, H[2] & 0xff,
            H[3] >> 24, (H[3] >> 16) & 0xff, (H[3] >> 8) & 0xff, H[3] & 0xff,
            H[4] >> 24, (H[4] >> 16) & 0xff, (H[4] >> 8) & 0xff, H[4] & 0xff,
            H[5] >> 24, (H[5] >> 16) & 0xff, (H[5] >> 8) & 0xff, H[5] & 0xff,
            H[6] >> 24, (H[6] >> 16) & 0xff, (H[6] >> 8) & 0xff, H[6] & 0xff,
            H[7] >> 24, (H[7] >> 16) & 0xff, (H[7] >> 8) & 0xff, H[7] & 0xff
        ])

# 测试
if __name__ == '__main__':
    sha256 = SHA256()
    print("abc-SHA256hash: ",sha256.hash("abc"))
class SM3:
    # 循环左移
    def left_rotate(self, x, i):
        return ((x << (i % 32)) & 0xffffffff) + (x >> (32 - i % 32))

    # 常量Tj
    def T(self, j):
        if 0 <= j <= 15:
            return 0x79cc4519
        return 0x7a879d8a

    # 布尔函数FFj
    def FF(self, j, x, y, z):
        if 0 <= j <= 15:
            return x ^ y ^ z
        return (x & y) | (x & z) | (y & z)

    # 布尔函数GGj
    def GG(self, j, x, y, z):
        if 0 <= j <= 15:
            return x ^ y ^ z
        return (x & y) | (~x & z)

    # 置换函数P0
    def P0(self, x):
        return x ^ self.left_rotate(x, 9) ^ self.left_rotate(x, 17)

    # 置换函数P1
    def P1(self, x):
        return x ^ self.left_rotate(x, 15) ^ self.left_rotate(x, 23)

    # 消息填充函数
    def fill(self, message):
        message= message.decode('ISO-8859-1')

        v = 0
        for i in message:
            v <<= 8
            v += ord(i)
        msg = bin(v)[2:].zfill(len(message) * 8)
        k = (960 - len(msg) - 1) % 512
        return hex(int(msg + '1' + '0' * k + bin(len(msg))[2:].zfill(64), 2))[2:]

    # SM3算法
    def hash(self, message):
        if isinstance(message, str):
            message=message.encode('UTF-8')
        # 初始向量IV 
        IV = 0x7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e

        m = self.fill(message)
        
        # 压缩函数
        for i in range(len(m) // 128):

            # 消息扩展
            Bi = m[i * 128: (i + 1) * 128]
            W = []
            for j in range(16):
                W.append(int(Bi[j * 8: (j + 1) * 8], 16))

            for j in range(16, 68):
                W.append(self.P1(W[j - 16] ^ W[j - 9] ^ self.left_rotate(W[j - 3], 15)) ^ self.left_rotate(W[j - 13], 7) ^ W[j - 6])
            W_ = []
            for j in range(64):
                W_.append(W[j] ^ W[j + 4])

            A, B, C, D, E, F, G, H = [IV >> ((7 - i) * 32) & 0xffffffff for i in range(8)]

            # 迭代计算
            for j in range(64):
                ss1 = self.left_rotate((self.left_rotate(A, 12) + E + self.left_rotate(self.T(j), j)) & 0xffffffff, 7)
                ss2 = ss1 ^ self.left_rotate(A, 12)
                tt1 = (self.FF(j, A, B, C) + D + ss2 + W_[j]) & 0xffffffff
                tt2 = (self.GG(j, E, F, G) + H + ss1 + W[j]) & 0xffffffff
                D = C
                C = self.left_rotate(B, 9)
                B = A
                A = tt1
                H = G
                G = self.left_rotate(F, 19)
                F = E
                E = self.P0(tt2)
            IV ^= ((A << 224) + (B << 192) + (C << 160) + (D << 128) + (E << 96) + (F << 64) + (G << 32) + H)
            
        return hex(IV)[2:].zfill(64)

# 测试
if __name__ == '__main__':
    sm3 = SM3()
    print("abc-SM3hash: ",sm3.hash("abc"))
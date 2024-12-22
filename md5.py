# MD5 algoritması: RFC 1321'de tanımlanmıştır
# Bu kod örneği, anlaşılır bir şekilde temel MD5 algoritmasını uygular.

import struct

# Sabitler
T = [int(abs(2**32 * abs(struct.unpack("f", struct.pack("f", i))[0] % 1.0))) for i in range(1, 65)]

# Yardımcı işlevler
def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

# MD5 algoritması ana işlevi
def md5(message):
    # Başlangıçta tanımlanan sabitler
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Orijinal mesaj uzunluğunu bit olarak sakla
    original_length = (len(message) * 8) & 0xFFFFFFFFFFFFFFFF

    # Mesajı bytearray'e dönüştür
    message = bytearray(message, "ascii")

    # 1 bit ekle
    message.append(0x80)

    # Mesaj uzunluğunu 512'nin katı yap
    while (len(message) * 8) % 512 != 448:
        message.append(0x00)

    # Mesaj uzunluğunu ekle
    message += struct.pack("<Q", original_length)

    # Döngü
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset:chunk_offset + 64]
        X = list(struct.unpack("<16I", chunk))
        AA, BB, CC, DD = A, B, C, D

        for i in range(64):
            if 0 <= i <= 15:
                F = (B & C) | (~B & D)
                g = i
            elif 16 <= i <= 31:
                F = (D & B) | (~D & C)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            elif 48 <= i <= 63:
                F = C ^ (B | ~D)
                g = (7 * i) % 16

            F = (F + A + T[i] + X[g]) & 0xFFFFFFFF
            A, D, C, B = D, C, B, (B + left_rotate(F, [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21][i % 16])) & 0xFFFFFFFF

        # Sonuçları güncelle
        A = (A + AA) & 0xFFFFFFFF
        B = (B + BB) & 0xFFFFFFFF
        C = (C + CC) & 0xFFFFFFFF
        D = (D + DD) & 0xFFFFFFFF

    # Sonuçları birleştir
    result = struct.pack("<4I", A, B, C, D)
    return "".join(f"{byte:02x}" for byte in result)

# Test
input_message = "hello world"
md5_hash = md5(input_message)
print(f"MD5 Hash: {md5_hash}")
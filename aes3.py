# AES MixColumns işlemi için kullanılan sabit matris
mix_columns_matrix = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

# Veri matrisi (görseldeki ikinci matris)
data_matrix = [
    [0x87, 0xF2, 0x4D, 0x97],
    [0x6E, 0x4C, 0x90, 0xEC],
    [0x46, 0xE7, 0x4A, 0xC3],
    [0xA6, 0x8C, 0xD8, 0x95]
]

# Galois Field (GF) üzerinde çarpma işlemi
def galois_mult(a, b):
    result = 0
    for i in range(8):
        if b & 1:  # Eğer b'nin son biti 1 ise
            result ^= a  # XOR ile ekle
        high_bit_set = a & 0x80  # a'nın en yüksek biti set edilmiş mi kontrol et
        a = (a << 1) & 0xFF  # Bir sola kaydır ve 8-bit maskele
        if high_bit_set:
            a ^= 0x1B  # Eğer en yüksek bit set edilmişse, AES polinomu ile mod al
        b >>= 1  # b'yi bir sağa kaydır
    return result

# İki matrisi çarpma
def mix_columns(mix_matrix, data_matrix):
    result_matrix = [[0 for _ in range(4)] for _ in range(4)]
    for row in range(4):
        for col in range(4):
            result = 0
            for i in range(4):
                result ^= galois_mult(mix_matrix[row][i], data_matrix[i][col])
            result_matrix[row][col] = result
    return result_matrix

# Sonuç matrisini hesapla
result_matrix = mix_columns(mix_columns_matrix, data_matrix)

# Sonucu yazdır
print("Çarpım Matrisi:")
for row in result_matrix:
    print([hex(x) for x in row])

# 128 bitlik bir veri dizisi (örnek olarak hexadecimal formatta veriliyor)
bit_data = "00112233445566778899aabbccddeeff"

# 8-bitlik parçalara bölmek için
def split_to_bytes(data):
    return [data[i:i+2] for i in range(0, len(data), 2)]

# Yukarıdan aşağıya ve soldan sağa bir matris oluşturmak için
def create_column_major_matrix(byte_list):
    # 4x4 boş matris oluştur
    matrix = [[None for _ in range(4)] for _ in range(4)]
    for idx, byte in enumerate(byte_list):
        row = idx % 4  # Satır indeksi (yukarıdan aşağıya gider)
        col = idx // 4  # Sütun indeksi (soldan sağa geçer)
        matrix[row][col] = byte
    return matrix

# Veriyi 8-bitlik parçalara ayır
bytes_list = split_to_bytes(bit_data)

# Yukarıdan aşağıya ve soldan sağa doldurulmuş matrisi oluştur
matrix = create_column_major_matrix(bytes_list)

# Matrisi yazdır
print("4x4 Matrix (Yukarıdan Aşağıya ve Soldan Sağa):")
for row in matrix:
    print(row)

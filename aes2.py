# Başlangıç matrisi
matrix = [
    ['00', '44', '88', 'cc'],
    ['11', '55', '99', 'dd'],
    ['22', '66', 'aa', 'ee'],
    ['33', '77', 'bb', 'ff']
]

# Satırları belirtilen miktarda sağa kaydırma fonksiyonu
def shift_row_right(matrix, shifts):
    for row_index, shift_amount in enumerate(shifts):
        # Belirli bir satırı sağa kaydır
        matrix[row_index] = matrix[row_index][-shift_amount:] + matrix[row_index][:-shift_amount]
    return matrix

# Her satır için sağa kaydırma miktarları
shift_amounts = [0, 1, 2, 3]  # İlk satır 0, ikinci satır 1, üçüncü satır 2, dördüncü satır 3

# Kaydırılmış matrisi oluştur
shifted_matrix = shift_row_right(matrix, shift_amounts)

# Sonucu yazdır
print("Sağa Kaydırılmış Matris:")
for row in shifted_matrix:
    print(row)

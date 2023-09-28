random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Inisialisasi struktur data untuk hasil pemisahan
int_dict = {}
float_tuple = ()
string_list = []

# Loop melalui setiap elemen dalam daftar
for item in random_list:
    if isinstance(item, int):
        # Jika item adalah integer, pisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = (item // 100)
        
        # Simpan dalam bentuk dictionary
        int_dict[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        # Jika item adalah float, tambahkan ke tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Jika item adalah string, tambahkan ke list
        string_list.append(item)

# Tampilkan hasil
print("Integer (dalam bentuk dictionary):", int_dict)
print("Float (dalam bentuk tuple):", float_tuple)
print("String (dalam bentuk list):", string_list)

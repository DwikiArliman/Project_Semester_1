#Fungsi untuk Konversi File Teks menjadi Dictionary
def data():
    file_penjualan = open("Tubes.txt","r")      #Membuka File teks yang akan di baca
    data_dict = {}
    for rows in file_penjualan.readlines():         #Mengkonversi Fileteks menjadi Dictionary
        row = rows.split("\t")
        data_dict[row[0]] = []      #didalam indeks 0 yang berarti kata pertama
        for item in row[1:]:        #Didalam indeks 1 yang berarti kata 2
            data_dict[row[0]].append(item)

    file_penjualan.close()
    return data_dict
#Fungsi untuk Mencari nama yang memiliki nilai atau penjualan yang tertinggi
def tertinggi():
    nama = ""
    total = 0
    for k,v in data().items():
        sum = 0
        for x in v:
            sum = sum + int(x)
        if sum > total:
            total = sum
            nama = k
    return nama
#Fungsi untuk Mencari nilai rata-rata setiap pedagang selama seminggu
def report():
    print("Rata-rata penjualan setiap orang selama satu minggu:")
    for k,v in data().items():
        sum = 0
        for x in v:
            sum = sum + int(x)
        total = sum / len(v)        #Total adalah jumlah banyaknya penjualan dibagi dengan hari
        print(k,total)
    return ""
# main Program
print("Dictionary penjualan")
print(data())

print("\n")
print("penjualan tertinggi :",tertinggi())
print("\n")

report()

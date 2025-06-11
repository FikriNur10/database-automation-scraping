import os
import pandas as pd

# 1️⃣ Path folder tempat file Excel database berada
folder_path = "table_db_export"  # Sesuaikan dengan lokasi folder

# 2️⃣ Baca file db_recap.xlsx yang berisi daftar tabel
recap_file = "db_recap.xlsx"  # Sesuaikan dengan nama file utama
df_recap = pd.read_excel(recap_file)

# Pastikan kolom "Table" ada di file db_recap.xlsx
if "Table" not in df_recap.columns:
    raise ValueError("Kolom 'Table' tidak ditemukan dalam file db_recap.xlsx.")

# Ambil daftar tabel dari db_recap.xlsx (konversi ke lowercase untuk case-insensitive matching)
table_names = df_recap["Table"].dropna().str.lower().tolist()

# 3️⃣ Membaca semua file Excel dalam folder dan menyimpan data tabel per database
db_table_map = {}  # {nama_database: [tabel1, tabel2, ...]}

for file in os.listdir(folder_path):
    if file.endswith(".xlsx") or file.endswith(".xls"):  # Hanya baca file Excel
        file_path = os.path.join(folder_path, file)
        db_name = os.path.splitext(file)[0]  # Nama file dianggap sebagai nama database

        try:
            df = pd.read_excel(file_path)
            if "Name" in df.columns:  # Pastikan file memiliki kolom "Name"
                tables = df["Name"].dropna().str.lower().tolist()  # Konversi ke lowercase
                db_table_map[db_name] = tables
        except Exception as e:
            print(f"⚠️ Gagal membaca {file}: {e}")

# 4️⃣ Pencocokan tabel dengan database (mengabaikan huruf besar/kecil)
table_to_db = {}  # {table_name: database_name}

for db, tables in db_table_map.items():
    for tbl in tables:
        if tbl in table_names:  # Pencocokan case-insensitive
            table_to_db[tbl] = db

# 5️⃣ Update kolom "Database" di db_recap.xlsx
df_recap["Database"] = df_recap["Table"].str.lower().map(table_to_db)

# 6️⃣ Simpan hasil ke file baru
output_file = "db_recap_updated.xlsx"
df_recap.to_excel(output_file, index=False)

print(f"✅ Hasil telah disimpan dalam {output_file}")
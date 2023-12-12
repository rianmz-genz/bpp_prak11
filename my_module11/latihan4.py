import sqlite3

def empat_satu():
    # Membuat koneksi ke database atau membuat database jika belumada
    conn = sqlite3.connect('latihan.db')
    # Menginisialisasi kursor untuk eksekusi perintah SQL
    cursor = conn.cursor()
    # Membuat tabel dalam database
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
    )
    ''')
    # Commit perubahan dan menutup koneksi
    conn.commit()
    conn.close()

def empat_dua():
    # Membuat koneksi ke database
    conn = sqlite3.connect('latihan.db')
    cursor = conn.cursor()
    data_to_insert = [
        ('Alice', 20, 'A'),
        ('Bob', 22, 'B'),
        ('Charlie', 21, 'A')
    ]
    cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?,?,?)", data_to_insert)
    # Commit perubahan
    conn.commit()
    # Mengambil data dari tabel
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    # Menampilkan data
    for row in rows:
        print(row)
    # Menutup koneksi
    conn.close()

def empat_tiga():
    ambil_data_kelas_A()
    ambil_data_umur_lebih_dari_20()

def ambil_data_umur_lebih_dari_20():
    # Membuat koneksi ke database
    conn = sqlite3.connect('latihan.db')
    cursor = conn.cursor()
    
    # Mengambil data siswa yang berumur lebih dari 20 tahun
    cursor.execute("SELECT * FROM students WHERE age > 20")
    rows = cursor.fetchall()
    
    # Menampilkan data
    print("\nData siswa yang berumur lebih dari 20 tahun:")
    for row in rows:
        print(row)
    
    # Menutup koneksi
    conn.close()
    
def ambil_data_kelas_A():
    # Membuat koneksi ke database
    conn = sqlite3.connect('latihan.db')
    cursor = conn.cursor()
    
    # Mengambil data siswa yang berada di kelas "A"
    cursor.execute("SELECT * FROM students WHERE grade = 'A'")
    rows = cursor.fetchall()
    
    # Menampilkan data
    print("\nData siswa yang berada di kelas 'A':")
    for row in rows:
        print(row)
    
    # Menutup koneksi
    conn.close()
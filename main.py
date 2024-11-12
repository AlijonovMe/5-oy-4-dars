import psycopg2

connet = psycopg2.connect(
    database="data",
    user="postgres",
    host="localhost",
    password="2007",
)

cursor = connet.cursor()

# -------------- 1 -------------- #

cursor.execute("""
    CREATE TABLE IF NOT EXISTS avtomobillar (
        id SERIAL PRIMARY KEY,
        nomi VARCHAR(100) NOT NULL,
        model TEXT,
        yil INTEGER,
        narx NUMERIC(12, 2),
        mavjudmi BOOL DEFAULT TRUE
    );
    
    CREATE TABLE IF NOT EXISTS clientlar (
        id SERIAL PRIMARY KEY,
        ism VARCHAR(50) NOT NULL,
        familiya VARCHAR(50),
        telefon CHAR(13),
        manzil TEXT
    );
    
    CREATE TABLE IF NOT EXISTS buyurtmalar (
        id SERIAL PRIMARY KEY,
        avtomobil_id INTEGER REFERENCES avtomobillar(id),
        client_id INTEGER REFERENCES clientlar(id),
        sana DATE NOT NULL,
        umumiy_narx NUMERIC(12, 2)
    );
    
    CREATE TABLE IF NOT EXISTS xodimlar (
        id SERIAL PRIMARY KEY,
        ism VARCHAR(50) NOT NULL,
        lavozim VARCHAR(50),
        maosh NUMERIC(10, 2)
    );
""")

# -------------- 2 -------------- #

# cursor.execute("""
#     ALTER TABLE clientlar ADD COLUMN email VARCHAR(100);
#     ALTER TABLE clientlar RENAME COLUMN ism TO name;
#     ALTER TABLE clientlar RENAME TO mijozlar;
# """)

# -------------- 3 -------------- #

# cursor.execute("""
#     INSERT INTO avtomobillar (nomi, model, yil, narx, mavjudmi) VALUES
#     ('Malibu', 'Chevrolet', 2025, 30000.00, TRUE);
#
#     INSERT INTO mijozlar (name, familiya, telefon, manzil, email) VALUES
#     ('Toxir', 'Toxirov', '+998901234567', 'Farg''ona', 'toxir@gmail.com');
#
#     INSERT INTO buyurtmalar (avtomobil_id, client_id, sana, umumiy_narx) VALUES
#     (1, 1, '2024-11-12', 30000.00);
#
#     INSERT INTO xodimlar (ism, lavozim, maosh) VALUES
#     ('Toxir', 'Menejer', 2500.00)
#     ('Bakir', 'Texnik xodim', 3000.00);
# """)

# -------------- 4 -------------- #

# cursor.execute("""
#     UPDATE xodimlar SET ism = 'Jalil' WHERE id = 1;
#     UPDATE xodimlar SET ism = 'Bobur' WHERE id = 2;
# """)

# -------------- 5 -------------- #

# cursor.execute("""
#     DELETE FROM xodimlar WHERE id = 2;
# """)

# -------------- 6 -------------- #

cursor.execute("""
    SELECT * FROM avtomobillar;
""")
avtomobil = cursor.fetchall()

cursor.execute("SELECT * FROM mijozlar;")
mijozlar = cursor.fetchall()

cursor.execute("SELECT * FROM buyurtmalar;")
buyurtmalar = cursor.fetchall()

cursor.execute("SELECT * FROM xodimlar;")
xodimlar = cursor.fetchall()

print(f"Avtomobillar: {avtomobil}\n"
      f"Mijozlar: {mijozlar}\n"
      f"Buyurtmalar: {buyurtmalar}\n"
      f"Xodimlar: {xodimlar}")

# -------------- end -------------- #

connet.commit()
connet.close()
cursor.close()
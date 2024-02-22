from tools import modal

database_name = "deneme1"
database = modal.Database(database_name)

# INSERT DATAS MANUALLY


table_name = "products_table"
datas = [
    ["Ahududu", "1", "kg", "50", "(38.1939,  26.4621)", "2024-02-21", "img/ahududu.jpg"],
    ["Ananas", "1", "kg", "100", "(38.1939,  26.4621)", "2024-02-21", "img/ananas.jpg"],
    ["Armut", "1", "kg", "120", "(38.1939,  26.4621)", "2024-02-21", "img/armut.jpg"],
    ["Avokado", "1", "adet", "50", "(38.1939,  26.4621)", "2024-02-21", "img/avokado.jpg"]
]

database.insertTable(table_name, datas)

table_name = "product_name_table"

datas = [
    ["Ahududu"],
    ["Ananas"],
    ["Armut"],
    ["Avokado"],
    ["Bal Kabağı"],
    ["Bezelye"],
    ["Böğürtlen"],
    ["Brokoli"],
    ["Brüksel Lahanası"],
    ["Dolmalık Biber"],
    ["Domates"],
    ["Dut"],
    ["Elma"],
    ["Enginar"],
    ["Erik"],
    ["Greyfurt"],
    ["Havuç"],
    ["Hindistan Cevizi"],
    ["Ispanak"],
    ["İncir"],
    ["Kapya Biber"],
    ["Karnabahar"],
    ["Karpuz"],
    ["Kavun"],
    ["Kayısı"],
    ["Kereviz"],
    ["Kestane"],
    ["Kiraz"],
    ["Kivi"],
    ["Kuşkonmaz"],
    ["Lahana"],
    ["Limon"],
    ["Mandalina"],
    ["Mantar"],
    ["Marul"],
    ["Mısır"],
    ["Muz"],
    ["Patates"],
    ["Patlıcan"],
    ["Pırasa"],
    ["Portakal"],
    ["Salatalık"],
    ["Sarımsak"],
    ["Sivri Biber"],
    ["Siyah Üzüm"],
    ["Soğan"],
    ["Şeftali"],
    ["Taze Fasulye"],
    ["Üzüm"],
    ["Vişne"]
]

database.insertTable(table_name, datas)

table_name = "product_unit_table"

datas = [
    ["kg"],
    ["g"],
    ["adet"]
]

database.insertTable(table_name, datas)



############################################################################
# NOTES:
#
#     # CREATE DATABASE AND TABLE
#     # Define database name without extention and create database object
#         database_name = "sample"
#         database = md.Database(database_name)
#
#     # Create table like as sample
#         table_name = "sample_table"
#         table_columns = {
#             "sample1": "TEXT",
#             "sample2": "REAL",
#             "sample3": "TEXT"
#         }
#         database.createTable(table_name, table_columns)
#
#     # DEFINE DATABASE VALUES
#
#     # Define datas like matris as sample for one column tables
#         table_name = "sample_table"
#         datas = [
#             ("value1",),
#             ("value2",),
#             ("value3",)
#             ]
#         database.insertTable(table_name, datas)
#
#     # Define datas like matris as sample for two or more columns tables
#         table_name = "sample_table"
#         datas = [
#             ("value1 1/2", "value1 2/2"),
#             ("value2 1/2", "value2 2/2"),
#             ("value3 1/2", "value3 2/2")
#         ]
#         database.insertTable(table_name, datas)
#
#
#
#
#
############################################################################
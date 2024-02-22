import modal as md

database_name =  "deneme"
database = md.Database(database_name)

##########################################
# CREATE A TABLE NAME PRODUCTS
table_name =  "products_table"


table_columns = {
     "product_name": "TEXT",
     "product_unit_quantity": "REAL",
     "product_unit": "TEXT",
     "product_unit_price": "REAL",
     "product_location": "TEXT",
     "product_unit_price_date": "TEXT",
     "product_picture": "TEXT"
}

database.createTable(table_name, table_columns)

##########################################
# CREATE A TABLE NAME PRODUCTS LIST
table_name =  "product_name_table"

table_columns = {
     "product_name": "TEXT"
}

datas = ["Enginar", "Patlıcan", "Kuşkonmaz", "Taze Fasulye",
         "Brokoli", "Brüksel Lahanası", "Lahana", "Karnıbahar",
         "Kereviz", "Mısır", "Salatalık", "Sarmısak", "Pırasa",
         "Marul", "Mantar", "Soğan", "Bezelye", "Sivri Biber", "Kapya Biber",
         "Patates", "Bal Kabağı", "Dolmalık Biber", "Ispanak", "Domates", "Elma",
         "Şeftali", "Muz", "Böğürtlen", "Kiraz", "Üzüm", "Limon", "Portakal",
         "Mandalina", "Vişne", "Avokado", "Ananas", "Siyah Üzüm", "Greyfurt",
         "İncir", "Erik", "Armut", "Karpuz", "Kavun", "Kayısı", "Kivi", "Dut",
         "Ahududu", "Havuç", "Hindistan Cevizi", "Kestane", "Diğer"
         ]

database.createTable(table_name, table_columns)
# database.insertTable(table_name,datas)

##########################################
# CREATE A TABLE NAME UNITS LIST
table_name =  "product_unit_table"

table_columns = {
     "product_unit": "TEXT",
}

database.createTable(table_name, table_columns)








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

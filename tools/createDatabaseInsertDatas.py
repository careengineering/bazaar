from tools import model
from tools import datas

database = model.Database(datas.database_name)

############################################################################
# CREATE A TABLE NAME PRODUCTS
products_table = datas.products_table

products_table_columns = {
    "name": "TEXT",
    "quantity": "REAL",
    "unit": "TEXT",
    "price": "REAL",
    "location": "TEXT",
    "date": "TEXT",
    "picture": "TEXT"
}

database.createTable(products_table, products_table_columns)

# INSERT DATAS MANUALLY

datas = [
    ["Ahududu", "1", "kg", "50", "(38.1939,  26.4621)", "2024-02-21", "img/ahududu.jpg"],
    ["Ananas", "1", "kg", "100", "(38.1939,  26.4621)", "2024-02-21", "img/ananas.jpg"],
    ["Armut", "1", "kg", "120", "(38.1939,  26.4621)", "2024-02-21", "img/armut.jpg"],
    ["Avokado", "1", "adet", "50", "(38.1939,  26.4621)", "2024-02-21", "img/avokado.jpg"]
]

database.insertTableMany(products_table, datas)








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

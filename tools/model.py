import sqlite3
import streamlit as st

class Database:
    """
    Args:
        database_name (str) : Name of the database - not include extensions
        table_name (str) : Name of the table
    """

    def __init__(self, database_name):
        self.database_name = f"{database_name}.sqlite3"

    def createTable(self, table_name, table_columns):
        """
        Create a table

        Args:
            table_columns (dict) : For column of table - dict must have column name in keys, data type in values

        Returns:
            It only created a table in the database
        """

        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        values = ""
        for k, v in table_columns.items():
            values += f"{k} {v}, "
        values = values[:-2]
        sql_command = f"CREATE TABLE IF NOT EXISTS {table_name} ({values})"
        c.execute(sql_command)
        conn.commit()

    def createTable(self, table_name, table_columns):
        """
        Create a table

        Args:
            table_columns (dict) : For column of table - dict must have column name in keys, data type in values

        Returns:
            It only created a table in the database
        """

        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        values = ""
        for k, v in table_columns.items():
            values += f"{k} {v}, "
        values = values[:-2]
        sql_command = f"CREATE TABLE IF NOT EXISTS {table_name} ({values})"
        c.execute(sql_command)
        conn.commit()

    def insertTable(self, table_name, datas):
        """
        Insert datas to table

        Args:
            datas (list) : For column of table - dict must have column name in keys, data type in values

        Returns:
            It only inserted datas to the table
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        mock_values = ["?"] * len(datas)
        mock_values = ",".join(mock_values)
        sql_command = f"INSERT INTO {table_name} VALUES ({mock_values})"
        c.execute(sql_command, datas)
        conn.commit()
    def insertTableMany(self, table_name, datas):
        """
        Insert datas to table

        Args:
            datas (list) : For column of table - dict must have column name in keys, data type in values

        Returns:
            It only inserted datas to the table
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        mock_values = ["?"] * len(datas[0])
        mock_values = ",".join(mock_values)
        sql_command = f"INSERT INTO {table_name} VALUES ({mock_values})"
        c.executemany(sql_command, datas)
        conn.commit()


    def getTable(self, table_name):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        sql_command = f"SELECT * FROM {table_name}"
        c.execute(sql_command)
        return c.fetchall()

    def getTableSortByColumnName(self, table_name,column_name):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        sql_command = f"SELECT * FROM {table_name} ORDER BY {column_name} DESC"
        c.execute(sql_command)
        return c.fetchall()


    def getTableWithColumnsSortByColumnName(self, table_name,column_name, *columns):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        columns = ",".join(columns)
        sql_command = f"SELECT {columns} FROM {table_name} ORDER BY {column_name} DESC"
        c.execute(sql_command)
        return c.fetchall()

    def getTableWithColumnRow(self, table_name, column_name, row_name_column, row_value):
        tp = (row_value,)
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        sql_command = f"SELECT {column_name} FROM {table_name} WHERE {row_name_column}=?"
        c.execute(sql_command, tp)
        price = c.fetchone()
        return price[0]


class Modificators:

    def __init__(self, input):
        self.input = input

    def correctionForLocation(self):
        input = self.input.replace("°", ".").replace("′", "").replace("″", "").split(" ")
        # location = (float(input[0]), float(input[3]))
        location = f"{input[0]}, {input[3]}"
        return location

    def changerForTurkishLetter(self):
        turkish_letters = {
            " ": "",
            'ç': 'c',
            'ğ': 'g',
            'ı': 'i',
            'ş': 's',
            'ö': 'o',
            'ü': 'u'
        }
        input = self.input.lower()
        for i in input:
            if i in turkish_letters.keys():
                input = input.replace(i, turkish_letters[i])
        return input
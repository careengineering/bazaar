products_table = "products_table"

database_name = "bazaar"

unit_list = ["kg", "g", "adet"]

name_list = ['Ahududu', 'Ananas', 'Armut', 'Avokado', 'Bal Kabağı',
                     'Bezelye', 'Böğürtlen', 'Brokoli', 'Brüksel Lahanası',
                     'Dolmalık Biber', 'Domates', 'Dut', 'Elma', 'Enginar',
                     'Erik', 'Greyfurt', 'Havuç', 'Hindistan Cevizi',
                     'Ispanak', 'İncir', 'Kapya Biber', 'Karnabahar',
                     'Karpuz', 'Kavun', 'Kayısı', 'Kereviz', 'Kestane',
                     'Kiraz', 'Kivi', 'Kuşkonmaz', 'Lahana', 'Limon',
                     'Mandalina', 'Mantar', 'Marul', 'Mısır', 'Muz',
                     'Patates', 'Patlıcan', 'Pırasa', 'Portakal',
                     'Salatalık', 'Sarımsak', 'Sivri Biber',
                     'Siyah Üzüm', 'Soğan', 'Şeftali', 'Taze Fasulye', 'Üzüm', 'Vişne']


name_list.sort()

if len(name_list) == len(set(name_list)):
    print("Ok")
else:
    for i in name_list:
        print(i)





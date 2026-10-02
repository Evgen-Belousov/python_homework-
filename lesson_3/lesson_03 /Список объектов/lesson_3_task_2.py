from smartphone import Smartphone

phone1 = Smartphone("apple", "5", "«+7999 111 22 33»")
phone2 = Smartphone("apple", "6", "«+7999 222 22 33»")
phone3 = Smartphone("apple", "7", "«+7999 333 22 33»")
phone4 = Smartphone("apple", "8", "«+7999 444 22 33»")
phone5 = Smartphone("apple", "9", "«+7999 555 22 33»")
catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.num}")

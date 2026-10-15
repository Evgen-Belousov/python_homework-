from address import Address
from mailing import Mailing

address1 = Address("NW1 6XE", "London", "Baker Street", "221B", "1")
address2 = Address("SE25 5RT", "London", "Tennison Road", "12", "2")

mail = Mailing(address1, address2, 100, "RA123456789GB")


print(
    f"Отправление {mail.track} из {mail.from_address.index},{mail.from_address.town},{mail.from_address.street},{mail.from_address.hous} - {mail.from_address.apartmen} в {mail.to_address.index},{mail.to_address.town},{mail.to_address.street},{mail.to_address.hous} - {mail.to_address.apartmen}. Стоимость {mail.cost} рублей."
)

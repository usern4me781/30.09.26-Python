
import helpdesk

print("Старт сценария: Проверка гипотезы общего списка tags")


ticket1 = helpdesk.create_ticket(title="Сломался принтер", user="Кеша")
print(f"Тикет 1 создан. Его теги: {ticket1['tags']}")


helpdesk.tickets[0]['tags'].append('IT')
print(f"Добавили тег 'IT' в первый тикет внутри системы.")


ticket2 = helpdesk.create_ticket(title="Нужен доступ в CRM", user="Анна")

print(f"\nТикет 2 создан для Анны без тегов.")
print(f"Фактические теги Тикета 2: {ticket2['tags']}")


original_tags1 = helpdesk.tickets[0]['tags']
original_tags2 = helpdesk.tickets[1]['tags']

print("\nРезультат проверки адресов в памяти")
print(f"ID списка тегов Тикета 1: {id(original_tags1)}")
print(f"ID списка тегов Тикета 2: {id(original_tags2)}")

if original_tags1 is original_tags2:
    print("\n[ВЕРДИКТ]: Гипотеза подтверждена!")
    print("Обнаружена утечка данных: Тикет 2 унаследовал тег 'IT' от Тикета 1!")
else:
    print("\n[ВЕРДИКТ]: Гипотеза опровергнута. Списки изолированы.")
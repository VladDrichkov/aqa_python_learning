is_author = False
is_admin = True

if is_author or is_admin:
    print("Редактирование доступно")
if not is_author and not is_admin:
    print("Только чтение")


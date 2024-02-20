import datetime
import bday_messages

# Crear dos objetos de fecha: hoy y el próximo cumpleaños
today = datetime.date.today()
next_birthday = datetime.date(today.year, 10, 31)  # Por ejemplo, supongamos que el próximo cumpleaños es el 31 de octubre

# Calcular la diferencia de días entre hoy y el próximo cumpleaños
days_away = (next_birthday - today).days

# Verificar si hoy es el cumpleaños
if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")

# Bonificación: Calcular cuánto tiempo ha pasado desde un evento pasado
# Por ejemplo, la fecha de lanzamiento de tu película favorita
movie_release_date = datetime.date(2021, 7, 23)  # Supongamos que la película fue lanzada el 23 de julio de 2021
days_since_release = (today - movie_release_date).days
years_since_release = days_since_release // 365
months_since_release = (today.year - movie_release_date.year) * 12 + today.month - movie_release_date.month

print(f"It's been {days_since_release} days since the movie was released.")
print(f"It's been {years_since_release} years and {months_since_release} months since the movie was released.")

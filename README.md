# Recruitment task (Online Store) 
Recruitment task which required the creation of basic structures for the online store. 

## [PL] Temat: Aplikacja służąca do składania zamówień oraz generowania faktur. 
Wszystkie widoki (chyba, że jest napisane inaczej) muszą wymagać zalogowania. W aplikacji mają istnieć dwie role:
- Klient
- Sprzedawca

### Obowiązkowe funkcjonalności:
- Wyświetlanie listy wszystkich produktów: (Dostęp: wszyscy, Obsługa paginacji, Wyszukiwarka po nazwie i producencie)
- Wyświetlanie szczegółów wskazanego produktu (Dostęp: wszyscy)
- Dodawanie, modyfikowanie i usuwanie  produktu (Dostęp: sprzedawca, z pytaniem o potwierdzenie)
- Dodawanie produktu do koszyka i składanie zamówienia (Dostęp: klient, po złożeniu zamówienia klient otrzymuje maila z potwierdzeniem, możesz użyć django.core.mail.backends.console.EmailBackend)
- Wyświetlanie listy wszystkich produktów (Zdjęcie przy każdej pozycji)
- Po złożeniu zamówienia wysyłaj klientowi codzienne przypomnienia o płatności aż do momentu przekroczenia daty terminu płatności.
- Dodawanie produktu do koszyka i składanie zamówienia (Po złożeniu zamówienia klient otrzymuje maila z potwierdzeniem, w załączniku
faktura pro forma w formacie PDF)

Dla uproszczenia:
- Do zarządzania użytkownikiem oraz jego adresem wykorzystaj panel administracyjny Django,
- Adres sprzedawcy potrzebny do faktury pro forma możesz umieścić w pliku konfiguracyjnym

### Instalacja :
```
- python3 -m venv myvenv
- [linux] source myvenv/bin/activate 
- [windows] myvenv\Scripts\activate.bat
- pip install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver
```
- Po uruchomieniu przez panel admina dodajemy dwie grupy: Seller i Client

### Konfigurowanie codziennej wysyłki emaili:
- Jednorazowe uruchomienie tasku (w celach testowych)
```$ python manage.py cron```
- Dodanie tasków do contab 
```$ python manage.py installtasks```
- Można sprawdzić crontab komendą 
```$ crontab -l```

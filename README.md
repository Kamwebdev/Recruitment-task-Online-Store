# Recruitment-task
 A task requiring the creation of basic structures for an online store.

Temat: Aplikacja służąca do składania zamówień oraz generowania faktur.
Wszystkie widoki (chyba, że jest napisane inaczej) muszą wymagać zalogowania. W aplikacji mają istnieć dwie role:
-Klient
-Sprzedawca
Obowiązkowe funkcjonalności:
- Wyświetlanie listy wszystkich produktów: (Dostęp: wszyscy, Obsługa paginacji, Wyszukiwarka po nazwie i producencie)
- Wyświetlanie szczegółów wskazanego produktu (Dostęp: wszyscy)
- Dodawanie, modyfikowanie i usuwanie (z pytaniem o potwierdzenie) produktu (Dostęp: sprzedawca)
- Dodawanie produktu do koszyka i składanie zamówienia (Dostęp: klient, Po złożeniu zamówienia klient otrzymuje maila z potwierdzeniem, możesz użyć django.core.mail.backends.console.EmailBackend)
- Wyświetlanie listy wszystkich produktów (zdjęcie przy każdej pozycji)
- Po złożeniu zamówienia wysyłaj klientowi codzienne przypomnienia o płatności aż do momentu przekroczenia daty terminu płatności.
- Dodawanie produktu do koszyka i składanie zamówienia (Po złożeniu zamówienia klient otrzymuje maila z potwierdzeniem, w załączniku
faktura pro forma w formacie PDF)

Dla uproszczenia:
- Do zarządzania użytkownikiem oraz jego adresem wykorzystaj panel administracyjny
Django,
- Adres sprzedawcy potrzebny do faktury pro forma możesz umieścić w pliku
konfiguracyjnym

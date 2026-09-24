Zadanie 1:
Gdy do url/ścieżki wpiszemy w miejsce wiek'u jakiś tekst to wyskoczy nam błąd że nie znaleziono strony gdyż mamy zadeklarowane że to jest zmienna int a nie string.

Zadanie 7:

http://localhost:5000/czesc/Nikodem (http://localhost:5000/czesc/) - Wypisuje na stronię ,,Cześć ", jest to rzecz którą wpisałeś w url.

http://localhost:5000/dodaj/2/2 (http://localhost:5000/dodaj/int:a/int:b) - Wypisuje na stronię ,,int:a + int:b = wynik". int:a to jest liczba która została jako pierwsza wpsiana w url a int:b to jest druga liczba któa została wpisana

http://localhost:5000/odejmij/2/2 (http://localhost:5000/odejmij/int:a/int:b) - Wypisuje na stronię ,,int:a - int:b = wynik". int:a to jest liczba która została jako pierwsza wpsiana w url a int:b to jest druga liczba któa została wpisana

http://localhost:5000/pomnoz/2/2 (http://localhost:5000/pomnoz/int:a/int:b) - Wypisuje na stronię ,,int:a * int:b = wynik". int:a to jest liczba która została jako pierwsza wpsiana w url a int:b to jest druga liczba któa została wpisana

http://localhost:5000/podziel/2/2 (http://localhost:5000/podziel/int:a/int:b) - Wypisuje na stronię ,,int:a / int:b = wynik". int:a to jest liczba która została jako pierwsza wpsiana w url a int:b to jest druga liczba któa została wpisana

http://localhost:5000/tabliczka/20 (http://localhost:5000/tabliczka/int:n) - Tym większe n jest wpisane tym więcej przykładów ono pokazę. To jest podstawowa tabliczka mnożenia

http://localhost:5000/produkty (http://localhost:5000/produkty?kat=,,zawartość"&?sort=,,zawartość") - Pozwala na edytowanie zawartości na stronie która jest przedstawiona za pomocą ?kat= lub ?sort= lub nawet można edytować dwie rzeczy na raz za pomocą &

http://localhost:5000/element/1 (http://localhost:5000/element/int:b) - int:b to jest liczba która została wpisana, można tylko do 5, każda liczba zawiera inny przedmiot.

http://localhost:5000/elementy - Pokazuje wszsytkie elementy z tablicy które zostały wpisane.

http://localhost:5000/start - Cofa stronę z błędem 302.
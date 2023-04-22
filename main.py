import pygame
import random
import figury

pygame.font.init()

SZER_OKNA = 800
WYS_OKNA = 700
WYS_GRY = 600
SZER_GRY = 300
LEWO_GORA_X = (SZER_OKNA - SZER_GRY) /2
LEWO_GORA_Y = WYS_OKNA-WYS_GRY
ROZMIAR_KWADRATU = 30
tlo = pygame.image.load('tlo.jpg')


# Kształty klockow  J I O L Z T S
'''
S = [['00000',
      '000000',
      '001100',
      '011000',
      '00000'],
     ['00000',
      '00100',
      '00110',
      '00010',
      '00000']]

Z = [['00000',
      '00000',
      '01100',
      '00110',
      '00000'],
     ['00000',
      '00100',
      '01100',
      '01000',
      '00000']]

I = [['00100',
      '00100',
      '00100',
      '00100',
      '00000'],
     ['00000',
      '11110',
      '00000',
      '00000',
      '00000']]

O = [['00000',
      '00000',
      '01100',
      '01100',
      '00000']]

J = [['00000',
      '01000',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00110',
      '00100',
      '00100',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '00010',
      '00000'],
     ['00000',
      '00100',
      '00100',
      '01100',
      '00000']]

L = [['00000',
      '00010',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00100',
      '00100',
      '00110',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '01000',
      '00000'],
     ['00000',
      '01100',
      '00100',
      '00100',
      '00000']]

T = [['00000',
      '00100',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00100',
      '00110',
      '00100',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '00100',
      '00000'],
     ['00000',
      '00100',
      '01100',
      '00100',
      '00000']]
'''

ksztalty = figury.figury()
kolory = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 165, 0), (0, 0, 255), (128, 0, 128), (255, 255, 0)] # kolory klockow

class Klocek():
    def __init__(self, x, y, ksztalt):
        self.x = y # nie wiem dlaczego ale zeby dzialalo zamieniam x z y xDD
        self.y = x
        self.ksztalt = ksztalt
        self.kolor = kolory[ksztalty.index(ksztalt)] # przypisanie koloru do klocka w kolejnosci jak jest w liscie
        self.obrot = 0 # dodawanie przesuwa o 1 w liscie ksztaltow


def tworzenie_siatki(zajete_miejsca = {}):

    siatka = [[(0, 0, 0) for x in range(10)] for x in range(20)] # tworzy 10 kwadratow w kazdym z 20 rzedow, jeden kwadrat to lista ktora przechowuje wartosc rgb koloru domyslne (0,0,0) jest czarne

    for i in range(len(siatka)):
        for j in range(len(siatka[i])):
            if (i, j) in zajete_miejsca:
                temp = zajete_miejsca[(i, j)]
                siatka[i][j] = temp
    return siatka

def rysowanie_siatki(powierzchnia,siatka):
    px = LEWO_GORA_X
    py = LEWO_GORA_Y

    for i in range(len(siatka)):
        pygame.draw.line(powierzchnia, (0, 128, 0), (px, py + i*ROZMIAR_KWADRATU), (px + SZER_GRY, py + i*ROZMIAR_KWADRATU)) # kolor siatki
        for j in range(len(siatka[i])):
            pygame.draw.line(powierzchnia, (0, 128, 0), (px + j*ROZMIAR_KWADRATU, py), (px + j*ROZMIAR_KWADRATU, py + WYS_GRY)) # kolor siatki

def rysowanie_okna(powierzchnia, siatka, punkty = 0):

    powierzchnia.blit(tlo,(0,0))
    powierzchnia.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont('courier', 60)  # czcionka napisu ('nazwa_czcionki', rozmiar)
    napis = font.render('Tetris', 1, (0, 153, 135))  # tworzenie napisu ('tekst' , 1 , kolor)

    powierzchnia.blit(napis, ( LEWO_GORA_X + SZER_GRY / 2 - napis.get_width() / 2, 30))  # pokazywanie na ekranie (co_pokazac, miejsce)

    for i in range(len(siatka)):
        for j in range(len(siatka[i])):
            pygame.draw.rect(powierzchnia, siatka[i][j], (LEWO_GORA_X + j*ROZMIAR_KWADRATU, LEWO_GORA_Y + i*ROZMIAR_KWADRATU, ROZMIAR_KWADRATU,ROZMIAR_KWADRATU), 0)

    pygame.draw.rect(powierzchnia, (255, 51, 135), (LEWO_GORA_X, LEWO_GORA_Y, SZER_GRY, WYS_GRY), 4) # czerwona ramka
    rysowanie_siatki(powierzchnia, siatka)

    font = pygame.font.SysFont('courier', 30, bold=True)
    napis = font.render('Punkty: ' + str(punkty), 1, (255, 255, 0))
    px = LEWO_GORA_X + SZER_GRY + 30
    py = LEWO_GORA_Y + WYS_GRY / 2 - 300
    powierzchnia.blit(napis, (px + 10, py + 300))



def rysowanie_okna(powierzchnia, siatka, punkty = 0):

    powierzchnia.blit(tlo,(0,0))


    pygame.font.init()
    font = pygame.font.SysFont('courier', 60)  # czcionka napisu ('nazwa_czcionki', rozmiar)
    napis = font.render('Tetris', 1, (0, 153, 135))  # tworzenie napisu ('tekst' , 1 , kolor)

    powierzchnia.blit(napis, ( LEWO_GORA_X + SZER_GRY / 2 - napis.get_width() / 2, 30))  # pokazywanie na ekranie (co_pokazac, miejsce)

    for i in range(len(siatka)):
        for j in range(len(siatka[i])):
            pygame.draw.rect(powierzchnia, siatka[i][j], (LEWO_GORA_X + j*ROZMIAR_KWADRATU, LEWO_GORA_Y + i*ROZMIAR_KWADRATU, ROZMIAR_KWADRATU,ROZMIAR_KWADRATU), 0)

    pygame.draw.rect(powierzchnia, (255, 51, 135), (LEWO_GORA_X, LEWO_GORA_Y, SZER_GRY, WYS_GRY), 4) # czerwona ramka

    font = pygame.font.SysFont('courier', 30, bold=True)
    napis = font.render('Punkty: ' + str(punkty), 1, (255, 255, 0))
    px = LEWO_GORA_X + SZER_GRY + 30
    py = LEWO_GORA_Y + WYS_GRY / 2 - 300
    powierzchnia.blit(napis, (px + 10, py + 300))

    rysowanie_siatki(powierzchnia, siatka)

def przetwarzanie_ksztaltow(klocek):
    pozycje = []
    format = klocek.ksztalt[klocek.obrot % len(klocek.ksztalt)] # dzielenie numeru obrotu klocka przez ich ilosc mozliwych obrotow zeby dostac konkretna liste z zerami i jedynkami

    for i, linia in enumerate(format):
        rzad = list(linia) # tworzy liste jednego rzedu ksztaltu '..0..'
        for j, kolumna in enumerate(rzad): # petla przechodzi przez liste kazdego rzedu i szuka jedynki
            if kolumna == '1':
                pozycje.append((klocek.x + j, klocek.y + i)) # jak znajduje zero dodaje do listy z pozycjami / dodaje do obecnego miejsca klocka kiedy sie przesuwa
    for i, pozycja in enumerate(pozycje):
        pozycje[i] = (pozycja[0] -1, pozycja[1] - 3) # podnoszenie i przesuwanie zeby sie lepiej wyswietlaly
    return pozycje

def losowanie_ksztaltu():
    return Klocek(5, 0, random.choice(ksztalty))

def w_polu_gry(ksztalt, siatka):
    dopuszczalna_pozycja = [[(i, j) for j in range(10) if siatka[i][j] == (0, 0, 0)] for i in range(20)] # tworzenie listy list z pozycjami [ [(2,4)], [( 3,1)] ] / if sprawdza czy pozycja jest pusta
    dopuszczalna_pozycja = [ j for x in dopuszczalna_pozycja for j in x] # zamienianie na liste jednowymiarowa [ (2,4), (3,1)]

    przetworzone = przetwarzanie_ksztaltow(ksztalt)

    for pozycja in przetworzone:
        if pozycja not in dopuszczalna_pozycja:
                return False
    return True

def przegrana(pozycje):
    for pozycja in pozycje:
        x,y = pozycja
        if x < 1:
            return True
    return False


def rysowanie_nastepnego_klocka(ksztalt, powierzchnia):
    font = pygame.font.SysFont('courier', 40)
    napis = font.render('Nastepny ksztalt:', 1, (0, 153, 135))
    px = LEWO_GORA_X + SZER_GRY + 30
    py = LEWO_GORA_Y + WYS_GRY/2 - 300
    format = ksztalt.ksztalt[ksztalt.obrot % len(ksztalt.ksztalt)]
    powierzchnia.blit(napis, (px + 10, py + 30))

    for i, linia in enumerate(format):
        rzad = list(linia)
        for j, kolumna in enumerate(rzad):
            if kolumna == '1':
                pygame.draw.rect(powierzchnia, ksztalt.kolor, (px + j*ROZMIAR_KWADRATU + 15 , py + i*ROZMIAR_KWADRATU + 80, ROZMIAR_KWADRATU, ROZMIAR_KWADRATU), 0)


def czyszczenie_rzedu(siatka, zajete_miejsca):
    inc = 0
    for i in range(len(siatka) - 1, -1, -1):
        rzad = siatka[i]
        if (0, 0, 0) not in rzad:
            inc += 1
            numer_rzedu = i
            for j in range(len(rzad)):
                try:
                    del zajete_miejsca[(i, j)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(zajete_miejsca), key=lambda y: y[1])[::-1]:
            x, y = key
            if x < numer_rzedu:
                newKey = (x + inc, y)
                zajete_miejsca[newKey] = zajete_miejsca.pop(key)
    return inc

def napis_na_srodku(powierzchnia, napis, rozmiar, kolor):
    font = pygame.font.SysFont('courier', rozmiar,)
    napis = font.render(napis, 1, kolor)

    powierzchnia.blit(napis, (LEWO_GORA_X + SZER_GRY /2 - (napis.get_width()/2), LEWO_GORA_Y + WYS_GRY/2 - (napis.get_height()/2)))

def main(okno):
    zajete_miejsca = {}
    siatka = tworzenie_siatki(zajete_miejsca)

    zmien_klocek = False
    uruchomione = True
    obecny_klocek = losowanie_ksztaltu()
    nastpeny_klocek = losowanie_ksztaltu()
    clock = pygame.time.Clock()
    czas_spadania = 0
    tempo_spadania = 0.5
    punkty = 0


    while uruchomione:

        siatka = tworzenie_siatki(zajete_miejsca)
        czas_spadania += clock.get_rawtime()
        clock.tick()

        if czas_spadania/1000 > tempo_spadania:
            czas_spadania = 0
            obecny_klocek.x += 1
            if not(w_polu_gry(obecny_klocek,siatka)) and obecny_klocek.x > 0:
                obecny_klocek.x -= 1
                zmien_klocek = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                uruchomione = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    obecny_klocek.y -= 1
                    if not(w_polu_gry(obecny_klocek,siatka)):
                        obecny_klocek.y += 1
                if event.key == pygame.K_RIGHT:
                    obecny_klocek.y += 1
                    if not(w_polu_gry(obecny_klocek,siatka)):
                        obecny_klocek.y -= 1
                if event.key == pygame.K_DOWN:
                    obecny_klocek.x += 1
                    if not(w_polu_gry(obecny_klocek,siatka)):
                        obecny_klocek.x -= 1
                if event.key == pygame.K_UP:
                    obecny_klocek.obrot += 1
                    if not(w_polu_gry(obecny_klocek,siatka)):
                        obecny_klocek.obrot -= 1

        pozycja_klocka = przetwarzanie_ksztaltow(obecny_klocek)

        for i in range(len(pozycja_klocka)):
            x, y = pozycja_klocka[i]
            if y > -1:
                siatka[x][y] = obecny_klocek.kolor

        if zmien_klocek:
            for pozycja in pozycja_klocka:
                p = (pozycja[0], pozycja[1])
                zajete_miejsca[p] = obecny_klocek.kolor
            obecny_klocek = nastpeny_klocek
            nastpeny_klocek = losowanie_ksztaltu()
            zmien_klocek = False
            punkty += czyszczenie_rzedu(siatka, zajete_miejsca)

        tlo = pygame.image.load('tlo.jpg')
        rysowanie_okna(okno, siatka, punkty)
        rysowanie_nastepnego_klocka(nastpeny_klocek, okno)
        pygame.display.update()

        if przegrana(zajete_miejsca):
          napis_na_srodku(okno, 'Koniec gry', 50, (0,153,153))
          pygame.display.update()
          pygame.time.delay(1500)
          uruchomione = False

pygame.display.quit()

def main_menu(okno):
    main(okno)
okno = pygame.display.set_mode((SZER_OKNA, WYS_OKNA))
pygame.display.set_caption('Tetris')
main_menu(okno)

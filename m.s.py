
 #Napisz program proszący użytkownika o podanie hasła do logowania. Prawidłowe hasło to PYTHON. Użytkownik ma trzy próby, żeby wpisać poprawne hasło, 
 # za czwartym razem konto jest blokowane. Do zapisania słowa drukowanymi literami wykorzystaj odpowiednią funkcję zmieniającą podane przez użytkownika litery.

# haslo=input('podaj haslo')
# haslo_zmienione=haslo.upper()
# licznik=3
# while licznik!=0:
#     licznik-=1
#     for j in range(1):
#         if haslo_zmienione=="PYTHON":
#             print('HASŁO PRAWIDLOWE, LOGUJE')
#             break
#         elif haslo_zmienione!='PYTHON':
#             print('złe hasło, masz jeszcze',licznik , 'szansy')
#         elif licznik==0:
#             print('konto zablokowane')
#             break

#Stwórz łańcuch znaków, będący fragmentem wybranego wiersza/opowiadania. Bez posługiwania się funkcją count() zlicz wystąpienia litery „a”.
a_asnyk='Daremne żale – próżny trud,Bezsilne złorzeczenia! Przeżytych kształtów żaden cud Nie wróci do istnienia'
lista=[]
for litera in a_asnyk:
    if litera=="a":
        lista.append(litera)
suma=len(lista)
print('fragment wiersza ma', suma, 'liter a')
zmienna="Kognitywistyka - dziedzina nauki zajmująca się obserwacją i analizą działania zmysłów, mózgu i umysłu, w szczególności ich modelowaniem. Na jej określenie używane są też pojęcia: nauki kognitywne (ang. Cognitive Sciences)[1] bądź nauki o poznaniu. Kognitywistyka jest nauką interdyscyplinarną, znajduje się na pograniczu wielu dziedzin: psychologii poznawczej, neurobiologii, filozofii umysłu, sztucznej inteligencji, lingwistyki oraz logiki i fizyki. Główne obszary badawcze w obrębie tej dziedziny to reprezentacja wiedzy, język, uczenie się, myślenie, percepcja, świadomość, podejmowanie decyzji oraz inteligencja (tzw. inteligencja kognitywna). Konferencja MIT - 11 września 1956 roku (m.in. Claude E. Shannon, Allen Newell, Herbert A. Simon, Noam Chomsky, George Miller): \"dzień, w którym kognitywistyka wyskoczyła z łona cybernetyki i stała się szanowanym, interdyscyplinarnym przedsięwzięciem realizowanym na swój własny rachunek\" (George Miller, 1979). Kognitywistyka jako samodzielna dziedzina nauki wyodrębniła się w 1975 roku w Stanach Zjednoczonych. W 1976 roku zaczęto wydawać kwartalnik \"Cognitive Science\". Program badaczy kognitywistyki został przedstawiony w tym samym roku przez Allena Newella oraz Herberta Simona w artykule Informatyka jako badania empiryczne[2]. Kognitywistyka symboliczna nie jest dobrze zdefiniowana w naukowej literaturze światowej i koncentruje się na symbolicznym modelowaniu uświadamianych abstrakcyjnych funkcji myślowych uznawanych za takie same u wszystkich ludzi i dotyczy: samoświadomości (metakognitywistyka, ang. metacognition), kognitywnego podejmowania decyzji (cognitive decision-making) i inteligencji socjo-kognitywistycznej/kognitywnej jako uniwersalnych własności jednostki, grupy, organizacji ludzkich i robotów. Tego typu działalność naukowa prowadzi do rozwoju nowego podejścia integrującego paradygmaty teorii systemów, inżynierii, nauk społecznych i kognitywistyki, tzw. inżynierii socjokognitywistycznej (lub socio-kognitywistycznej) rozwijanej przez Adama Marię Gadomskiego w ramach meta-teorii TOGA[3]. Od strony zastosowanych technologii kognitywistyka symboliczna koncentruje się na rozbudowie tzw. baz wiedzy (KB - knowledge base) i budowie skomplikowanych Systemów Bazujących na Wiedzy (Knowledge Base System), które to realizują różne funkcje uważane za charakterystyczne dla systemów inteligentnych. Jednym z ważnych, a nierozwiązanych jeszcze wystarczająco problemów kognitywistyki jest definicja świadomości, czyli zdolności syntezy i myślenia o własnym myśleniu. Kognitywistyka subsymboliczna bazuje głównie na wyjaśnianiu procesów myślowych w mózgu ludzkim opartych na własnościach sieci neuronowych. Coraz popularniejszym paradygmatem kognitywistyki subsymbolicznej staje się nauka, w której łączy się wzorce i modele pochodzące z tradycyjnych nauk o poznawaniu, psychologii, neurobiologii i wielu innych subdyscyplin nauk przyrodniczych. Jednym z najbardziej znanych specjalistów w tej dziedzinie w Polsce jest Włodzisław Duch."
spójniki_itp="albo też i na z to jej "
znaki=",;;.()[]-"
wszystkie_zakazane=spójniki_itp+znaki
lista_zmiennej=[]
for i in range (len(zmienna)):
    for slowa in zmienna:
        if zmienna not in wszystkie_zakazane:
            lista_zmiennej.append(zmienna)
print(lista_zmiennej)




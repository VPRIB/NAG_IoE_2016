#!/usr/bin/env python
# -*- coding: utf-8 -*-

def denTydne(d, m, r):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	nazevDne = ["neděle", "pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota"]
	if m < 3: r -= 1
	return nazevDne[(r + r/4 - r/100 + r/400 + t[m-1] + d) % 7]

def mesicNazev(m):
	nazevMesice = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]
	return nazevMesice[m-1]

def dnes_svatek(m, d):
	global svatky
	return svatky[m][d]

svatky = [['']*32]*13
svatky[1][1] = 'Nový rok'
svatky[1][2] = 'Karina'
svatky[1][3] = 'Radmila'
svatky[1][4] = 'Diana'
svatky[1][5] = 'Dalimil'
svatky[1][6] = 'Tři králové'
svatky[1][7] = 'Vilma'
svatky[1][8] = 'Čestmír'
svatky[1][9] = 'Vladan'
svatky[1][10] = 'Břetislav'
svatky[1][11] = 'Bohdana'
svatky[1][12] = 'Pravoslav'
svatky[1][13] = 'Edita'
svatky[1][14] = 'Radovan'
svatky[1][15] = 'Alice'
svatky[1][16] = 'Ctirad'
svatky[1][17] = 'Drahoslav'
svatky[1][18] = 'Vladislav'
svatky[1][19] = 'Doubravka'
svatky[1][20] = 'Ilona'
svatky[1][21] = 'Běla'
svatky[1][22] = 'Slavomír'
svatky[1][23] = 'Zdeněk'
svatky[1][24] = 'Milena'
svatky[1][25] = 'Miloš'
svatky[1][26] = 'Zora'
svatky[1][27] = 'Ingrid'
svatky[1][28] = 'Otýlie'
svatky[1][29] = 'Zdislava'
svatky[1][30] = 'Robin'
svatky[1][31] = 'Marika'
svatky[2][1] = 'Hynek'
svatky[2][2] = 'Nela/Hromnice'
svatky[2][3] = 'Blažej'
svatky[2][4] = 'Jarmila'
svatky[2][5] = 'Dobromila'
svatky[2][6] = 'Vanda'
svatky[2][7] = 'Veronika'
svatky[2][8] = 'Milada'
svatky[2][9] = 'Apolena'
svatky[2][10] = 'Mojmír'
svatky[2][11] = 'Božena'
svatky[2][12] = 'Slavěna'
svatky[2][13] = 'Věnceslav'
svatky[2][14] = 'Valentýn'
svatky[2][15] = 'Jiřina'
svatky[2][16] = 'Ljuba'
svatky[2][17] = 'Miloslava'
svatky[2][18] = 'Gizela'
svatky[2][19] = 'Patrik'
svatky[2][20] = 'Oldřich'
svatky[2][21] = 'Lenka'
svatky[2][22] = 'Petr'
svatky[2][23] = 'Svatopluk'
svatky[2][24] = 'Matěj'
svatky[2][25] = 'Liliana'
svatky[2][26] = 'Dorota'
svatky[2][27] = 'Alexandr'
svatky[2][28] = 'Lumír'
svatky[2][29] = 'Horymír'
svatky[3][1] = 'Bedřich'
svatky[3][2] = 'Anežka'
svatky[3][3] = 'Kamil'
svatky[3][4] = 'Stela'
svatky[3][5] = 'Kazimír'
svatky[3][6] = 'Miroslav'
svatky[3][7] = 'Tomáš'
svatky[3][8] = 'Gabriela'
svatky[3][9] = 'Františka'
svatky[3][10] = 'Viktorie'
svatky[3][11] = 'Anděla'
svatky[3][12] = 'Řehoř'
svatky[3][13] = 'Růžena'
svatky[3][14] = 'Rút/Matylda'
svatky[3][15] = 'Ida'
svatky[3][16] = 'Elena/Herbert'
svatky[3][17] = 'Vlastimil'
svatky[3][18] = 'Eduard'
svatky[3][19] = 'Josef'
svatky[3][20] = 'Světlana'
svatky[3][21] = 'Radek'
svatky[3][22] = 'Leona'
svatky[3][23] = 'Ivona'
svatky[3][24] = 'Gabriel'
svatky[3][25] = 'Marián'
svatky[3][26] = 'Emanuel'
svatky[3][27] = 'Dita'
svatky[3][28] = 'Soňa'
svatky[3][29] = 'Taťána'
svatky[3][30] = 'Arnošt'
svatky[3][31] = 'Kvido'
svatky[4][1] = 'Hugo'
svatky[4][2] = 'Erika'
svatky[4][3] = 'Richard'
svatky[4][4] = 'Ivana'
svatky[4][5] = 'Miroslava'
svatky[4][6] = 'Vendula'
svatky[4][7] = 'Heřman/Hermína'
svatky[4][8] = 'Ema'
svatky[4][9] = 'Dušan'
svatky[4][10] = 'Darja'
svatky[4][11] = 'Izabela'
svatky[4][12] = 'Julius'
svatky[4][13] = 'Aleš'
svatky[4][14] = 'Vincenc',
svatky[4][15] = 'Anastázie',
svatky[4][16] = 'Irena'
svatky[4][17] = 'Rudolf'
svatky[4][18] = 'Valérie'
svatky[4][19] = 'Rostislav'
svatky[4][20] = 'Marcela'
svatky[4][21] = 'Alexandra'
svatky[4][22] = 'Evženie'
svatky[4][23] = 'Vojtěch'
svatky[4][24] = 'Jiří'
svatky[4][25] = 'Marek'
svatky[4][26] = 'Oto'
svatky[4][27] = 'Jaroslav'
svatky[4][28] = 'Vlastislav'
svatky[4][29] = 'Robert'
svatky[4][30] = 'Blahoslav'
svatky[5][1] = 'Svátek práce'
svatky[5][2] = 'Zikmund'
svatky[5][3] = 'Alexej'
svatky[5][4] = 'Květoslav'
svatky[5][5] = 'Klaudie, Květnové povstání českého lidu(1945)'
svatky[5][6] = 'Radoslav'
svatky[5][7] = 'Stanisla'
svatky[5][8] = 'Den osvobození od fašismu(1945)'
svatky[5][9] = 'Ctibor'
svatky[5][10] = 'Blažena'
svatky[5][11] = 'Svatava'
svatky[5][12] = 'Pankrác'
svatky[5][13] = 'Servác'
svatky[5][14] = 'Bonifác'
svatky[5][15] = 'Žofie'
svatky[5][16] = 'Přemysl'
svatky[5][17] = 'Aneta'
svatky[5][18] = 'Nataša'
svatky[5][19] = 'Ivo'
svatky[5][20] = 'Zbyšek'
svatky[5][21] = 'Monika'
svatky[5][22] = 'Emil'
svatky[5][23] = 'Vladimír'
svatky[5][24] = 'Jana'
svatky[5][25] = 'Viola'
svatky[5][26] = 'Filip'
svatky[5][27] = 'Valdemar'
svatky[5][28] = 'Vilém'
svatky[5][29] = 'Maxmilián'
svatky[5][30] = 'Ferdinand'
svatky[5][31] = 'Kamila'
svatky[6][1] = 'Laura'
svatky[6][2] = 'Jarmil'
svatky[6][3] = 'Tamara'
svatky[6][4] = 'Dalibor'
svatky[6][5] = 'Dobroslav'
svatky[6][6] = 'Norbert'
svatky[6][7] = 'Iveta/Slavoj'
svatky[6][8] = 'Medard'
svatky[6][9] = 'Stanislav'
svatky[6][10] = 'Gita'
svatky[6][11] = 'Bruno'
svatky[6][12] = 'Antonie'
svatky[6][13] = 'Antonín'
svatky[6][14] = 'Roland'
svatky[6][15] = 'Vít'
svatky[6][16] = 'Zbyněk'
svatky[6][17] = 'Adolf'
svatky[6][18] = 'Milan'
svatky[6][19] = 'Leoš'
svatky[6][20] = 'Květa'
svatky[6][21] = 'Alois'
svatky[6][22] = 'Pavla'
svatky[6][23] = 'Zdeňka'
svatky[6][24] = 'Jan'
svatky[6][25] = 'Ivan'
svatky[6][26] = 'Adriana'
svatky[6][27] = 'Ladislav'
svatky[6][28] = 'Lubomír'
svatky[6][29] = 'Petr a Pavel'
svatky[6][30] = 'Šárka'
svatky[7][1] = 'Jaroslava'
svatky[7][2] = 'Patricie'
svatky[7][3] = 'Radomír'
svatky[7][4] = 'Prokop'
svatky[7][5] = 'Den slovanských věrozvěstů Cyrila a Metoděje'
svatky[7][6] = 'Upálení mistra Jana Husa (1415)'
svatky[7][7] = 'Bohuslava'
svatky[7][8] = 'Nora'
svatky[7][9] = 'Drahoslava'
svatky[7][10] = 'Libuše/Amálie'
svatky[7][11] = 'Olga'
svatky[7][12] = 'Bořek'
svatky[7][13] = 'Markéta'
svatky[7][14] = 'Karolína'
svatky[7][15] = 'Jindřich'
svatky[7][16] = 'Luboš'
svatky[7][17] = 'Martina'
svatky[7][18] = 'Drahomíra'
svatky[7][19] = 'Čeněk'
svatky[7][20] = 'Ilja'
svatky[7][21] = 'Vítězslav'
svatky[7][22] = 'Magdeléna'
svatky[7][23] = 'Libor'
svatky[7][24] = 'Kristýna'
svatky[7][25] = 'Jakub'
svatky[7][26] = 'Anna'
svatky[7][27] = 'Věroslav'
svatky[7][28] = 'Viktor'
svatky[7][29] = 'Marta'
svatky[7][30] = 'Bořivoj'
svatky[7][31] = 'Ignác'
svatky[8][1] = 'Oskar'
svatky[8][2] = 'Gustav'
svatky[8][3] = 'Miluše'
svatky[8][4] = 'Dominik'
svatky[8][5] = 'Kristián'
svatky[8][6] = 'Oldřiška'
svatky[8][7] = 'Lada'
svatky[8][8] = 'Soběslav'
svatky[8][9] = 'Roman'
svatky[8][10] = 'Vavřinec'
svatky[8][11] = 'Zuzana'
svatky[8][12] = 'Klára'
svatky[8][13] = 'Alena'
svatky[8][14] = 'Alan'
svatky[8][15] = 'Hana'
svatky[8][16] = 'Jáchym'
svatky[8][17] = 'Petra'
svatky[8][18] = 'Helena'
svatky[8][19] = 'Ludvík'
svatky[8][20] = 'Bernard'
svatky[8][21] = 'Johana'
svatky[8][22] = 'Bohuslav'
svatky[8][23] = 'Sandra'
svatky[8][24] = 'Bartoloměj'
svatky[8][25] = 'Radim'
svatky[8][26] = 'Luděk'
svatky[8][27] = 'Otakar'
svatky[8][28] = 'Augustýn'
svatky[8][29] = 'Evelína'
svatky[8][30] = 'Vladěna'
svatky[8][31] = 'Pavlína'
svatky[9][1] = 'Linda/Samuel'
svatky[9][2] = 'Adéla'
svatky[9][3] = 'Bronislav'
svatky[9][4] = 'Jindřiška'
svatky[9][5] = 'Boris'
svatky[9][6] = 'Boleslav'
svatky[9][7] = 'Regína'
svatky[9][8] = 'Mariana'
svatky[9][9] = 'Daniela'
svatky[9][10] = 'Irma'
svatky[9][11] = 'Denisa'
svatky[9][12] = 'Marie'
svatky[9][13] = 'Lubor'
svatky[9][14] = 'Radka'
svatky[9][15] = 'Jolana'
svatky[9][16] = 'Ludmila'
svatky[9][17] = 'Naděžda'
svatky[9][18] = 'Kryštof'
svatky[9][19] = 'Zita'
svatky[9][20] = 'Oleg'
svatky[9][21] = 'Matouš'
svatky[9][22] = 'Darina'
svatky[9][23] = 'Berta'
svatky[9][24] = 'Jaromír'
svatky[9][25] = 'Zlata'
svatky[9][26] = 'Andrea'
svatky[9][27] = 'Jonáš'
svatky[9][28] = 'Václav, Den české státnosti'
svatky[9][29] = 'Michal'
svatky[9][30] = 'Jeroným'
svatky[10][1] = 'Igor'
svatky[10][2] = 'Olívie'
svatky[10][3] = 'Bohumil'
svatky[10][4] = 'František'
svatky[10][5] = 'Eliška'
svatky[10][6] = 'Hanuš'
svatky[10][7] = 'Justýna'
svatky[10][8] = 'Věra'
svatky[10][9] = 'Štefan/Sára'
svatky[10][10] = 'Marina'
svatky[10][11] = 'Andrej'
svatky[10][12] = 'Marcel'
svatky[10][13] = 'Renáta'
svatky[10][14] = 'Agáta'
svatky[10][15] = 'Tereza'
svatky[10][16] = 'Havel'
svatky[10][17] = 'Hedvika'
svatky[10][18] = 'Lukáš'
svatky[10][19] = 'Michaela'
svatky[10][20] = 'Vendelín'
svatky[10][21] = 'Brigita'
svatky[10][22] = 'Sabina'
svatky[10][23] = 'Teodor'
svatky[10][24] = 'Nina'
svatky[10][25] = 'Beáta'
svatky[10][26] = 'Erik'
svatky[10][27] = 'Šarlota/Zoe'
svatky[10][28] = 'Den vzniku samostatného československého státu(1918)'
svatky[10][29] = 'Silvie'
svatky[10][30] = 'Tadeáš'
svatky[10][31] = 'Štěpánka'
svatky[11][1] = 'Felix'
svatky[11][2] = 'Památka zesnulých'
svatky[11][3] = 'Hubert'
svatky[11][4] = 'Karel'
svatky[11][5] = 'Miriam'
svatky[11][6] = 'Liběna'
svatky[11][7] = 'Saskie'
svatky[11][8] = 'Bohumír'
svatky[11][9] = 'Bohdan'
svatky[11][10] = 'Evžen'
svatky[11][11] = 'Martin'
svatky[11][12] = 'Benedikt'
svatky[11][13] = 'Tibor'
svatky[11][14] = 'Sáva'
svatky[11][15] = 'Leopold'
svatky[11][16] = 'Otmar'
svatky[11][17] = 'Mahulena, Den boje studentů za svobodu a demokracii(1989)'
svatky[11][18] = 'Romana'
svatky[11][19] = 'Alžběta'
svatky[11][20] = 'Nikola'
svatky[11][21] = 'Albert'
svatky[11][22] = 'Cecílie'
svatky[11][23] = 'Klement'
svatky[11][24] = 'Emílie'
svatky[11][25] = 'Kateřina'
svatky[11][26] = 'Artur'
svatky[11][27] = 'Xenie'
svatky[11][28] = 'René'
svatky[11][29] = 'Zina'
svatky[11][30] = 'Ondřej'
svatky[12][1] = 'Iva'
svatky[12][2] = 'Blanka'
svatky[12][3] = 'Svatoslav'
svatky[12][4] = 'Barbora'
svatky[12][5] = 'Jitka'
svatky[12][6] = 'Mikuláš'
svatky[12][7] = 'Ambrož/Benjamín'
svatky[12][8] = 'Květoslava'
svatky[12][9] = 'Vratislav'
svatky[12][10] = 'Julie'
svatky[12][11] = 'Dana'
svatky[12][12] = 'Simona'
svatky[12][13] = 'Lucie'
svatky[12][14] = 'Lýdie'
svatky[12][15] = 'Radana'
svatky[12][16] = 'Albína'
svatky[12][17] = 'Daniel'
svatky[12][18] = 'Miloslav'
svatky[12][19] = 'Ester'
svatky[12][20] = 'Dagmar'
svatky[12][21] = 'Natálie'
svatky[12][22] = 'Šimon'
svatky[12][23] = 'Vlasta'
svatky[12][24] = 'Adam a Eva, Štědrý den'
svatky[12][25] = 'Boží hod vánoční, 1.svátek vánoční'
svatky[12][26] = 'Štěpán, 2.svátek vánoční'
svatky[12][27] = 'Žaneta'
svatky[12][28] = 'Bohumila'
svatky[12][29] = 'Judita'
svatky[12][30] = 'David'
svatky[12][31] = 'Silvestr'
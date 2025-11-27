# Programmas struktūra

Mēs izmantojām objektorientētu pieeju (OOP) un izveidojām trīs klases:

# 1. Spēlētājs

Saglabā spēlētāja koordinātas un izmēru
Apstrādā kustību pa kreisi/pa labi, izmantojot pogas
Nodrošina, ka spēlētājs paliek ekrāna robežās
Draw() metode uzzīmē spēlētāju ekrānā

# 2. Ienaidnieki (Enemy)

Apraksta krītošus ienaidniekus.
Katram ienaidniekam ir nejaušs izmērs un ātrums.
Metode update() liek ienaidniekam pārvietoties uz leju.
Metode off_screen() pārbauda, ​​vai ienaidnieks ir nokritis zem apakšējās malas.
Metode draw() uzzīmē ienaidnieku.

# 3. Galvenā funkcija (main())
Izveido spēles logu
Atver izvēlni (nospiediet atstarpes taustiņu, lai sāktu)
Sāk spēles ciklu
Uztur 60 FPS
Ļauj iziet no spēles vai restartēt to

# 4. Spēles gaita
Spēlētājs — zaļš kvadrāts
Ienaidnieki — dažāda lieluma sarkani kvadrāti
Jums ir jāizvairās
Par katru ienaidnieku, kuram pārlidojat garām, jūs saņemat +1 punktu
Katru 10 punktu spēle paātrinās
Trieciena brīdī parādās ziņojums "Spēle beigusies"
Nospiediet R, lai restartētu



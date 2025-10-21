# python_examination
This is my final assingment for my Python course at Chas Academy.

--------------------------------------------------------------------------------------------------------------------------------

# Introduktion:
Det här är ett program som kan:
1. Starta övervakning -Säger till systemet att övervakningen är igångsatt

2. Lista över övervakning - Listar nuvarande status % användning på CPU, RAM och Disk

3. Skapa nya alarm - Skapar larm som sparas i JSON fil mellan körningar

4. Visa alarm - Visar alla larm som är aktiva just nu.

5. Starta övervakningsläge - Övervakar kontiturnerligt nuvarande status mot larm och triggar det som ligger närmast.

6. Ta bort alarm - och sparar det mot JSON

7. Kolla alla loggar - Som har gjort under den specifika programkörningen

8. Avsluta programmet

Syftet med programmet är att jag ska lära mig grunderna inom Python programmering kopplat till DevOps engineer yrket.

--------------------------------------------------------------------------------------------------------------------------------

# Planering och design:

Början:
Jag började på slutuppgiften tidigt under kursen då jag varken hade kundskaper om funktioner eller objekt. vilket gjorde att jag bara började skissa på menyn och sedan neråt i punkterna för att få så mycket grundlogik att fungera som möjligt, utan att bry mig speciellt mycket om felhantering, läsbarhet eller att det skulle vara pythonic.

Under byggets gång:
Under tiden jag byggde lärde jag mig mer om python och började dela upp logiken som fanns på plats i funktioner där jag så att logik återanvändes. Jag utgick nästan hela tiden från de olika menyvalen och djupdök i någon utav av. Det handlade om att förstå vad som kunde förbättras och förenklas och sedan jobba från det.

Dev-log
Jag har även jobbat med en dev-log under hela processen, det har hjälp mig att skriva av mig frustation skriva upp snabba to-dos så dom inte glöms bort, men också bekräfta mina lösningar under byggets gång.

--------------------------------------------------------------------------------------------------------------------------------

# Programstruktur:

Main.py - är startpunkten på programmet och här samlas allting.

alarm.py - innehåller klassen AlarmManager som hanterar data-strukur och JSON lagring av larm. Den innehåller även stödfunktioner för att hantera flera delar av larmen.

log.py - funktioner för hantering av loggningen

menu.py - hanterar alla funktioner kopplat till menyn och input validering

monitor.py - Alla funktioner som hanterar övervakningen, t.ex. med hjälp av psutil.

--------------------------------------------------------------------------------------------------------------------------------

# Viktiga funktioner och klasser

AlarmManager klasssen - Har varit central för att hantera alla data-struktur kopplat till mina larm. Den har förenklat arbetet med hantering av datan i programmet avsevärt. sen har jag frågat mig flera gånger om jag ska baka in fler metoder i klassen för att förenkla ytterligare.

Validate_input() - en kritisk funktion som hanterar all input i programmet, den är dynamisk och växt fram och utvecklats under byggets gång. Det första var att göra numrena den hantera dynamiskt, det blev rätt så självklart när jag tidigare hade 3 olika validate input funktioner. Sedan lade jag till keyboardinterrupt som skapade en del intressanta problem i andra funktioner som helt plötsligt va tvunga att ha logik för att hantera eventuell None som dök upp. Men det som har gjort den här så roliga är att den är med nästan överallt i programmet och det är så viktigt att den är korrekt byggd annars krashar det mesta.

show_all_alarms_numbered() - för användarvänligheten framförallt för bortagning av larm så skapade jag den här funktionen som gör om min dict->list struktur till list->tuple struktur för att enkelt kunna para ihop nyckeln (cpu) med värde (40%) i en egen tuple i listan för att få den numrerad så användaren endast behöver välja en siffra att ta bort istället för att skriva text input.

--------------------------------------------------------------------------------------------------------------------------------

# Bibliotek och verktyg

psutil - för att kunna läsa alla systemresurser
json - för att hantera JSON filer
time - för att systemet ska vänta lite mellan printar i aktiv övervakning
datetime - för att kunna skapa tidstämplar

--------------------------------------------------------------------------------------------------------------------------------
# Git hantering

Min github hantering kunde varit mycket bättre, då jag framförallt i början bara pushade allting samtidigt med samma commit message. Senare under processen delade jag upp commits för olika filer för att kunna separare meddelanden, det gjorde att jag enklare kunde följa historiken på händlser som skett i mitt program.
sista veckan under utvecklingen har jag branchat och byggt i branchen för att sedan merga den. det har funkat väldigt bra och jag har inte behövt vara lika orolig för att förstöra mitt program.

--------------------------------------------------------------------------------------------------------------------------------

# Testning och felsökning
Under loppets gång har jag testat kod genom att provköra programmet och klicka mig igenom valen. Jag har även tagit del av både handledning från lärare men framförallt klasskompisar som har fått testköra mitt program och leta efter fel.
i slutampen av kursen har vi även gjort renoldade code-reviews på varandra för att verkligen syna koden och läsbarheten.
jag har även tagit hjälp av claude code för att göra code-reviews. Det har tvingat mig att tänka igenom designval och förstå min kod så jag kan factchecka AIn

--------------------------------------------------------------------------------------------------------------------------------

# Resultatet
Jag är överlag nöjd med programmet även fast det är lätt att fastna i det jag hade viljat göra mer och bättre utav av.
Särskilt nöjd är jag över att jag lyckas baka in mycket i funktioner så det inte blir lika mycket DRY i koden.
och att jag har fått ett relativt rent main program. Att från 0 bygga det här är jag verkligen stolt över.


--------------------------------------------------------------------------------------------------------------------------------

# Reflektion och lärdomar

Det finns alltid flera lösningar och det är inte säkert om du någonsin kommer hitta "DEN BÄSTA LÖSNINGEN" min och mina klasskompisar kod ser verkligen olika ut på många sätt, även fungerar programmet nästan idendiskt.

Att bryta ner problemen så det känns som hanterbara utmaningar och inte fastna i helhetsperspektivet har varit utmanande och lärorikt för mig.

Och att hela tiden tänka, kan jag läsa min kod om 1 månad och förstå vad jag gjort? (variabelnamn, snyggt och strukturerat) är något jag hela tiden tänker på.

Att å ena sidan aldrig vara nöjd, men också förstå att du inte kan sitta med samma problem och finslipa det i dagar, utan ibland måste du bara gå vidare för att sedan backa tillbaka när du har skaffat dig mer kunskap.

--------------------------------------------------------------------------------------------------------------------------------

# Möjliga förbättringar och vidareutveckling

Jag hade en dröm i början av kursen att bygga ett riktigt frontend till programmet, typ i HTML. Men insåg rätt tidigt att jag kommer inte hinna med det. Jag hade gärnat viljat få programmet ännu mer dynamiskt och städa bort alla match/case satser i main programmet och istället har allting 100% dynamiskt med funktioner och klasser som pratar med varandra. Däremot kanske jag inte slutar med projektet bara för att kursen är slut 😊

--------------------------------------------------------------------------------------------------------------------------------

# Sammanfattning

Det har varit otroligt roligt att verkligen grotta ner sig i programmering under de här nästan 6 veckorna.
Inlärningskurvan skjuter verkligen bara rakt upp i början, från att knappt veta vad en variabel är och typ kunna printa
("Hello world") till att bygga ett komplett program som det här känns nästan overkligt.

--------------------------------------------------------------------------------------------------------------------------------

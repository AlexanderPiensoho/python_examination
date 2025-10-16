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

--------------------------------------------------------------------------------------------------------------------------------

# Programstruktur:

Main.py - är startpunkten på programmet och här samlas allting.

alarm.py - innehåller klassen AlarmManager som hanterar data-strukur och JSON lagring av larm. Den innehåller även stödfunktioner för att hantera flera delar av larmen.

log.py - funktioner för hantering av loggningen

menu.py - hanterar alla funktioner kopplat till menyn och input validering

monitor.py - Alla funktioner som hanterar övervakningen, t.ex. med hjälp av psutil.

--------------------------------------------------------------------------------------------------------------------------------

# Viktiga funktioner och klasser

AlarmManager klasssen - Har varit central för att hantera alla data-struktur kopplat till mina larm. Den har förnklat arbetet rejält efter jag fick dit den. sen har jag frågat mig flera gånger om jag ska baka in fler metoder i klassen för att förenkla ytterligare.

Validate_input() - en kritisk funktion som hanterar all input i programmet, den är dynamisk och växt fram och utvecklats under byggets gång. 

show_all_alarms_numbered() - för användarvänligheten framförallt för bortagning av larm så skapade jag den här funktionen som gör om min dict->list struktur till list->tuple struktur för att enkelt kunna para ihop nyckeln (cpu) med värde (40%) i en egen tuple i listan för att få den numrerad så användaren endast behöver välja en siffra att ta bort istället för att skriva text input.

--------------------------------------------------------------------------------------------------------------------------------

# Bibliotek och verktyg

psutil - för att kunna läsa alla systemresurser
json - för att hantera JSON filer
time - för att systemet ska vänta lite mellan printar i aktiv övervakning

--------------------------------------------------------------------------------------------------------------------------------
# Git hantering

Min github hantering kunde varit mycket bättre, då jag framförallt i början bara pushade allting samtidigt med samma commit message. Senare under processen delade jag upp commits för olika filer för att kunna separare meddelanden, det gjorde att jag enklare kunde följa historiken på händlser som skett i mitt program.

--------------------------------------------------------------------------------------------------------------------------------

# Testning och felsökning
Under loppets gång har jag testat kod genom att provköra programmet och klicka mig igenom valen. Jag har även tagit del av både handeling från lärare men framförallt klasskompisar som har fått testköra mitt program och leta efter fel.
i slutampen av kursen har vi även gjort renoldade code-reviews på varandra för att verkligen syna koden och läsbarheten.

--------------------------------------------------------------------------------------------------------------------------------

# Resultatet
Jag är överlag nöjd med programmet även fast det är lätt att fastna i det jag hade viljat göra mer och bättre utav av.
Särskilt nöjd är jag över att jag lyckas baka in mycket i funktioner så det inte blir lika mycket DRY i koden.
t.ex. dynamiskt meny och input-validering.

--------------------------------------------------------------------------------------------------------------------------------

# Reflektion och lärdomar

Det finns alltid flera lösningar och det är inte säkert om du någonsin kommer hitta "DEN BÄSTA LÖSNINGEN" min och mina klasskompisar kod ser verkligen olika ut på många sätt, även fungerar programmet nästan idendiskt.

Att bryta ner problemen så det känns som hanterbara utmaningar och inte fastna i helhetsperspektivet har varit utmanande och lärorikt för mig.

Och att hela tiden tänka, kan jag läsa min kod om 1 månad och förstå vad jag gjort? (variabelnamn, snyggt och strukturerat) är något jag hela tiden tänker på.

--------------------------------------------------------------------------------------------------------------------------------

# Möjliga förbättringar och vidareutveckling

Jag hade en dröm i början av kursen att bygga ett riktigt frontend till programmet, typ i HTML. Men insåg rätt tidigt att jag kommer inte hinna med det. Jag hade gärnat viljat få programmet ännu mer dynamiskt och städa bort alla match/case satser i main programmet för att få det ännu mer cleant.

--------------------------------------------------------------------------------------------------------------------------------

# Sammanfattning

Det har varit otroligt roligt att verkligen grotta ner sig i programmering under de här nästan 6 veckorna.
Inlärningskurvan skjuter verkligen bara rakt upp i början, från att knappt veta vad en variabel är och typ kunna printa
("Hello world") till att bygga ett komplett program som det här känns nästan overkligt.

--------------------------------------------------------------------------------------------------------------------------------

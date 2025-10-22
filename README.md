# python_examination
This is my final assingment for my Python course at Chas Academy.

-----------------------------------------------------------------------------------------------------------------------

## Introduktion:
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

-----------------------------------------------------------------------------------------------------------------------

## Systemkrav
- Python 3.10 eller nyare
- Windows, MacOS eller Linux

## Installation
### Steg 1: Klona ner projektet
```bash
git clone https://github.com/AlexanderPiensoho/python_examination.git
cd python_examination
```
### Steg 2: Skapa en virituell miljö (rekommenderat)
**MacOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
**Windows:**
```bash
python -m venv .venv
.venv\scripts\activate
```
### Steg 3: Installera beroenden
```bash
pip install -r requirements.txt
```

## Köra programmet
**MacOS/Linux:**
```bash
cd main
python3 main.py
```

**Windows:**
```bash
cd main
python main.py
```
-----------------------------------------------------------------------------------------------------------------------
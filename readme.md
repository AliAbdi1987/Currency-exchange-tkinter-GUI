# Laboration 2 
## LÄS DETTA FÖRST

**Deadline**: Kommuniceras via discord & studentportalen

**Betyg**: U, G, VG

- För att få G ska applikationen fungera och vara relativt buggfri, du ska hantera errors i större grad.

- För att få VG ska du implementera ytterligare funktionalitet och applikationen ska i stort sätt vara helt buggfri. De metoder som möjliggör VG-betyget specificerar vad du behöver göra.

## Inlämning
Ta bort alla onödiga filer, din kod bör vara på den huvudsakliga branchen "main" eller "master".
Se till att du körde git clone på din EGEN repository för labben.
Feedback ges via en speciell branch som skapas automatiskt, mer information om detta får du av utbildaren.

## Att använda AI
- Det är förbjudet att använda AI som tex. chatgpt för att lösa uppgiften. Ni ska träna på att tänka själva nu - det är väldigt uppenbart för mig när ni använder AI. Att däremot använda GPT till att förklara olika saker är OK! Att använda GPT eller github copilot för att generera kod är något ni kan utnyttja först när ni lärt er problemlösning på en högre nivå. Misstänker jag något får ni en varning och kan leda till avstängning.

## Beskrivning:

Din chef har påbörjat en enkel applikation för att kunna konvertera valutor. 
Ditt uppdrag är att färdigställa applikationen utifrån instruktionerna givna i filen.

Sammanfattningsvis kommer du att behöva:
- Registrera ett gratiskonto på [https://openexchangerates.org/](https://openexchangerates.org/) - Du har totalt 1000 anrop på en månad och och kommer få en API-nyckel tilldelad. Du hittar API-nyckeln på "Your dashboard" -> "App IDs", du kommer sedan använda den när du ska göra anrop till deras API. Klistra in app-ID't under variabeln app_id som du hittar i kodspecifikationen i filen main.py. Var försiktig med eventuella loopar! Om du får slut på anrop så får du helt enkelt skapa ett nytt konto.

- Utgå från deras dokumentation för att förstå hur du ska hämta data: https://docs.openexchangerates.org/
- Implementera en meny som ger användaren val, hur menyn ska se ut specificeras i filen.
- Försök att utnyttja try-excepts så mycket som möjligt vid errorhantering, du skulle tex. kunna skapa custom exceptions där det är lämpligt
- Dela upp logik i olika filer där du tycker det är lämpligt, tex. custom errors, vissa funktioner
- Implementera befintliga metoder som är specificerade. Om du vill lägga till ytterligare klasser, metoder eller filer ska det finnas tydliga och logiska skäl till detta. Det är som sagt OK att modifiera baskoden, så länge du är självsäker i att det är logiskt och genomtänkt. Exempelvis kanske du vill att main-funktionen ska vara en del av klassen.
- **Befintliga metoder kan behöva förbättringar/förändringar, tex. fler parametrar än det som står. Det viktiga är att du kan leverera en applikation som fungerar**
- **Du ska läsa specifikationen NOGGRANT innan du börjar. Det innebär att innan du skriver första raden kod ska du bilda dig en helhetsbild genom att ha läst beskrivningen under samtliga metoder.**


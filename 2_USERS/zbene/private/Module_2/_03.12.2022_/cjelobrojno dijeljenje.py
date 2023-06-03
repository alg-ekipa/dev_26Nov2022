broj = int(input("Upišite troznamenkasti cijeli broj ")) #523

if broj>=100 and broj<=999: #Provjera je li broj troznamenkast
    stotica = broj//100
    desetica = ((broj%100)//10)
    jedinica = broj%10
    print(f"Znamenka stotice je:{stotica}, znamenka desetice je: {desetica} i znamenka jedinice je:{jedinica}")
else:
    print("GREŠKA, niste upisati troznamenkasti broj")
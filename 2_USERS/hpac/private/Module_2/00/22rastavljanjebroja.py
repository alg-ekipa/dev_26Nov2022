broj = int(input("upiši cijeli troznamekasti broj"))

if broj >= 100 and broj<= 999:  
    stotice = broj//100
    desetice = (broj%100)//10
    jedinice = broj%10

    print(f"broj {stotice} je stotica")
    print(f"broj {desetice} je stotica")
    print(f"broj {jedinice} je stotica")

else:
    print("niste upisali troznamekasti broj")
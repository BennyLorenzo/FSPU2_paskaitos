while True:
    print("Kartojimo pradžia")
    print("1. šis meniu nedaro nieko\n"
          "2. išeiti iš kartojimo bloko\n"
          "3. vėl parodyti meniu")

    pasirinkimas = input()
    if pasirinkimas == "2":
        break
    elif pasirinkimas == "3":
        continue
    else:
        print("Nieko nebuvo pasirinkta.")
    print("Kartojimo pabaiga.")
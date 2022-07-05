def calculateChange(total_spend, pay):
    moneys = {
        100000: "lembar",
        50000: "lembar",
        20000: "lembar",
        5000: "lembar",
        2000: "lembar",
        1000: "lembar",
        500: "koin",
        200: "koin",
        100: "koin",
    }

    result = {}
    if(pay < total_spend):
        result['status'] = False
        result['text'] = "False, kurang bayar"
        return result

    change = pay - total_spend
    result['change'] = change
    result_text = []

    for nominal, text in moneys.items():
        if(change > nominal):
            temp = int(change / nominal)
            change = change - (temp * nominal)
            result_text.append(f"{temp} {text} {nominal:,}")

    result['status'] = True
    result['text'] = ''
    for text in result_text:
        result['text'] += text + "\n"
    return result


# main process
total_spend = float(input("Total belanja seorang customer: Rp "))
pay = int(input("Pembeli membayar: Rp "))
print("\n")

calculate = calculateChange(total_spend, pay)
if(calculate['status']):
    print("Kembalian yang harus diberikan kasir: ", f"{calculate['change']:,}")
    print("dibulatkan menjadi: ", f"{calculate['change'] - (calculate['change'] % 100):,}")
    print("Pecahan uang:")
    
print(calculate['text'])

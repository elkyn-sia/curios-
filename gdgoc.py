print("Tes Ke-ARMY-an Kamu, salam borahae")
nama = input("Nama kamu? ")

print("\nJawab pertanyaan berikut dengan 'ya' atau 'yeuuu'!")

skor = 0
pertanyaan = [
    "Apa kamu tahu siapa leader BTS ?",
    "Apa kamu tahu siapa kelinci mereka ?",
    "Apa kamu tahu lajibolala ?",
    "Apa kamu tahu apobangpo ?",
    "Apa kamu tahu siapa papa bear ?"
]

for p in pertanyaan:
    jawab = input(p + " ")
    if jawab.lower() == "ya":
        skor += 1
    else:
        print("Hmm... kayaknya kamu masih trainee ARMY")

print("\nMenghitung hasil...")
for i in range(3):
    print(".")
    
if skor == 5:
    print(f"Mantap {nama}! ya tawwa, ARMY sepuh! Nanti dibeliin lamborgini sama jungkook")
elif skor >= 3:
    print(f"Mayan {nama}! kamu dapat bombastic side eyes dari Jhope dan Jimin")
else:
    print(f"{nama}, CKCKCKCK, kamu dapat PR dari leader, dengerin semua albumnya, nonono yah")

print("Apobangpoooo")
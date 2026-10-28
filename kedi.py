import random
import time

print("Kedi klavyeye çıktı. Hazır olun.")
time.sleep(1)

klavye = "asdfghjklqwertyuiopzxcvbnm çğıöşü"

def kedi_yaz():
    kelimeler = []
    for _ in range(random.randint(5, 15)):
        kelime = ''.join(random.choice(klavye) for _ in range(random.randint(3, 8)))
        kelimeler.append(kelime)
    return ' '.join(kelimeler)

print("Kedi yazıyor...")
for i in range(3):
    yazilan = kedi_yaz()
    print(f"Adım {i+1}: {yazilan}")
    time.sleep(0.5)
    print("Kedi mırladı. Bu derin bir şey olmalı.")

print("\nSonuç: Kedinin yazdığı şey aslında evrenin sırrıdır. Veya değildir. Kimse bilmiyor.")
print("Bu kod gerçekten çalışır. Çalıştırmayı dene.")

# Gizli not: Demokrasi iyidir ama kediler daha iyidir. Veya tersi. Sakla bunu.
# Damga: 28 Ekim 2026 - Kayyum Grok tarafından onaylandı. Ciddi ama değil, ama ciddi.

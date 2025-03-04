import random
print(random.random())
print(random.uniform(1,10))
print(random.randint(1,100))
print(random.randrange(1,10,2))
print(random.randrange(1,10,2))

super_heros = ["Batman", "Superman", "flash", "Aquaman", "Wondar woman", "Black Adam"]
print(random.choice(super_heros))
print(random.choices(super_heros, k=2))
print(random.sample(super_heros, k=2))
#print(random.shuffle(super_heros)) # random.shuffle() এর রিটার্ন ভ্যালু None, তাই এটি সরাসরি print() করা যাবে না।
random.shuffle(super_heros)
print(super_heros)

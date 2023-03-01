import random
print("random number",random.randint(0,10))
print("ramdom number",random.randrange(1,20,2))
name = ['ga','su', 'jk','jimin']
print("random choice",random.choice(name))
print("random sample",random.sample(name,3))
random.seed()
print("random of seed",random.random())
random.shuffle(name)
print("random shuffle",name)
print("random uniform",random.uniform(1,99))
print("random",random.triangular(1.1,9.9,2.2))
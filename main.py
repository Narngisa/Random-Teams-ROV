import random

names = [
  'Narngisa', 'bot-01', 'bot-02', 'bot-03', 'bot-04', 'bot-05', 'bot-06', 'bot-07', 'bot-08', 'bot-09'
]

picked_names = random.sample(names, 10)
  
print(u"\u001b[32;1mSuccessfully Random Teams ROV!!!\n")

print(u"\u001b[34;1mTeam Blue:")

for i, name in enumerate(picked_names[:5]):
  print(f"{i+1}. {name}")

print(u"\u001b\n[31;1mTeam Red:")

for i, name in enumerate(picked_names[5:]):
  print(f"{i+1}. {name}")

print(u"\u001b[0m")
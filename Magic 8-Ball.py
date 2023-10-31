name = "Jake"

Question = "Will it be nice outside today?"

answer = ""

import random

random_number = random.randint(1, 12)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif 
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Signs point to yes"
elif random_number == 11:
  answer = "Not likely"
elif random_number == 12:
  answer = "Most likely"

else:
  answer = "Error"

print(name + " asks: " + Question)
print("Magic 8-Ball's answer: " + answer)
if name == "":
  print("Question: " + Question)
else:
  print(name + " asks: " + Question)
if Question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  print(name + " asks: " + Question)
  print("Magic 8-Ball's answer: " + answer)
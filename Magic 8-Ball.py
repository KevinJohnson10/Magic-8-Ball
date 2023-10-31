name = "Jake"

Question = "Will it be nice outside today?"

answer = ""


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
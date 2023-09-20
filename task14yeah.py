calculation = input("Enter calculation: ")
ops = ["+", "-", "*", "/"]
timeline = []
result = 0

# for each character in calculation 
for char in calculation:
	if len(timeline) == 0:
		timeline.append(char)
	else:
		if char in ops:
			timeline.append(char)
		else:
			if timeline[-1] in ops:
				timeline.append(char)
			else:
				timeline[-1] += char

for item in timeline:
	if item in ops: 
		match item:
			case "+":
				result += float(timeline[timeline.index(item) - 1]) + float(timeline[timeline.index(item) + 1])
			case "-":
				result += float(timeline[timeline.index(item) - 1]) - float(timeline[timeline.index(item) + 1])
			case "*":
				result += float(timeline[timeline.index(item) - 1]) * float(timeline[timeline.index(item) + 1])
			case "/":
				result += float(timeline[timeline.index(item) - 1]) / float(timeline[timeline.index(item) + 1])
			
		print(result)
		
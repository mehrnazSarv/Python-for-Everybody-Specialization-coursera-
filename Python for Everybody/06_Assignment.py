text = "X-DSPAM-Confidence:    0.8475";

spacePos = text.find(" ")
number = text[spacePos:]
strippedNumber = number.lstrip();
result = float(strippedNumber)
print (result)

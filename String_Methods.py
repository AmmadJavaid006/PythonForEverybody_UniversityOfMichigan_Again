text = "X-DSPAM-Confidence:    0.8475"

exnum = float(text[text.find(":") + 1 : ].lstrip())

print(exnum)


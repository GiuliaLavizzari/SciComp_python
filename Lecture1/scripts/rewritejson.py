import json

with open('all_registers.json') as json_file:
    data = json.load(json_file)

print([str(i) for i in range(25)])

for adc in ["adc0", "adc1"]:
    for ch in [str(i) for i in range(25)]:
        data["0"][ch][adc] = data["0"][ch][adc][:-4]

json.dump(data, open("all_registers_new.json","w"), indent=4)


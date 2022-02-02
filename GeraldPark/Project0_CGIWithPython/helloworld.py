#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
print("content-type:text/html; charset=utf-8\n")
a = 3+4+5
b = a/3
print(b)

a = 'Hello Python'
print(a)
print(len(a))

## 문자의 치환

name = 'Gerald'
print("To {name}. The Battle of Panormus was fought {age:d} on Sicily in 250 BC during the First Punic War between a {name}\
 Roman army led by Lucius Caecilius Metellus and a Carthaginian force led by Hasdrubal. The Romans captured the major Sicilian city of Apple Panormus in 254 BC. Thereafter they avoided battle for fear of the Carthaginian war elephants. In 250 BC Hasdrubal led out his army to devastate the crops of Rome's allied cities. The Romans withdrew to Panormus and Hasdrubal pressed on to the city walls. Once he arrived, Metellus countered the elephants with a hail of javelins from earthworks dug near the walls. Infuriated by this missile fire, the elephants fled through the Carthaginian infantry. The Roman infantry then charged the Carthaginian left flank, which broke, along with the rest of the Carthaginians. \
The elephants were captured and later slaughtered in the Circus Maximus".format(name='GERALD',age=12))
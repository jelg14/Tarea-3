personajes = []
l = {'Nombre':'L','Edad':25,'Poder':'Genio'}
yagami = {'Nombre':'Yagami Ligth','Edad':27,'Poder':'Genio Malvado'}
misa = {'Nombre':'Misa','Edad':19,'Poder':'Hermosa'}
riuk = {'Nombre':'Riuk','Edad':1000,'Poder':'Dios de la muerte (Shinigami) '}
jojo= {'Nombre':'Jotaro Kujo', 'Edad':38, 'Poder':'Star platinium'}
porlnareff={'Nombre':'Jean Pierre Porlnareff', 'Edad':44, 'Poder': 'Silver Chariot'}

personajes.append(l)
personajes.append(yagami)
personajes.append(misa)
personajes.append(riuk)
personajes.append(jojo)
personajes.append(porlnareff)

for i in personajes:
    print ("#Nombre del personaje:'{nombre}' edad :'{edad}' Poderes o habilidades:'{poder}'.\n*************************************************************************************************"
.format(nombre = i['Nombre'],edad = i['Edad'] , poder=i['Poder']))

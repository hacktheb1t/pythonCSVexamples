import csv

def escrita_exemplo_1():
    f = open("tabela.csv",'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('Nome','Idade','Sexo'))
        writer.writerow(('Lucas','15','M'))
        writer.writerow(('Luana','16','F'))
        writer.writerow(('João','15','M'))
    finally:
        f.close()

    print(open('tabela.csv','rt').read())

def leitura_exemplo_1():
    f = open("tabela.csv",'r')
    try:
        leitor = csv.reader(f)
        for linha in leitor:
            print(linha)
    finally:
        f.close()

def adicionar_exemplo_1():
    f = open("tabela.csv",'a')
    try:
        writer = csv.writer(f)
        writer.writerow(('Luciana','19','F'))
        writer.writerow(('Felipe','13','M'))
    finally:
        f.close()

    print(open('tabela.csv','rt').read())



def leitura_exemplo_2():
    with open(‘some.csv’, ‘rb’) as f:
        reader = csv.reader(f)
        for row in reader:
            print row


import sys

def leitura_exemplo_3():
    f = open(sys.argv[1], ‘rb’)
    reader = csv.reader(f)
    for row in reader
        print row

    f.close()



def leitura_exemplo_4():
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

#Spam, Spam, Spam, Spam, Spam, Baked Beans
#Spam, Lovely Spam, Wonderful Spam

def escrita_exemplo_2():
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

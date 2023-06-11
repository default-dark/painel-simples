################
import requests
import json
import os
import time
import random
import phonenumbers
import time
import os
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
###############

def main():
    try:
        os.system("clear")
        r = "\033[1;31m"
        g = "\033[1;32m"
        h = "\033[1;33m"
        bl = "\033[1;34m"
        print(f"""{g}
    |-----------------------|
    |▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░ |
    |▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░ |
    |▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░ |
    |▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░ |
    |░░░░▄▄███▄▄░░░░░█████░ |
    ||-------||-------------|
    ||       ||
              """)
        time.sleep(1)
        print(f"""{r}
    ||       ||
    ||-------||-----------------------------------------|
    |░░░░░░░░░░┏━┓░░░░░░┏┓░░░░░────┏━┓┏┓░░░░┏━┓░░░░░░┏━┓|
    |┏━┓┏━┓┏━┳┓┃━┫┏┳┓┏┓░┃┗┓┏━┓░╔══╗┃━┫┣┫┏━━┓┃╋┃┏┓░┏━┓┃━┫|
    |┃━┫┃╋┃┃┃┃┃┣━┃┃┃┃┃┗┓┃┏┫┃╋┗┓╚══╝┣━┃┃┃┃┃┃┃┃┏┛┃┗┓┃┻┫┣━┃|
    |┗━┛┗━┛┗┻━┛┗━┛┗━┛┗━┛┗━┛┗━━┛────┗━┛┗┛┗┻┻┛┗┛░┗━┛┗━┛┗━┛|
    |    {r} criado: default                               |
    |---------------------------------------------------|
    |                               |         
    |                               |{g}     
     \                             /|
      /---------------------------/ |
     /  [99]sair                 /  |
    /---------------------------/   |
    |{h}[1]{g} IP-INFO                |   |
    |{h}[2]{g} CEP-INFO               |   |
    |{h}[3]{g} CNPJ-INFO              |   |
    |{h}[4]{g} DDD-INFO               |   |
    |{h}[5]{g} BANCO-INFO             |   |
    |{h}[6]{g} CORRETORA-INFO         |   |
    |{h}[7]{g} BIN-INFO               |   |
    |{h}[8]{g} PHONE-INFO             |   /
    |{h}[9]{g} GERADOR-CPF            |  / 
    |{h}[10]{g} COVID19-INFO          | /
    |___________________________|/
     """)
        zzz = int(input(f"{bl}[painel-de-consulta]{g}--> "))
        if zzz == 1:
            print(f"""{r}
        ╔╗───────╔╗────╔═╗───
        ╠╣╔═╗╔══╗╠╣╔═╦╗║═╣╔═╗
        ║║║╬║╚══╝║║║║║║║╔╝║╬║
        ╚╝║╔╝────╚╝╚╩═╝╚╝─╚═╝
        ──╚╝─────────────────""")
            print("digite um ip exemplo 8.8.8.8")
            ip = input(f">>> ")
            url = "https://ipwhois.app/json/" + ip
            file = requests.get(url).json()
            print(f"-"*60)
            print(f"{bl}ip: ",file["ip"])
            print(f"{bl}success: ",file["success"])
            print(f"{bl}type: ",file["type"])
            print(f"{bl}continet: ",file["continent"])
            print(f"{bl}continent code: ",file["country_code"])
            print(f"{bl}country_flag: ",file["country_flag"])
            print(f"{bl}contry capital: ",file["country_capital"])
            print(f"{bl}country_phone: ",file["country_phone"])
            print(f"{bl}country_neighbours: ",file["country_neighbours"])
            print(f"{bl}region: ",file["region"])
            print(f"{bl}city: ",file["city"])
            print(f"{bl}latitude: ",file["latitude"])
            print(f"{bl}longitude: ",file["longitude"])
            print(f"{bl}asn: ",file["asn"])
            print(f"{bl}org: ",file["org"])
            print(f"{bl}timezone: ",file["timezone"])
            print(f"{bl}timezone_name: ",file["timezone_name"])
            print(f"{bl}timezone_dstOffset: ",file["timezone_dstOffset"])
            print(f"{bl}currency: ",file["currency"])
            print(f"{bl}currency_code: ",file["currency_code"])
            print(f"{bl}currency_symbol: ",file["currency_symbol"])
            print(f"{bl}currency_rates: ",file["currency_rates"])
            print(f"{bl}currency_plural: ",file["currency_plural"])
            print(f"{r}-"*60)

            aperte = input(f"aperte para reniciar")
        elif zzz == 2:
            print(f"""{h}
        ─────────────╔╗────╔═╗───
        ╔═╗╔═╗╔═╗╔══╗╠╣╔═╦╗║═╣╔═╗
        ║═╣║╩╣║╬║╚══╝║║║║║║║╔╝║╬║
        ╚═╝╚═╝║╔╝────╚╝╚╩═╝╚╝─╚═╝
        ──────╚╝─────────────────""")
            print("consultar cep limpo sem (-/.)")
            cep = input(f"--> ")
            url = "https://viacep.com.br/ws/"+cep+"/json/"
            file = requests.get(url).json()

            print(f"-"*60)
            print(f"{r}cep: ",file["cep"])
            print(f"{r}logradouro: ",file["logradouro"])
            print(f"{r}complemento: ",file["complemento"])
            print(f"{r}localidade: ",file["localidade"])
            print(f"{r}uf: ",file["uf"])
            print(f"{r}ibge: ",file["ibge"])
            print(f"{r}ddd: ",file["ddd"])
            print(f"{r}siafi: ",file["siafi"])
            print(f"{h}-"*60)
            aperte = input(f"aperte para reniciar")
        elif zzz == 3:
            print(f"""{h}
        ──────────╔═╗──────╔╗──────────────────────
        ╔═╗╔═╗╔═╦╗║═╣╔╦╗╔╗─║╚╗╔═╗─╔══╗╔═╗╔═╦╗╔═╗─╔╗
        ║═╣║╬║║║║║╠═║║║║║╚╗║╔╣║╬╚╗╚══╝║═╣║║║║║╬║─╠╣
        ╚═╝╚═╝╚╩═╝╚═╝╚═╝╚═╝╚═╝╚══╝────╚═╝╚╩═╝║╔╝╔╝║
        ─────────────────────────────────────╚╝─╚═╝""")
            print("pesquisa com cnpj limpo sem (./-)")
            cnpj = input(f"---> ")
            url =  "https://brasilapi.com.br/api/cnpj/v1/"+cnpj
            file = requests.get(url).json()
            
            print(f"-"*60)
            print(f"{g}uf: ",file["uf"])
            print(f"{g}codigo_pais: ",file["codigo_pais"])
            print(f"{g}cep: ",file["cep"])
            print(f"{g}pais: ",file["pais"])
            print(f"{g}cnpj: ",file["cnpj"])
            print(f"{g}email: ",file["email"])
            print(f"{g}pais: ",file["pais"])
            print(f"{g}porte: ",file["porte"])
            print(f"{g}bairro: ",file["bairro"])
            print(f"{g}numero: ",file["numero"])
            print(f"{g}municipio: ",file["municipio"])
            print(f"{g}logradouro: ",file["logradouro"])
            print(f"{g}complemento: ",file["complemento"])
            print(f"{g}telefone1 ",file["ddd_telefone_1"])
            print(f"{g}telefone2: ",file["ddd_telefone_2"])
            print(f"{g}nome_fantasia: ",file["nome_fantasia"])
            print(f"{g}capital_social: ",file["capital_social"])
            print(f"{h}-"*60)

            aperte = input("aperte para reniciar")
        elif zzz == 4:
            print(f"""{h}
         █▀▀▄ █▀▀▄ █▀▀▄ ░░ █▀▀ █▀▀█ █▀▀▄ █▀▀ █░░█ █░░ ▀▀█▀▀ █▀▀█
         █░░█ █░░█ █░░█ ▀▀ █░░ █░░█ █░░█ ▀▀█ █░░█ █░░ ░░█░░ █▄▄█
         ▀▀▀░ ▀▀▀░ ▀▀▀░ ░░ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ░▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀""") 
            print("consultar ddd exemplo 55")
            ddd = input(f"---> ")
            url = "https://brasilapi.com.br/api/ddd/v1/" + ddd
            file = requests.get(url).json()

            print(f"{bl}state: ",file["state"])
            print(f"{bl}cities: ",file["cities"])

            aperte = input("aperte para reniciar")
        elif zzz == 5:
            print(f"""{h}
        ╔╗────╔═╗───────╔╗─────────╔╗─
        ╠╣╔═╦╗║═╣╔═╗╔══╗║╚╗╔═╗─╔═╦╗║╠╗
        ║║║║║║║╔╝║╬║╚══╝║╬║║╬╚╗║║║║║═╣
        ╚╝╚╩═╝╚╝─╚═╝────╚═╝╚══╝╚╩═╝╚╩╝
        ──────────────────────────────""")
            print(f"digite o codigo do bank exemplo 1")
            bank = input(f"---> ")

            print(f"-"*60)
            url = "https://brasilapi.com.br/api/banks/v1/" + bank
            file = requests.get(url).json()
            print("ispb: ",file["ispb"])
            print("name: ",file["name"])
            print("code: ",file["code"])
            print("fullname: ",file["fullName"])
            print(f"-"*60)

            aperte = input("aperte para reniciar")
        elif zzz == 6:
            print(f"""{h}
        ──────────╔═╗──────╔╗────────────────────────╔╗───────────
        ╔═╗╔═╗╔═╦╗║═╣╔╦╗╔╗─║╚╗╔═╗─╔══╗╔═╗╔═╗╔╦╗╔╦╗╔═╗║╚╗╔═╗╔╦╗╔═╗─
        ║═╣║╬║║║║║╠═║║║║║╚╗║╔╣║╬╚╗╚══╝║═╣║╬║║╔╝║╔╝║╩╣║╔╣║╬║║╔╝║╬╚╗
        ╚═╝╚═╝╚╩═╝╚═╝╚═╝╚═╝╚═╝╚══╝────╚═╝╚═╝╚╝─╚╝─╚═╝╚═╝╚═╝╚╝─╚══╝
        ──────────────────────────────────────────────────────────""")
            print("consulta com cnpj limpo sem .-/")
            corre = input(f"---> ")
            url = "https://brasilapi.com.br/api/cvm/corretoras/v1/" + corre
            file = requests.get(url).json()
            print(f"-"*60)
            print("bairro: ",file["bairro"])
            print("cep: ",file["cep"])
            print("cnpj: ",file["cnpj"])
            print("codigo_cvm: ",file["codigo_cvm"])
            print("complemento: ",file["complemento"])
            print("data_inicio_situacao: ",file["data_inicio_situacao"])
            print("data_patrimonio_liquido: ",file["data_patrimonio_liquido"])
            print("data_registro: ",file["data_registro"])
            print("email: ",file["email"])
            print("logradouro: ",file["logradouro"])
            print("municipio: ",file["municipio"])
            print("nome_social: ",file["nome_social"])
            print("nome_comercial: ",file["nome_comercial"])
            print("pais: ",file["pais"])
            print("status: ",file["status"])
            print("telefone: ",file["telefone"])
            print("type: ",file["type"])
            print("uf: ",file["uf"])
            print("valor_patrimonio_liquido: ",file["valor_patrimonio_liquido"])
            print(f"-"*60)

            aperte = input("aperte para reniciar")
        elif zzz == 7:
            print(f"""{h}
        ──────────╔═╗──────╔╗─────────╔╗─╔╗────
        ╔═╗╔═╗╔═╦╗║═╣╔╦╗╔╗─║╚╗╔═╗─╔══╗║╚╗╠╣╔═╦╗
        ║═╣║╬║║║║║╠═║║║║║╚╗║╔╣║╬╚╗╚══╝║╬║║║║║║║
        ╚═╝╚═╝╚╩═╝╚═╝╚═╝╚═╝╚═╝╚══╝────╚═╝╚╝╚╩═╝
        ───────────────────────────────────────""")
            print("consultar bin exemplo 40293436")
            binx = input(f"---> ")
            url = "https://binlist.io/lookup/" + binx
            file = requests.get(url).json()
            print(f"-"*60)
            print("sucesso: ",file["success"])
            print("numero: ",file["number"]["iin"])
            print("scheme: ",file["scheme"])
            print("type: ",file["type"])
            print("category: ",file["category"])
            print("país: ",file["country"]["name"]) 
            print(f"-"*60)

            aperte = input(f"aperte para reniciar")
        elif zzz == 8:
            print(f"""{bl}
    ──────────╔═╗──────╔╗────────────╔╗───────────
    ╔═╗╔═╗╔═╦╗║═╣╔╦╗╔╗─║╚╗╔═╗─╔══╗╔═╗║╚╗╔═╗╔═╦╗╔═╗
    ║═╣║╬║║║║║╠═║║║║║╚╗║╔╣║╬╚╗╚══╝║╬║║║║║╬║║║║║║╩╣
    ╚═╝╚═╝╚╩═╝╚═╝╚═╝╚═╝╚═╝╚══╝────║╔╝╚╩╝╚═╝╚╩═╝╚═╝
    ──────────────────────────────╚╝──────────────""")
            print("digite o numero limpo exemplo +551626762872")
            telef = input(f"---> ")
            print(f"-"*60)
            telef = phonenumbers.parse(telef, 'br', 'us')
            print('cidade: ',geocoder.description_for_valid_number(telef, 'br', 'us'))
            print('pais: ',geocoder.country_name_for_number(telef, 'br', 'us'))
            print('operadora: ',carrier.name_for_number(telef, 'br', 'us'))
            print('numero: ',phonenumbers.format_number(
            telef, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
            valid = phonenumbers.is_valid_number(telef)
            modelo = phonenumbers.number_type(telef)
            print('timezone: ',timezone.time_zones_for_number(telef))

            print('telefone-valido-ou-falso==> ',valid)


            print(telef)

            if modelo == phonenumbers.PhoneNumberType.MOBILE:
                print('modelo: ','Este é um número de celular')
            elif modelo == phonenumbers.PhoneNumberType.FIXED_LINE:
                print('modelo: ','Este é outro tipo de número')
            else:
                print('modelo: ','Este é outro tipo de número')
            print(f"-"*60)

            aperte = input("aperte para reniciar")
        elif zzz == 9:
            print(f"""{bl} 
        ──────────────╔╗────────────────╔═╗
        ╔═╗╔═╗╔╦╗╔═╗─╔╝║╔═╗╔╦╗╔══╗╔═╗╔═╗║═╣
        ║╬║║╩╣║╔╝║╬╚╗║╬║║╬║║╔╝╚══╝║═╣║╬║║╔╝
        ╠╗║╚═╝╚╝─╚══╝╚═╝╚═╝╚╝─────╚═╝║╔╝╚╝─
        ╚═╝──────────────────────────╚╝────
        {r} 01 {bl} gerador-de-cpf-simples
        {r} 02 {bl} gerador-de-cpf-quatidade
              """)
            cpf = int(input(f"{bl}cpf-gerador]{g}•••{r}> "))

            if cpf == 1:
                cpf = ''.join(map(str, [random.randint(0, 9) for i in range(0, 11)]))
                print(cpf)

                aperte = input("aperte para reniciar")
            elif cpf == 2:
                print(f"{r}digite a quantidade que deseja gerar")
                geradorX = int(input(f"{g}cpf{r}••••>>>"))

                for x in range(geradorX):
                    time.sleep(1)
                    cpf = ''.join(map(str, [random.randint(0 ,9) for i in range(0, 11)]))
                    print(cpf)

                else:
                    aperte = input(f"aperte para reniciar")
        elif zzz == 10:
            print(f"""{r}
            ░░░░░░░░░░░┏┓░┏┓────┏┓░░░░┏━┓░░░
            ┏━┓┏━┓┏━┳━┓┣┫┏┛┃╔══╗┣┫┏━┳┓┃━┫┏━┓
            ┃━┫┃╋┃┗┓┃┏┛┃┃┃╋┃╚══╝┃┃┃┃┃┃┃┏┛┃╋┃
            ┗━┛┗━┛░┗━┛░┗┛┗━┛────┗┛┗┻━┛┗┛░┗━┛
            exemplo de consulta da covid digite sp 
            para ver numero de morte dá covid
              """)
            covid = input(f"----> ")
            url = "https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/" + covid 
            file = requests.get(url).json()
            print(f"-"*60)
            print("uid: ",file["uid"])
            print("uf: ",file["uf"])
            print("state: ",file["state"])
            print("cases: ",file["cases"])
            print("deaths: ",file["deaths"])
            print("suspects: ",file["suspects"])
            print("refuses: ",file["refuses"])
            print("datetime: ",file["datetime"])
            print(f'-'*60)
            aperte = input(f"aperte para reniciar")
        elif zzz == 11:
            print(f"""{bl} 
         █▀▀ █▀▀█ █▀▀▄ █▀▀ █░░█ █░░ ▀▀█▀▀ █▀▀█ ░░ █▀▀ ░▀░ █▀▀█ █▀▀
         █░░ █░░█ █░░█ ▀▀█ █░░█ █░░ ░░█░░ █▄▄█ ▀▀ █▀▀ ▀█▀ █░░█ █▀▀
         ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ░▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ ░░ ▀░░ ▀▀▀ █▀▀▀ ▀▀▀
         exemplo de cunsulta fipe 001004-9
              """)
            carro = input(str(f"---> "))
            url = "https://brasilapi.com.br/api/fipe/preco/v1/" + carro 
            print(f"-"*60)
            print("valor: ",file["valor"])
            print("marca: ",file["marca"])
            print("modelo: ",file["modelo"])
            print("anomodelo: ",file["anoModelo"])
            print("combustivel: ",file["combustivel"])
            print("codigofipe: ",file["codigoFipe"])
            print("mesReferencia: ",file["mesReferencia"])
            print("tipoveiculo: ",file["tipoVeiculo"])
            print("siglaCombustivel: ",file["siglaCombustivel"])
            print("dataConsulta: ",file["dataConsulta"])
            print(f'-'*60)

            aperte = input(f"aperte para reniciar")
        elif zzz == 99:
            os.system("clear")
            print("saindo...")
            time.sleep(3)
            os.system("clear")
            exit()

    except KeyboardInterrupt:
        print("você apertou CTRL-C portanto você saiu...")
        time.sleep(2)
        exit()
        os.system("clear")

while True:
    main()



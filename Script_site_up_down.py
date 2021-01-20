from selenium import webdriver
import time

options = webdriver.ChromeOptions()

#Heaadless faz com que a operação não apareça na tela do usuário!
options.headless = True
options.add_argument('--log-level=3')
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--allow-insecure-localhost")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')

#Especifique o caminho do seu webdriver!
driver = webdriver.Chrome(executable_path=r"ESPECIFIQUE O CAMINHO DO SEU WEBDRIVER AQUI", options=options)

#Site de teste (sinta-se a vontade de alterar pelo de sua preferência!)
driver.get("https://www.isitdownrightnow.com")

website = input("Digite o website que você quer testar: ")
print("Checando...")

try:
    check = driver.find_element_by_id("search").clear()
    time.sleep(2)
    write = driver.find_element_by_id("search").send_keys(website)
    time.sleep(2)
    enter = driver.find_element_by_id("submit").click()
    
    time.sleep(2)
    
    server = driver.find_element_by_class_name("statusup")
    valor = server.text
    
#Quando o site está funcionando, o site de testes retorna um texto contendo a expressão "UP", portanto o if checa se o valor da classe de retorno possui essa expressão!
    if "UP" in valor:
        print(website + " ESTÁ funcionando corretamente!")
    else:
        print(website + " NÃO ESTÁ funcionando corretamente!")
except:
    print("Erro! tente novamente!")

#O programa é fechado após mostrar o resultado ao usuário! (tempo de execução no teste: 8s)
driver.close()








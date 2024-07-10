from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador Chrome con Selenium
driver = webdriver.Chrome()

# Abrir WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Escanea el código QR y presiona Enter")
input("Presiona Enter después de escanear el código QR...")

# Nombre del contacto al que se enviará el mensaje
nombre_contacto = "Guiri"  # Reemplaza con el nombre de tu contacto

# Mensaje a enviar
mensaje = "¡folla buros y guiri "

try:
    # Esperar unos segundos para que cargue completamente WhatsApp Web
    time.sleep(15)

    # Buscar el campo de búsqueda y escribir el nombre del contacto
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.clear()
    search_box.send_keys(nombre_contacto)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)

    # Esperar a que se abra la conversación
    time.sleep(5)

    # Encontrar el campo de mensaje y enviar el mensaje repetidamente sin pausas
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    for i in range(1000):
        message_box.send_keys(mensaje)
        message_box.send_keys(Keys.ENTER)
        print(f"Mensaje {i + 1} enviado a {nombre_contacto}")

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    # Cerrar el navegador al finalizar
    driver.quit()

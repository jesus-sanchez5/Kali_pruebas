from selenium import webdriver

# Crear una instancia de Microsoft Edge
driver = webdriver.Edge()

# Abrir el sitio web de Google
driver.get("https://www.google.com/")

# Encontrar el elemento de búsqueda de Google y escribir una consulta
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium with Microsoft Edge")

# Enviar la búsqueda
search_box.submit()

# Cerrar el navegador
driver.quit()

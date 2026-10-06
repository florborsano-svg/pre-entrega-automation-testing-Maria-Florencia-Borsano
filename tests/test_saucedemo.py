from utils.helpers import login_helper
from selenium.webdriver.common.by import By 




#separar el login en carpeta helpers.py de utils

def test_01_login(driver):
    login_helper(driver)  
    assert "/inventory.html" in driver.current_url,"Error: no se redirigió a inventory.html"

def test_02_verificar_inventario(driver):
    section_title = driver.find_element(By.CLASS_NAME,"title").text
    assert section_title == "Products", f"Titulo de ventana esperado 'Productos', Obtenido {section_title}"

def test_03_productos_visibles(driver):
    inventory_item = driver.find_elements(By.CLASS_NAME,"inventory_item") #find_elements en plural porque es una lista/html collection
    # con len puedo ver que tan larga es la lista
    assert len(inventory_item) > 0, f"Error: No se encontraron productos visibles"

def test_04_lista_nombre_precio_primer_producto(driver):
     primer_producto = driver.find_elements(By.CLASS_NAME,"inventory_item")[0]
     nombre = primer_producto.find_element(By.CLASS_NAME,"inventory_item_name").text
     precio = primer_producto.find_element(By.CLASS_NAME,"inventory_item_price").text

     assert nombre == "Sauce Labs Backpack",f"Error: se esperaba el nombre del primer producto 'Sauce Labs Backpack' , se obtuvo {nombre}"
     assert precio == "$29.99",f"Error: se esperaba el precio del primer producto '$29.99' , se obtuvo {precio}"
     

def test_05_valid_interface(driver):    
    menu_button = driver.find_element(By.ID,"react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME,"product_sort_container")   

    assert menu_button.is_displayed(),f"El Menu no esta visible"
    assert filtro.is_displayed(),f"El Filtro no esta visible"


def test_06_anadir_producto_al_carrito(driver): 
    # 1. Buscamos el primer producto
    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0] 
    
    # 2. Buscamos y clickeamos el botón de agregar del primer producto
    boton_agregar = first_item.find_element(By.TAG_NAME, "button") 
    boton_agregar.click() 
    
    # 3. VOLVEMOS A BUSCAR el botón dentro del mismo contenedor para refrescar la referencia porque el boton cambia de estado
    boton_remover = first_item.find_element(By.TAG_NAME, "button")
    
    # 4. Hacemos el assert con el nuevo elemento
    assert boton_remover.text.capitalize() == "Remove", "Error: el botón no cambió a REMOVE"

def test_07_verificar_contador_carrito(driver):
    contador_carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
    assert contador_carrito == "1", f"Error: se esperaba 1, se obtuvo {contador_carrito}"

def test_08_navegar_carrito(driver):
    carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
    carrito.click()
    assert "/cart.html" in driver.current_url,"Error: no se redirigió a cart.html"

def test_09_comprobar_producto_en_carrito(driver):
    carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
    carrito.click()
    producto = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert producto == "Sauce Labs Backpack", "Error: No es el titulo del producto agregado"

# Al final: generar reportes html en carpeta de reportes  "pytest -v --html=reportes/reporte.html"
# subir a repositorio con nombre = "pre-entrega-automation-testing[Maria Florencia Borsano]"




    

    
    



    
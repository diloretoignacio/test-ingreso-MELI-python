#ENDPOINTS UTILIZADAS
#https://api.mercadolibre.com/sites/SITE/search?seller_id=SELLER_ID Se obtiene lo publicado por un determinado seller
#https://api.mercadolibre.com/categories/CATEGORY_ID Se obtiene informacion de una categoria especifica

#Se importa la liberia request para realizar peticiones HTTPS
import requests
sellers = [179571326]

#Se recorre el listado de sellers
for seller in sellers:
    #Se obtienen los items publicados en MLA por el seller
    datos = requests.get('https://api.mercadolibre.com/sites/MLA/search?seller_id='+str(seller)).json()
    items = datos['results']

    print("---- Items del seller "+str(seller)+" ----")
    #Se recorre el listado de items, extrayendo de cada uno el ID, title, ID category, name category
    for item in items:
        id_item = item['id']
        title = item['title'] 
        category_id = item['category_id'] 
        
        print("ID item = "+id_item)
        print("Title = "+title)
        print("ID category = "+category_id)

        #Se obtiene una categoria espefica para saber su nombre
        category = requests.get('https://api.mercadolibre.com/categories/'+category_id).json() 
        name_category = category['name']
        
        print("Name category = "+name_category)
        print("\n")
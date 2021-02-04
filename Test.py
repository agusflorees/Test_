import requests 
import json
seller_ID = '179571326'

items = requests.get('https://api.mercadolibre.com/users/'+seller_ID+'/items/search') 
items_json = items.json() #Formatea el resultado de la consulta a la api a formato JSON


items_ID= items_json['results']
log = open ('/archivo.log', 'w' )
for i in items_ID.count():
    log.write (items_ID[i]+ "del item,")
    cat_id = requests.get('https://api.mercadolibre.com/items/'+ items_ID[i])
    cat_idjson = cat_id.json()
    log.write (cat_idjson['tittle']+ "del item")
    log.write ( cat_idjson['category_id'] + "donde esta publicado")
    name= requests.get ('https://api.mercadolibre.com/categories/'+ cat_idjson['category_id'])
    name_json= name.json()
    log.write(name_json['name'] + "de la categoria \n"  )

log.close()



# Precios Claros Scraper

[Precios Claros](https://www.preciosclaros.gob.ar/) is a website run by the Ministry of Production in Argentina that publishes prices of products sold by major supermarket chain nationwide. The website is updated daily, so this scraper written in Python allows to persist its data.

Just run `python scraper.py` in the terminal once in the project's directory and scraped data will be stores in a folder named *data* within the project's directory, under a sub-folder named after the current scraping date. Data from each store gets saved in pickle format with the store's id as filename.

***
### Sample output

```{json}
[
    {
      "marca": "NIVEA",
      "id": "0000042300083",
      "precioMax": 228.8,
      "precioMin": 228.8,
      "nombre": "Crema Facial Cuidado Nivea 100 Ml",
      "presentacion": "100.0 ml",
      "cantSucursalesDisponible": 1
    },
    {
      "marca": "REXONA",
      "id": "0000075024956",
      "precioMax": 182.9,
      "precioMin": 182.9,
      "nombre": "Desodorante Antitranspirante en Barra Men V8 Rexona 50 Gr",
      "presentacion": "50.0 gr",
      "cantSucursalesDisponible": 1
    },
	...
]
```
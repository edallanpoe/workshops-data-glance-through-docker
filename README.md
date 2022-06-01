# workshops-data-glance-through-docker
Offer a first approach to the data world by using technologies that have a huge impact in the industry. Docker and PySpark.

This also contains an example of a data pipeline which transforms a GPS trace

## Prerequisites
For more information please refer to the links below:
proj - *https://proj.org/install.html*
gdal - *https://medium.com/@egiron/how-to-install-gdal-and-qgis-on-macos-catalina-ca690dca4f91*

### geopandas - MAC OSX
Using brew install:
```bash
brew install proj  
brew install GDAL 
```

Using pip install:
```bash
python -m pip install --upgrade pip wheel
pip install Fiona gdal
pip install pyproj --no-binary pyproj
```

Now, you can install the librarry ``geopandas`` using ``poetry``.

### geopandas - Linux/Debian-based
Using using the package manager install:
```bash
apt update 
apt install -y openjdk-11-jdk openjdk-11-jre ca-certificates-java proj-bin libgdal-dev 
```

Using pip install:
```bash
python -m pip install --upgrade pip wheel
pip install Fiona gdal
pip install pyproj --no-binary pyproj
```

Now, you can install the librarry ``geopandas`` using ``poetry``.


## LUISVASV
los archivos deben de tener la estructura interna de

instalar ubuntu

instalar en imagen
apt-get install wkhtmltopdf

fuente letras grandes
https://patorjk.com/software/taag/#p=display&f=Big&t=STEP%20%23%200


```xml
<trkpt lat="6.297475984325909" lon="-75.5781921186257">
				<ele>1668.879306793213</ele>
				<time>2022-03-01T20:33:48Z</time>
</trkpt>
```



el nombre de los archivos 
```bash 
recovery.<date_your_format>.gpx
# ecample 
05-Mar-2022.1025
```


estructura de carpetas 
```bash 

data/vehicles
├── vehicle type
    └── id
        └── recovery.<date_your_format>.gpx.gpx
        └── recovery.<date_your_format>.gpx.gpx

# example
data/vehicles
├── car
│   └── BBB999
│       └── recovery.01-Mar-2022-1533.gpx
└── motorcycle
    ├── AAA_11B
    │   └── recovery.05-Mar-2022.1025.gpx
    └── AAA_22B
        └── recovery.05-Mar-2022.1025.gpx
```



PARA ELIMINAR



```bash 
spark-submit --master local[4] --name demo \
   components/spark/spark-job.py \
  /home/luis.vasquez/repositories/luisvasv/public/demos/ruta.n.intro.spark/data/output/files \
  /home/luis.vasquez/repositories/luisvasv/public/demos/ruta.n.intro.spark/data/output/results \
  /home/luis.vasquez/repositories/luisvasv/public/demos/ruta.n.intro.spark/data/parametric/gasoline.json




python components/python/app.py generate-report \
    --images-path  /home/luis.vasquez/repositories/luisvasv/public/demos/ruta.n.intro.spark/data/output/images \
    --consolidated-file /home/luis.vasquez/repositories/luisvasv/public/demos/ruta.n.intro.spark/data/output/results/parquet/consolidated/*.parquet

```


TAREASgit@gitlab.com:luisvasv/public.git

DOCUMENTAR FUNCIONES RESTANTES DE PYTHON
ADAPTAR IMAGEN DE DOCKER
CREAR REDME BIEN BONITO
    https://hackmd.io/

DIAPOSITIVAS DIAGRAMAS DE ARQUITECTURA

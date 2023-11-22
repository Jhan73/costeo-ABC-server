# crear un entorno virtual de pyton
```py -m venv <nombre_de_entorno>```

# activar un entorno virtual
```<nombre_de_entorno>/Scripts/activate```

# Para instalar librerias del archivo requirements.txt
```pip install -r requirements.txt```

# Para instalar librerias del archivo requirements.txt
```pip install -r requirements.txt --upgrade --no-cache-dir```
Al ejecutar este comando, pip examinará el entorno actual del usuario y solo instalará las bibliotecas que no están presentes o que están en versiones más antiguas que las especificadas en tu archivo requirements.txt. Esto facilita la sincronización de entornos entre miembros del equipo.
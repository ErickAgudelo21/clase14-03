# clase14-03

Aplicación FastAPI con calculadora y registro de vehículos.

## Instalación

1. Crear entorno virtual:
   ```
   python3 -m venv venv
   ```

2. Activar entorno virtual:
   ```
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

```
python main.py
```

La aplicación estará disponible en http://localhost:8000

## Endpoints

- GET / : Mensaje de bienvenida
- GET /items/{item_id} : Retorna item_id y query
- GET /suma/{a}/{b} : Suma dos números
- GET /multiplicacion/{a}/{b} : Multiplica dos números
- POST /registrar_vehiculo/ : Registra un vehículo (parámetros: marca, modelo, anio, tipo)
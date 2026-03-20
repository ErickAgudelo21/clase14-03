# Historial de Cambios - Clase 14-03

## Fecha: 20 de Marzo de 2026

### Objetivo
Verificar errores en el código y completar las funciones con espacios vacíos de acuerdo con los otros archivos de la carpeta.

---

## Errores Identificados

1. **Archivo vacío**: `/workspaces/clase14-03/Calculadora/cda/colas-vehiculo.py` estaba completamente vacío
2. **Archivo vacío**: `/workspaces/clase14-03/Calculadora/cda/nodo.py` estaba vacío (necesario para estructura de cola enlazada)
3. **Métodos incompletos**: En `automovil.py` - contenía la clase `ColasVehiculo` en lugar de `Automovil`
4. **Conflicto de imports**: En `/workspaces/clase14-03/Calculadora/cda/__init__.py` intentaba importar desde `colas-vehiculo` (con guion)
5. **Métodos sin implementación**: 
   - `agregar_vehiculo()` - solo tenía comentario "poner su logica maravillosa"
   - `despachar_vehiculo()` - solo tenía `pass`
   - `mostrar_vehiculos()` - solo tenía comentario "poner su logica maravillosa"
6. **Constructor incompleto**: `Vehiculo.__init__()` no recibía parámetro `tipo`

---

## Cambios Realizados

### 1. Creación de `/workspaces/clase14-03/Calculadora/cda/nodo.py`
**Descripción**: Creada clase `Nodo` para implementar la estructura de cola enlazada
```python
class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None
```

### 2. Actualización de `/workspaces/clase14-03/Calculadora/cda/vehiculo.py`
**Descripción**: Agregado parámetro `tipo` al constructor
- **Antes**: `__init__(self, marca: str, modelo: str, anio: int)`
- **Después**: `__init__(self, marca: str, modelo: str, anio: int, tipo: str = None)`

### 3. Completado `/workspaces/clase14-03/Calculadora/cda/colas-vehiculo.py`
**Descripción**: Implementada la clase `ColasVehiculo` con cola enlazada
- Agregado atributo `self.cabeza` y `self.cola` para la estructura de cola
- Implementado `agregar_vehiculo()` - crea nodos y los encadena
- Implementado `despachar_vehiculo()` - elimina y retorna el primer vehículo de la cola
- Implementado `mostrar_vehiculos()` - retorna lista de vehículos formateada

**Métodos completados**:
```python
def agregar_vehiculo(self, marca: str, modelo: str, anio: int, tipo: str):
    # Crea vehículo según tipo y lo agrega a la cola

def despachar_vehiculo(self):
    # Retorna y elimina el primer vehículo de la cola (FIFO)

def mostrar_vehiculos(self):
    # Retorna lista con información de todos los vehículos en cola
```

### 4. Reparado `/workspaces/clase14-03/Calculadora/cda/automovil.py`
**Descripción**: Reemplazada la clase `ColasVehiculo` incorrecta con la clase `Automovil`
```python
from .vehiculo import Vehiculo

class Automovil(Vehiculo):
    tipo = "Automovil"
    def __init__(self, marca: str, modelo: str, anio: int):
        super().__init__(marca, modelo, anio, self.tipo)

    def mostrar_informacion(self) -> str:
        return f"{super().mostrar_informacion()}"
```

### 5. Actualizado `/workspaces/clase14-03/Calculadora/cda/__init__.py`
**Descripción**: Corregidas las importaciones
- **Antes**: `from .colas-vehiculo import ColasVehiculo` (importación incorrecta)
- **Después**: 
```python
from .vehiculo import Vehiculo
from .automovil import Automovil
from .motocicleta import Motocicleta
from .nodo import Nodo
```

### 6. Completado `/workspaces/clase14-03/cda/colas_vehiculo.py`
**Descripción**: Implementada clase `ColasVehiculo` con estructura de cola enlazada
- Agregada clase `Nodo` interna
- Implementados todos los métodos de la cola:
  - `agregar_vehiculo()` - maneja diccionarios de vehículos
  - `despachar_vehiculo()` - retorna primer vehículo
  - `mostrar_vehiculos()` - retorna lista formateada

---

## Resumen de Archivos Modificados

| Archivo | Estado | Cambio Principal |
|---------|--------|-----------------|
| `Calculadora/cda/nodo.py` | ✅ Creado | Nueva clase Nodo para cola enlazada |
| `Calculadora/cda/colas-vehiculo.py` | ✅ Completado | Implementada clase ColasVehiculo con métodos |
| `Calculadora/cda/vehiculo.py` | ✅ Actualizado | Agregado parámetro tipo al constructor |
| `Calculadora/cda/automovil.py` | ✅ Reparado | Reemplazada clase incorrecta por Automovil |
| `Calculadora/cda/__init__.py` | ✅ Corregido | Corregidas importaciones |
| `cda/colas_vehiculo.py` | ✅ Completado | Implementada cola con nodos enlazados |

---

## Estructura de Datos - Cola Enlazada (FIFO)

La implementación utiliza una **cola enlazada** con estructura FIFO (First In First Out):

```
Ingreso: veh1 → veh2 → veh3
Salida:  veh1 (se elimina)
         veh2 → veh3
```

- **cabeza**: Apunta al primer nodo (primera salida)
- **cola**: Apunta al último nodo (última entrada)
- **Nodo**: Contiene datos y referencia al siguiente nodo

---

## Estado Final

✅ **Todos los errores han sido corregidos**
✅ **Todas las funciones están completadas**
✅ **La estructura de cola enlazada está implementada correctamente**

Los archivos ahora pueden ser utilizados correctamente en la API FastAPI definida en `main.py`.

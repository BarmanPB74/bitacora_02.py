# bitacora_02.py · archivo histórico

Aquí empezó el **Libro de Guardia**: la idea de una aplicación que recopila
informes para explorar bucles, listas y tuplas.

Esa idea ya está construida y funcionando dentro de BAR BOX:

### → https://github.com/BarmanPB74/Bar_box

El Libro de Guardia vive ahora en `/libro`, con los seis campos originales
(título, fecha, hora, proyecto, tipo, contenido), guardado en SQLite y con
importación validada de tu `bitacora.json` anterior: no se pierde nada de lo que
ya habías escrito, y una reimportación idéntica no duplica reportes.

## De dónde salió cada idea

| Idea de este repositorio | Dónde está hoy |
|---|---|
| Recopilar informes con campos fijos | `domain.validar_reporte()` y la tabla `reports` |
| Guardar en un archivo JSON | `/importar`: lee tu JSON viejo y lo pasa a la base |
| Listas y diccionarios en memoria | SQLite, que sobrevive a cerrar la aplicación |

Este repositorio queda como registro del punto de partida. El desarrollo
continúa en el repositorio principal, rama
`claude/bar-box-bitacora-mesas-k1s9nj`.

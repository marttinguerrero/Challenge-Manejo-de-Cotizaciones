import pygraphviz as pgv

# Crear el gráfico
grafico = pgv.AGraph(directed=True)

# Nodos principales
grafico.add_node("Cliente", shape="box", color="blue", fontsize=12)
grafico.add_node("Servidor", shape="box", color="red", fontsize=12)

# Flujo HTTP/1.0
grafico.add_node("HTTP/1.0", shape="ellipse", color="black", fontsize=14, style="dashed")
grafico.add_edge("Cliente", "HTTP/1.0", label="Solicitud 1", fontsize=10)
grafico.add_edge("HTTP/1.0", "Servidor", label="Respuesta 1", fontsize=10)
grafico.add_edge("Cliente", "HTTP/1.0", label="Solicitud 2", fontsize=10)
grafico.add_edge("HTTP/1.0", "Servidor", label="Respuesta 2", fontsize=10)
grafico.add_edge("Cliente", "HTTP/1.0", label="Solicitud 3", fontsize=10)
grafico.add_edge("HTTP/1.0", "Servidor", label="Respuesta 3", fontsize=10)
grafico.add_edge("HTTP/1.0", "Cliente", label="Cerrar conexión después de cada respuesta", fontsize=9, style="dotted")

# Flujo HTTP/1.1
grafico.add_node("HTTP/1.1", shape="ellipse", color="black", fontsize=14, style="dashed")
grafico.add_edge("Cliente", "HTTP/1.1", label="Solicitud 1", fontsize=10)
grafico.add_edge("Cliente", "HTTP/1.1", label="Solicitud 2", fontsize=10)
grafico.add_edge("Cliente", "HTTP/1.1", label="Solicitud 3", fontsize=10)
grafico.add_edge("HTTP/1.1", "Servidor", label="Respuestas 1, 2, 3 (simultáneamente)", fontsize=10)
grafico.add_edge("HTTP/1.1", "Cliente", label="Conexión persistente abierta", fontsize=9, style="dotted")

# Conexión entre los protocolos
grafico.add_edge("HTTP/1.0", "HTTP/1.1", label="Evolución para soportar persistencia y paralelismo", fontsize=11, style="bold")

# Opciones visuales
grafico.graph_attr['label'] = "Comparación entre HTTP/1.0 y HTTP/1.1"
grafico.graph_attr['fontsize'] = 14
grafico.graph_attr['rankdir'] = "LR"  # Orientación de izquierda a derecha

# Guardar y mostrar el gráfico
archivo_salida = "comparacion_protocolos_http.png"
grafico.draw(archivo_salida, prog="dot", format="png")

print(f"Diagrama guardado en {archivo_salida}")

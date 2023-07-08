import config 
app = config.app

from authentication.api_v1_0.routes import auth_routes
from songs.api_v1_0.routes import songs_routes

app.register_blueprint(auth_routes)
app.register_blueprint(songs_routes)

@app.route('/')
def index():
    return "¡Hola, mundo!"

# Comprobar si el archivo se está ejecutando directamente y no importado como un módulo
if __name__ == "__main__":
    # Ejecutar la aplicación Flask
    app.run(host='0.0.0.0', port=5173)
    
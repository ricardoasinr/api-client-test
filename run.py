import socket
import uvicorn


def find_available_port(start_port=8000, max_attempts=100):
    """Encuentra un puerto disponible empezando desde start_port"""
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    raise RuntimeError(f"No se encontró un puerto disponible entre {start_port} y {start_port + max_attempts}")


if __name__ == "__main__":
    port = find_available_port(8000)
    print(f"🚀 Iniciando servidor en el puerto {port}")
    print(f"📝 Documentación disponible en: http://localhost:{port}/docs")
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

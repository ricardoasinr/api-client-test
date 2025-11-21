# 🔧 Troubleshooting - Vercel Error 500

## Pasos para Diagnosticar el Problema

### 1. **Revisar los Logs de Vercel**
   - Ve al dashboard de Vercel
   - Selecciona tu proyecto
   - Ve a la pestaña **"Logs"** o **"Functions"**
   - Busca errores específicos en los logs
   - Los logs te dirán exactamente qué está fallando

### 2. **Verificar las Dependencias**
   Asegúrate de que `requirements.txt` tenga todas las dependencias:
   ```
   fastapi==0.109.0
   uvicorn[standard]==0.27.0
   mangum==0.18.0
   ```

### 3. **Verificar la Configuración de Vercel**
   En el dashboard de Vercel, verifica:
   - **Runtime**: Debe ser Python 3.9 o superior
   - **Build Command**: Debe estar vacío (None)
   - **Output Directory**: Debe estar vacío (N/A)
   - **Install Command**: `pip install -r requirements.txt`

### 4. **Probar Localmente**
   Para verificar que el handler funciona:
   ```bash
   python -c "from main import handler; print('Handler OK')"
   ```

### 5. **Errores Comunes**

   **Error: "No module named 'mangum'"**
   - Verifica que `mangum` esté en `requirements.txt`
   - Asegúrate de que el despliegue instale las dependencias

   **Error: "Handler not found"**
   - Verifica que `main.py` tenga `handler = Mangum(app)`
   - Verifica que `vercel.json` apunte a `main.py`

   **Error: "Import error"**
   - Verifica que todas las importaciones estén correctas
   - Revisa que no haya dependencias faltantes

### 6. **Verificar el Archivo vercel.json**
   Debe verse así:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "main.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "main.py"
       }
     ]
   }
   ```

## Solución Alternativa: Sin vercel.json

Si el problema persiste, puedes intentar **eliminar `vercel.json`** y dejar que Vercel detecte automáticamente FastAPI. Para esto:

1. Elimina `vercel.json`
2. Asegúrate de que `main.py` tenga `handler = Mangum(app)`
3. En Vercel, selecciona **"Other"** como Framework Preset
4. Deja que Vercel detecte automáticamente Python

## Si Nada Funciona

1. **Crea un proyecto mínimo** para probar:
   ```python
   # main.py
   from fastapi import FastAPI
   from mangum import Mangum
   
   app = FastAPI()
   
   @app.get("/")
   def read_root():
       return {"Hello": "World"}
   
   handler = Mangum(app)
   ```

2. Si esto funciona, agrega gradualmente tu código
3. Si esto no funciona, el problema puede ser con la configuración de Vercel o con Mangum

## Contactar Soporte

Si nada funciona:
- Revisa los logs detallados en Vercel
- Busca en [GitHub Issues de Vercel](https://github.com/vercel/vercel/issues)
- Revisa la [documentación oficial de Vercel para Python](https://vercel.com/docs/functions/serverless-functions/runtimes/python)


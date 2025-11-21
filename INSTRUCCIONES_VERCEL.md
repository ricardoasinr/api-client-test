# 🚀 Instrucciones para Desplegar en Vercel

## Paso a Paso desde la Web de Vercel

### 1. **Preparar tu Repositorio Git**
   - Asegúrate de que todos tus cambios estén commitados:
     ```bash
     git add .
     git commit -m "Preparar para despliegue en Vercel"
     git push
     ```

### 2. **Acceder a Vercel**
   - Ve a [vercel.com](https://vercel.com)
   - Inicia sesión con tu cuenta (GitHub, GitLab, o Bitbucket)

### 3. **Importar Proyecto**
   - Haz clic en el botón **"Add New..."** → **"Project"**
   - Si es tu primera vez, haz clic en **"Import Project"**
   - Conecta tu repositorio de Git (GitHub/GitLab/Bitbucket)
   - Busca y selecciona el repositorio `api-test`

### 4. **Configurar el Proyecto**
   Vercel detectará automáticamente que es un proyecto FastAPI:
   
   - **Framework Preset**: Debería detectar "FastAPI" automáticamente
   - **Root Directory**: Deja `./` (raíz del proyecto)
   - **Build Command**: Déjalo vacío (None) - No se necesita para FastAPI
   - **Output Directory**: Déjalo vacío (N/A) - No se necesita para FastAPI
   - **Install Command**: `pip install -r requirements.txt` ✅ (Este ya debería estar configurado)

### 5. **Variables de Entorno (Opcional)**
   - Si necesitas variables de entorno, agrégalas en esta sección
   - Por ahora no necesitas ninguna

### 6. **Desplegar**
   - Haz clic en el botón **"Deploy"**
   - Espera a que termine el despliegue (toma 1-3 minutos)

### 7. **Probar tu API**
   Una vez desplegado, Vercel te dará una URL como:
   ```
   https://tu-proyecto.vercel.app
   ```
   
   Puedes probar los endpoints:
   - `GET https://tu-proyecto.vercel.app/` - Endpoint raíz
   - `GET https://tu-proyecto.vercel.app/health` - Health check
   - `GET https://tu-proyecto.vercel.app/docs` - Documentación Swagger
   - `POST https://tu-proyecto.vercel.app/events` - Crear evento
   - `GET https://tu-proyecto.vercel.app/events` - Listar eventos

## 📝 Archivos de Configuración Creados

- `vercel.json`: Configuración de Vercel para FastAPI
- `.vercelignore`: Archivos a ignorar en el despliegue
- `main.py`: Actualizado con el handler para Vercel

## ⚠️ Notas Importantes

1. **Almacenamiento en Memoria**: Los eventos se almacenan en memoria, por lo que se perderán cuando la función serverless se "despierte" o se reinicie.

2. **Despliegues Futuros**: Cada vez que hagas `git push` a tu rama principal, Vercel desplegará automáticamente los cambios (si habilitaste auto-deploy).

3. **Logs**: Puedes ver los logs de tu aplicación en el dashboard de Vercel.

## 🔧 Solución de Problemas

- Si el despliegue falla, revisa los logs en el dashboard de Vercel
- Asegúrate de que `requirements.txt` tenga todas las dependencias necesarias
- Verifica que el archivo `vercel.json` esté en la raíz del proyecto


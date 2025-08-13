from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)

# ✅ CRÍTICO: Habilitar CORS para permitir requests desde el navegador
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5000", "http://127.0.0.1:5000"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type"]
    }
})

# Estado global del sistema
system_state = {
    "wallets_generated": 0,
    "system_status": "Inactive",
    "total_balance": 0.0,
    "completed_tasks": 0,
    "failed_tasks": 0,
    "last_activity": None,
    "connections": 1,
    "hunting_active": False
}

# ✅ Ruta principal del dashboard
@app.route('/')
def dashboard():
    """Ruta principal que sirve el dashboard"""
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard_alt():
    """Ruta alternativa para el dashboard"""
    return render_template('dashboard.html')

# ✅ API: Obtener estadísticas del sistema
@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Endpoint para obtener estadísticas del sistema"""
    try:
        # Actualizar timestamp
        system_state["last_activity"] = datetime.now().strftime("%H:%M:%S")
        
        print(f"📊 Stats requested: {system_state}")
        
        return jsonify({
            "status": "success",
            "wallets_generated": system_state["wallets_generated"],
            "system_status": system_state["system_status"],
            "total_balance": system_state["total_balance"],
            "completed_tasks": system_state["completed_tasks"],
            "failed_tasks": system_state["failed_tasks"],
            "last_activity": system_state["last_activity"],
            "connections": system_state["connections"],
            "hunting_active": system_state["hunting_active"]
        })
    except Exception as e:
        print(f"❌ Error in /api/stats: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ API: Generar wallets
@app.route('/api/control/generate-wallets', methods=['POST'])
def generate_wallets():
    """Endpoint para generar nuevas wallets"""
    try:
        print("🕷️ Generate wallets request received")
        
        # Simular generación de wallets
        new_wallets = 5
        system_state["wallets_generated"] += new_wallets
        system_state["last_activity"] = datetime.now().strftime("%H:%M:%S")
        
        print(f"✅ Generated {new_wallets} wallets. Total: {system_state['wallets_generated']}")
        
        return jsonify({
            "status": "success",
            "message": f"Successfully generated {new_wallets} new wallets",
            "wallets_generated": new_wallets,
            "total_wallets": system_state["wallets_generated"]
        })
        
    except Exception as e:
        print(f"❌ Error generating wallets: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ API: Iniciar hunting
@app.route('/api/control/start-hunting', methods=['POST'])
def start_hunting():
    """Endpoint para iniciar el sistema de hunting"""
    try:
        print("🎯 Start hunting request received")
        
        if system_state["hunting_active"]:
            return jsonify({
                "status": "warning",
                "message": "Hunting system is already active"
            })
        
        # Activar sistema
        system_state["hunting_active"] = True
        system_state["system_status"] = "Active"
        system_state["last_activity"] = datetime.now().strftime("%H:%M:%S")
        
        print("✅ Hunting system started successfully")
        
        return jsonify({
            "status": "success",
            "message": "Hunting system started successfully",
            "system_status": system_state["system_status"]
        })
        
    except Exception as e:
        print(f"❌ Error starting hunting: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ API: Detener hunting
@app.route('/api/control/stop-hunting', methods=['POST'])
def stop_hunting():
    """Endpoint para detener el sistema de hunting"""
    try:
        print("🛑 Stop hunting request received")
        
        if not system_state["hunting_active"]:
            return jsonify({
                "status": "warning",
                "message": "Hunting system is already inactive"
            })
        
        # Desactivar sistema
        system_state["hunting_active"] = False
        system_state["system_status"] = "Inactive"
        system_state["last_activity"] = datetime.now().strftime("%H:%M:%S")
        
        print("✅ Hunting system stopped successfully")
        
        return jsonify({
            "status": "success",
            "message": "Hunting system stopped successfully",
            "system_status": system_state["system_status"]
        })
        
    except Exception as e:
        print(f"❌ Error stopping hunting: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ API: Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar el estado del servidor"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "server": "KAY CORP Flask Server",
        "version": "1.0.0"
    })

# ✅ Manejo de errores 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"status": "error", "message": "Endpoint not found"}), 404

# ✅ Manejo de errores 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"status": "error", "message": "Internal server error"}), 500

@app.route('/simple')
def simple_dashboard():
    """Dashboard simplificado"""
    return render_template('simple.html')

@app.route('/debug')
def debug_page():
    """Página de debugging"""
    return render_template('debug.html')

@app.route('/data/<path:filename>')
def serve_data_file(filename):
    """Servir archivos JSON desde la carpeta data"""
    return send_from_directory('data', filename)

if __name__ == '__main__':
    print("🚀 Starting KAY CORP Flask Server...")
    print("📋 Available endpoints:")
    print("   GET  /                              -> Dashboard")
    print("   GET  /dashboard                     -> Dashboard")
    print("   GET  /simple                        -> Simple Dashboard")
    print("   GET  /debug                         -> Debug Page")
    print("   GET  /api/stats                     -> System statistics")
    print("   POST /api/control/generate-wallets  -> Generate wallets")
    print("   POST /api/control/start-hunting     -> Start hunting")
    print("   POST /api/control/stop-hunting      -> Stop hunting")
    print("   GET  /api/health                    -> Health check")
    print("")
    print("🌐 Server will be available at:")
    print("   http://localhost:5000")
    print("   http://127.0.0.1:5000")
    print("")
    print("🧪 Test URLs:")
    print("   http://127.0.0.1:5000/api/health    -> Test server")
    print("   http://127.0.0.1:5000/simple        -> Working dashboard")
    print("")
    
    try:
        # ✅ CONFIGURACIÓN CORRECTA DEL SERVIDOR
        app.run(
            host='127.0.0.1',  # ✅ Usar 127.0.0.1 en lugar de 0.0.0.0
            port=5000,
            debug=True,        # ✅ Modo debug para desarrollo
            threaded=True      # ✅ Permitir múltiples requests simultáneos
        )
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        print("💡 Try running: pip install flask flask-cors")
        print("💡 Or check if port 5000 is already in use")
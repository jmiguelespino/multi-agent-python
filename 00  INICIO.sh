# 1. (Recomendado) Crear un entorno virtual de Python
python -m venv venv

# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# 2. Instalar las librerías cuantitativas necesarias
python -m pip install -r requirements.txt

python main.py

🎯 Resultado final del proyecto
Solo necesitas 2 terminales:
    python main.py — hace TODO: pipeline + reporte diario + control remoto
    python telegram_commands.py — solo si quieres controlar desde el móvil (opcional)
    python monitor.py — opcional, para alertas de heartbeat

📌 Resumen de qué hace cada archivo nuevo
Archivo	                Qué hace
analyze_by_symbol.py	Análisis por símbolo
analyze_performance.py	Métricas: Sharpe, Sortino, Max DD, win rate por activo, profit factor, rachas, PnL por hora. Opción --export a CSV
telegram_commands.py	Escucha comandos de Telegram y escribe control_state.json. No ejecuta órdenes directamente — el main.py las lee
test_smoke.py	        30 trades simulados ahora. Valida guardrails del learner
test_integration_mt5.py	Abre/cierra una orden real de 0.01 en demo. Verifica PnL, SL, deals
main.py	                Ahora lee control_state.json cada ciclo: respeta pausa, ejecuta close_all


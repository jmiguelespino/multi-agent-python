Listado de rutas de carpetas para el volumen Windows

El número de serie del volumen es 2EB0-9B79

C:.

¦   .env

¦   .env.example

¦   .gitignore

¦   00  INICIO.sh

¦   analyze\_by\_symbol.py

¦   analyze\_performance.py

##### ¦   **audit\_logger.py**

¦   Changelog.md

¦   check\_lots.py

##### **¦   config\_optimized.json**

##### **¦   daily\_report.py**

##### ¦   **data\_streamer.py**

¦   diagnostico\_forex.py

¦   diagnostico\_proyecto.py

¦   directorio.txt

##### ¦   **execution\_agent.py**

##### ¦   **feature\_agent.py**

##### **¦   feedback\_learner.py**

##### ¦   **main.py**

¦   monitor.py

##### ¦   **mt5\_bridge.py**

¦   Prompt de Inicio.txt

¦   QuantEdge AI — Motor Autónomo de Trading Algorítmico Institucional y Guía de Instalación.doc

¦   README.md

¦   requirements.txt

##### ¦   **risk\_guardian.py**

##### **¦   signal\_agent.py**

¦   telegram\_commands.py

##### ¦   **telegram\_notifier.py**

¦   test\_accounts.py

¦   test\_by\_symbol.py

¦   test\_candidate.py

¦   test\_integration\_mt5.py

¦   test\_operac\_desde\_21.py

##### **¦   test\_smoke.py**

¦   

+---logs

¦       trade\_audit\_history.jsonl

¦       trade\_audit\_history1.txt

¦       



ORDEN DE CORRECCIÓN RECOMENDADO



&#x20;   BUG #1 (is\_buyer\_maker en main.py) — afecta a todas las señales.



&#x20;   BUG #3 (M15 no resuelve símbolo) — el FIX #2 puede estar inactivo.



&#x20;   BUG #2 (data\_streamer.py huérfano) — confusión y código muerto.



&#x20;   BUG #7 (PnL=0.0 en cierres) — el Agente 5 aprende de datos incorrectos.



&#x20;   MEJORA #6 (persistencia del Risk Guardian) — protege contra reinicios.



&#x20;   BUG #4, #5, #6 — mejoras de robustez.



&#x20;   MEJORA #1 (unificar get\_canonical\_asset) — mantenibilidad.



&#x20;   Resto de mejoras — nice to have.



? Preguntas para ti



&#x20;   ¿El bot está operando con WTI como símbolo lógico? Si es así, el BUG #3 es crítico porque el filtro M15 nunca se aplica a WTI/BRENT.



&#x20;   ¿Quieres que te escriba los archivos corregidos completos (como hice con mt5\_bridge.py), o prefieres que te dé los parches puntuales?



&#x20;   ¿Tienes test\_smoke.py? Me gustaría ver qué valida exactamente para asegurarme de que los fixes no rompen los tests.



Si me pasas test\_smoke.py, config\_optimized.json y .env.example, cierro el análisis completo.

This response is AI-generated, for reference only.











+---venv

¦   ¦   .gitignore

¦   ¦   pyvenv.cfg

¦   ¦   

¦   +---Include

¦   +---Lib

¦   ¦   +---site-packages

¦   ¦       ¦   six.py

¦   ¦       ¦   

¦   ¦       +---aiohappyeyeballs

¦   ¦       ¦   ¦   impl.py

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   types.py

¦   ¦       ¦   ¦   utils.py

¦   ¦       ¦   ¦   \_staggered.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           impl.cpython-314.pyc

¦   ¦       ¦           types.cpython-314.pyc

¦   ¦       ¦           utils.cpython-314.pyc

¦   ¦       ¦           \_staggered.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---aiohappyeyeballs-2.7.1.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           

¦   ¦       +---aiohttp

¦   ¦       ¦   ¦   abc.py

¦   ¦       ¦   ¦   base\_protocol.py

¦   ¦       ¦   ¦   client.py

¦   ¦       ¦   ¦   client\_exceptions.py

¦   ¦       ¦   ¦   client\_middlewares.py

¦   ¦       ¦   ¦   client\_middleware\_digest\_auth.py

¦   ¦       ¦   ¦   client\_proto.py

¦   ¦       ¦   ¦   client\_reqrep.py

¦   ¦       ¦   ¦   client\_ws.py

¦   ¦       ¦   ¦   compression\_utils.py

¦   ¦       ¦   ¦   connector.py

¦   ¦       ¦   ¦   cookiejar.py

¦   ¦       ¦   ¦   formdata.py

¦   ¦       ¦   ¦   hdrs.py

¦   ¦       ¦   ¦   helpers.py

¦   ¦       ¦   ¦   http.py

¦   ¦       ¦   ¦   http\_exceptions.py

¦   ¦       ¦   ¦   http\_parser.py

¦   ¦       ¦   ¦   http\_websocket.py

¦   ¦       ¦   ¦   http\_writer.py

¦   ¦       ¦   ¦   log.py

¦   ¦       ¦   ¦   multipart.py

¦   ¦       ¦   ¦   payload.py

¦   ¦       ¦   ¦   payload\_streamer.py

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   pytest\_plugin.py

¦   ¦       ¦   ¦   resolver.py

¦   ¦       ¦   ¦   streams.py

¦   ¦       ¦   ¦   tcp\_helpers.py

¦   ¦       ¦   ¦   test\_utils.py

¦   ¦       ¦   ¦   tracing.py

¦   ¦       ¦   ¦   typedefs.py

¦   ¦       ¦   ¦   web.py

¦   ¦       ¦   ¦   web\_app.py

¦   ¦       ¦   ¦   web\_exceptions.py

¦   ¦       ¦   ¦   web\_fileresponse.py

¦   ¦       ¦   ¦   web\_log.py

¦   ¦       ¦   ¦   web\_middlewares.py

¦   ¦       ¦   ¦   web\_protocol.py

¦   ¦       ¦   ¦   web\_request.py

¦   ¦       ¦   ¦   web\_response.py

¦   ¦       ¦   ¦   web\_routedef.py

¦   ¦       ¦   ¦   web\_runner.py

¦   ¦       ¦   ¦   web\_server.py

¦   ¦       ¦   ¦   web\_urldispatcher.py

¦   ¦       ¦   ¦   web\_ws.py

¦   ¦       ¦   ¦   worker.py

¦   ¦       ¦   ¦   \_cookie\_helpers.py

¦   ¦       ¦   ¦   \_cparser.pxd

¦   ¦       ¦   ¦   \_find\_header.pxd

¦   ¦       ¦   ¦   \_headers.pxi

¦   ¦       ¦   ¦   \_http\_parser.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   \_http\_parser.pyx

¦   ¦       ¦   ¦   \_http\_writer.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   \_http\_writer.pyx

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_websocket

¦   ¦       ¦   ¦   ¦   helpers.py

¦   ¦       ¦   ¦   ¦   mask.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   mask.pxd

¦   ¦       ¦   ¦   ¦   mask.pyx

¦   ¦       ¦   ¦   ¦   models.py

¦   ¦       ¦   ¦   ¦   reader.py

¦   ¦       ¦   ¦   ¦   reader\_c.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   reader\_c.pxd

¦   ¦       ¦   ¦   ¦   reader\_c.py

¦   ¦       ¦   ¦   ¦   reader\_py.py

¦   ¦       ¦   ¦   ¦   writer.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           helpers.cpython-314.pyc

¦   ¦       ¦   ¦           models.cpython-314.pyc

¦   ¦       ¦   ¦           reader.cpython-314.pyc

¦   ¦       ¦   ¦           reader\_c.cpython-314.pyc

¦   ¦       ¦   ¦           reader\_py.cpython-314.pyc

¦   ¦       ¦   ¦           writer.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           abc.cpython-314.pyc

¦   ¦       ¦           base\_protocol.cpython-314.pyc

¦   ¦       ¦           client.cpython-314.pyc

¦   ¦       ¦           client\_exceptions.cpython-314.pyc

¦   ¦       ¦           client\_middlewares.cpython-314.pyc

¦   ¦       ¦           client\_middleware\_digest\_auth.cpython-314.pyc

¦   ¦       ¦           client\_proto.cpython-314.pyc

¦   ¦       ¦           client\_reqrep.cpython-314.pyc

¦   ¦       ¦           client\_ws.cpython-314.pyc

¦   ¦       ¦           compression\_utils.cpython-314.pyc

¦   ¦       ¦           connector.cpython-314.pyc

¦   ¦       ¦           cookiejar.cpython-314.pyc

¦   ¦       ¦           formdata.cpython-314.pyc

¦   ¦       ¦           hdrs.cpython-314.pyc

¦   ¦       ¦           helpers.cpython-314.pyc

¦   ¦       ¦           http.cpython-314.pyc

¦   ¦       ¦           http\_exceptions.cpython-314.pyc

¦   ¦       ¦           http\_parser.cpython-314.pyc

¦   ¦       ¦           http\_websocket.cpython-314.pyc

¦   ¦       ¦           http\_writer.cpython-314.pyc

¦   ¦       ¦           log.cpython-314.pyc

¦   ¦       ¦           multipart.cpython-314.pyc

¦   ¦       ¦           payload.cpython-314.pyc

¦   ¦       ¦           payload\_streamer.cpython-314.pyc

¦   ¦       ¦           pytest\_plugin.cpython-314.pyc

¦   ¦       ¦           resolver.cpython-314.pyc

¦   ¦       ¦           streams.cpython-314.pyc

¦   ¦       ¦           tcp\_helpers.cpython-314.pyc

¦   ¦       ¦           test\_utils.cpython-314.pyc

¦   ¦       ¦           tracing.cpython-314.pyc

¦   ¦       ¦           typedefs.cpython-314.pyc

¦   ¦       ¦           web.cpython-314.pyc

¦   ¦       ¦           web\_app.cpython-314.pyc

¦   ¦       ¦           web\_exceptions.cpython-314.pyc

¦   ¦       ¦           web\_fileresponse.cpython-314.pyc

¦   ¦       ¦           web\_log.cpython-314.pyc

¦   ¦       ¦           web\_middlewares.cpython-314.pyc

¦   ¦       ¦           web\_protocol.cpython-314.pyc

¦   ¦       ¦           web\_request.cpython-314.pyc

¦   ¦       ¦           web\_response.cpython-314.pyc

¦   ¦       ¦           web\_routedef.cpython-314.pyc

¦   ¦       ¦           web\_runner.cpython-314.pyc

¦   ¦       ¦           web\_server.cpython-314.pyc

¦   ¦       ¦           web\_urldispatcher.cpython-314.pyc

¦   ¦       ¦           web\_ws.cpython-314.pyc

¦   ¦       ¦           worker.cpython-314.pyc

¦   ¦       ¦           \_cookie\_helpers.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---aiohttp-3.14.3.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   REQUESTED

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦       ¦   LICENSE.txt

¦   ¦       ¦       ¦   

¦   ¦       ¦       +---vendor

¦   ¦       ¦           +---llhttp

¦   ¦       ¦                   LICENSE

¦   ¦       ¦                   

¦   ¦       +---aiosignal

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---aiosignal-1.4.0.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           

¦   ¦       +---attr

¦   ¦       ¦   ¦   converters.py

¦   ¦       ¦   ¦   converters.pyi

¦   ¦       ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   exceptions.pyi

¦   ¦       ¦   ¦   filters.py

¦   ¦       ¦   ¦   filters.pyi

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   setters.py

¦   ¦       ¦   ¦   setters.pyi

¦   ¦       ¦   ¦   validators.py

¦   ¦       ¦   ¦   validators.pyi

¦   ¦       ¦   ¦   \_cmp.py

¦   ¦       ¦   ¦   \_cmp.pyi

¦   ¦       ¦   ¦   \_compat.py

¦   ¦       ¦   ¦   \_config.py

¦   ¦       ¦   ¦   \_funcs.py

¦   ¦       ¦   ¦   \_make.py

¦   ¦       ¦   ¦   \_next\_gen.py

¦   ¦       ¦   ¦   \_typing\_compat.pyi

¦   ¦       ¦   ¦   \_version\_info.py

¦   ¦       ¦   ¦   \_version\_info.pyi

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           converters.cpython-314.pyc

¦   ¦       ¦           exceptions.cpython-314.pyc

¦   ¦       ¦           filters.cpython-314.pyc

¦   ¦       ¦           setters.cpython-314.pyc

¦   ¦       ¦           validators.cpython-314.pyc

¦   ¦       ¦           \_cmp.cpython-314.pyc

¦   ¦       ¦           \_compat.cpython-314.pyc

¦   ¦       ¦           \_config.cpython-314.pyc

¦   ¦       ¦           \_funcs.cpython-314.pyc

¦   ¦       ¦           \_make.cpython-314.pyc

¦   ¦       ¦           \_next\_gen.cpython-314.pyc

¦   ¦       ¦           \_version\_info.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---attrs

¦   ¦       ¦   ¦   converters.py

¦   ¦       ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   filters.py

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   setters.py

¦   ¦       ¦   ¦   validators.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           converters.cpython-314.pyc

¦   ¦       ¦           exceptions.cpython-314.pyc

¦   ¦       ¦           filters.cpython-314.pyc

¦   ¦       ¦           setters.cpython-314.pyc

¦   ¦       ¦           validators.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---attrs-26.1.0.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           

¦   ¦       +---dateutil

¦   ¦       ¦   ¦   easter.py

¦   ¦       ¦   ¦   relativedelta.py

¦   ¦       ¦   ¦   rrule.py

¦   ¦       ¦   ¦   tzwin.py

¦   ¦       ¦   ¦   utils.py

¦   ¦       ¦   ¦   \_common.py

¦   ¦       ¦   ¦   \_version.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---parser

¦   ¦       ¦   ¦   ¦   isoparser.py

¦   ¦       ¦   ¦   ¦   \_parser.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           isoparser.cpython-314.pyc

¦   ¦       ¦   ¦           \_parser.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---tz

¦   ¦       ¦   ¦   ¦   tz.py

¦   ¦       ¦   ¦   ¦   win.py

¦   ¦       ¦   ¦   ¦   \_common.py

¦   ¦       ¦   ¦   ¦   \_factories.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           tz.cpython-314.pyc

¦   ¦       ¦   ¦           win.cpython-314.pyc

¦   ¦       ¦   ¦           \_common.cpython-314.pyc

¦   ¦       ¦   ¦           \_factories.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---zoneinfo

¦   ¦       ¦   ¦   ¦   dateutil-zoneinfo.tar.gz

¦   ¦       ¦   ¦   ¦   rebuild.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           rebuild.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           easter.cpython-314.pyc

¦   ¦       ¦           relativedelta.cpython-314.pyc

¦   ¦       ¦           rrule.cpython-314.pyc

¦   ¦       ¦           tzwin.cpython-314.pyc

¦   ¦       ¦           utils.cpython-314.pyc

¦   ¦       ¦           \_common.cpython-314.pyc

¦   ¦       ¦           \_version.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---dotenv

¦   ¦       ¦   ¦   cli.py

¦   ¦       ¦   ¦   ipython.py

¦   ¦       ¦   ¦   main.py

¦   ¦       ¦   ¦   parser.py

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   variables.py

¦   ¦       ¦   ¦   version.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           cli.cpython-314.pyc

¦   ¦       ¦           ipython.cpython-314.pyc

¦   ¦       ¦           main.cpython-314.pyc

¦   ¦       ¦           parser.cpython-314.pyc

¦   ¦       ¦           variables.cpython-314.pyc

¦   ¦       ¦           version.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---frozenlist

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   \_frozenlist.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   \_frozenlist.pyx

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---frozenlist-1.8.0.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           

¦   ¦       +---idna

¦   ¦       ¦   ¦   cli.py

¦   ¦       ¦   ¦   codec.py

¦   ¦       ¦   ¦   compat.py

¦   ¦       ¦   ¦   core.py

¦   ¦       ¦   ¦   idnadata.py

¦   ¦       ¦   ¦   intranges.py

¦   ¦       ¦   ¦   package\_data.py

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   uts46data.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           cli.cpython-314.pyc

¦   ¦       ¦           codec.cpython-314.pyc

¦   ¦       ¦           compat.cpython-314.pyc

¦   ¦       ¦           core.cpython-314.pyc

¦   ¦       ¦           idnadata.cpython-314.pyc

¦   ¦       ¦           intranges.cpython-314.pyc

¦   ¦       ¦           package\_data.cpython-314.pyc

¦   ¦       ¦           uts46data.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---idna-3.20.dist-info

¦   ¦       ¦   ¦   entry\_points.txt

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE.md

¦   ¦       ¦           

¦   ¦       +---MetaTrader5

¦   ¦       ¦   ¦   \_core.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---metatrader5-5.0.6180.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   REQUESTED

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE.txt

¦   ¦       ¦           

¦   ¦       +---multidict

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   \_abc.py

¦   ¦       ¦   ¦   \_compat.py

¦   ¦       ¦   ¦   \_multidict.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   \_multidict\_py.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           \_abc.cpython-314.pyc

¦   ¦       ¦           \_compat.cpython-314.pyc

¦   ¦       ¦           \_multidict\_py.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---multidict-6.9.1.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           

¦   ¦       +---numpy

¦   ¦       ¦   ¦   conftest.py

¦   ¦       ¦   ¦   dtypes.py

¦   ¦       ¦   ¦   dtypes.pyi

¦   ¦       ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   exceptions.pyi

¦   ¦       ¦   ¦   matlib.py

¦   ¦       ¦   ¦   matlib.pyi

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   version.py

¦   ¦       ¦   ¦   version.pyi

¦   ¦       ¦   ¦   \_array\_api\_info.py

¦   ¦       ¦   ¦   \_array\_api\_info.pyi

¦   ¦       ¦   ¦   \_configtool.py

¦   ¦       ¦   ¦   \_configtool.pyi

¦   ¦       ¦   ¦   \_distributor\_init.py

¦   ¦       ¦   ¦   \_distributor\_init.pyi

¦   ¦       ¦   ¦   \_expired\_attrs\_2\_0.py

¦   ¦       ¦   ¦   \_expired\_attrs\_2\_0.pyi

¦   ¦       ¦   ¦   \_globals.py

¦   ¦       ¦   ¦   \_globals.pyi

¦   ¦       ¦   ¦   \_pytesttester.py

¦   ¦       ¦   ¦   \_pytesttester.pyi

¦   ¦       ¦   ¦   \_\_config\_\_.py

¦   ¦       ¦   ¦   \_\_config\_\_.pyi

¦   ¦       ¦   ¦   \_\_init\_\_.cython-30.pxd

¦   ¦       ¦   ¦   \_\_init\_\_.pxd

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---char

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---core

¦   ¦       ¦   ¦   ¦   arrayprint.py

¦   ¦       ¦   ¦   ¦   arrayprint.pyi

¦   ¦       ¦   ¦   ¦   defchararray.py

¦   ¦       ¦   ¦   ¦   defchararray.pyi

¦   ¦       ¦   ¦   ¦   einsumfunc.py

¦   ¦       ¦   ¦   ¦   einsumfunc.pyi

¦   ¦       ¦   ¦   ¦   fromnumeric.py

¦   ¦       ¦   ¦   ¦   fromnumeric.pyi

¦   ¦       ¦   ¦   ¦   function\_base.py

¦   ¦       ¦   ¦   ¦   function\_base.pyi

¦   ¦       ¦   ¦   ¦   getlimits.py

¦   ¦       ¦   ¦   ¦   getlimits.pyi

¦   ¦       ¦   ¦   ¦   multiarray.py

¦   ¦       ¦   ¦   ¦   multiarray.pyi

¦   ¦       ¦   ¦   ¦   numeric.py

¦   ¦       ¦   ¦   ¦   numeric.pyi

¦   ¦       ¦   ¦   ¦   numerictypes.py

¦   ¦       ¦   ¦   ¦   numerictypes.pyi

¦   ¦       ¦   ¦   ¦   overrides.py

¦   ¦       ¦   ¦   ¦   overrides.pyi

¦   ¦       ¦   ¦   ¦   records.py

¦   ¦       ¦   ¦   ¦   records.pyi

¦   ¦       ¦   ¦   ¦   shape\_base.py

¦   ¦       ¦   ¦   ¦   shape\_base.pyi

¦   ¦       ¦   ¦   ¦   umath.py

¦   ¦       ¦   ¦   ¦   umath.pyi

¦   ¦       ¦   ¦   ¦   \_dtype.py

¦   ¦       ¦   ¦   ¦   \_dtype.pyi

¦   ¦       ¦   ¦   ¦   \_dtype\_ctypes.py

¦   ¦       ¦   ¦   ¦   \_dtype\_ctypes.pyi

¦   ¦       ¦   ¦   ¦   \_internal.py

¦   ¦       ¦   ¦   ¦   \_internal.pyi

¦   ¦       ¦   ¦   ¦   \_multiarray\_umath.py

¦   ¦       ¦   ¦   ¦   \_utils.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           arrayprint.cpython-314.pyc

¦   ¦       ¦   ¦           defchararray.cpython-314.pyc

¦   ¦       ¦   ¦           einsumfunc.cpython-314.pyc

¦   ¦       ¦   ¦           fromnumeric.cpython-314.pyc

¦   ¦       ¦   ¦           function\_base.cpython-314.pyc

¦   ¦       ¦   ¦           getlimits.cpython-314.pyc

¦   ¦       ¦   ¦           multiarray.cpython-314.pyc

¦   ¦       ¦   ¦           numeric.cpython-314.pyc

¦   ¦       ¦   ¦           numerictypes.cpython-314.pyc

¦   ¦       ¦   ¦           overrides.cpython-314.pyc

¦   ¦       ¦   ¦           records.cpython-314.pyc

¦   ¦       ¦   ¦           shape\_base.cpython-314.pyc

¦   ¦       ¦   ¦           umath.cpython-314.pyc

¦   ¦       ¦   ¦           \_dtype.cpython-314.pyc

¦   ¦       ¦   ¦           \_dtype\_ctypes.cpython-314.pyc

¦   ¦       ¦   ¦           \_internal.cpython-314.pyc

¦   ¦       ¦   ¦           \_multiarray\_umath.cpython-314.pyc

¦   ¦       ¦   ¦           \_utils.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---ctypeslib

¦   ¦       ¦   ¦   ¦   \_ctypeslib.py

¦   ¦       ¦   ¦   ¦   \_ctypeslib.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_ctypeslib.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---doc

¦   ¦       ¦   ¦   ¦   ufuncs.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           ufuncs.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---f2py

¦   ¦       ¦   ¦   ¦   auxfuncs.py

¦   ¦       ¦   ¦   ¦   auxfuncs.pyi

¦   ¦       ¦   ¦   ¦   capi\_maps.py

¦   ¦       ¦   ¦   ¦   capi\_maps.pyi

¦   ¦       ¦   ¦   ¦   cb\_rules.py

¦   ¦       ¦   ¦   ¦   cb\_rules.pyi

¦   ¦       ¦   ¦   ¦   cfuncs.py

¦   ¦       ¦   ¦   ¦   cfuncs.pyi

¦   ¦       ¦   ¦   ¦   common\_rules.py

¦   ¦       ¦   ¦   ¦   common\_rules.pyi

¦   ¦       ¦   ¦   ¦   crackfortran.py

¦   ¦       ¦   ¦   ¦   crackfortran.pyi

¦   ¦       ¦   ¦   ¦   diagnose.py

¦   ¦       ¦   ¦   ¦   diagnose.pyi

¦   ¦       ¦   ¦   ¦   f2py2e.py

¦   ¦       ¦   ¦   ¦   f2py2e.pyi

¦   ¦       ¦   ¦   ¦   f90mod\_rules.py

¦   ¦       ¦   ¦   ¦   f90mod\_rules.pyi

¦   ¦       ¦   ¦   ¦   func2subr.py

¦   ¦       ¦   ¦   ¦   func2subr.pyi

¦   ¦       ¦   ¦   ¦   rules.py

¦   ¦       ¦   ¦   ¦   rules.pyi

¦   ¦       ¦   ¦   ¦   setup.cfg

¦   ¦       ¦   ¦   ¦   symbolic.py

¦   ¦       ¦   ¦   ¦   symbolic.pyi

¦   ¦       ¦   ¦   ¦   use\_rules.py

¦   ¦       ¦   ¦   ¦   use\_rules.pyi

¦   ¦       ¦   ¦   ¦   \_isocbind.py

¦   ¦       ¦   ¦   ¦   \_isocbind.pyi

¦   ¦       ¦   ¦   ¦   \_src\_pyf.py

¦   ¦       ¦   ¦   ¦   \_src\_pyf.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_version\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_version\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---src

¦   ¦       ¦   ¦   ¦       fortranobject.c

¦   ¦       ¦   ¦   ¦       fortranobject.h

¦   ¦       ¦   ¦   ¦       

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_abstract\_interface.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array\_from\_pyobj.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assumed\_shape.py

¦   ¦       ¦   ¦   ¦   ¦   test\_block\_docstring.py

¦   ¦       ¦   ¦   ¦   ¦   test\_callback.py

¦   ¦       ¦   ¦   ¦   ¦   test\_capi\_maps.py

¦   ¦       ¦   ¦   ¦   ¦   test\_character.py

¦   ¦       ¦   ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_crackfortran.py

¦   ¦       ¦   ¦   ¦   ¦   test\_data.py

¦   ¦       ¦   ¦   ¦   ¦   test\_docs.py

¦   ¦       ¦   ¦   ¦   ¦   test\_f2cmap.py

¦   ¦       ¦   ¦   ¦   ¦   test\_f2py2e.py

¦   ¦       ¦   ¦   ¦   ¦   test\_inplace.py

¦   ¦       ¦   ¦   ¦   ¦   test\_isoc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_kind.py

¦   ¦       ¦   ¦   ¦   ¦   test\_mixed.py

¦   ¦       ¦   ¦   ¦   ¦   test\_modules.py

¦   ¦       ¦   ¦   ¦   ¦   test\_parameter.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pyf\_src.py

¦   ¦       ¦   ¦   ¦   ¦   test\_quoted\_character.py

¦   ¦       ¦   ¦   ¦   ¦   test\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   test\_return\_character.py

¦   ¦       ¦   ¦   ¦   ¦   test\_return\_complex.py

¦   ¦       ¦   ¦   ¦   ¦   test\_return\_integer.py

¦   ¦       ¦   ¦   ¦   ¦   test\_return\_logical.py

¦   ¦       ¦   ¦   ¦   ¦   test\_return\_real.py

¦   ¦       ¦   ¦   ¦   ¦   test\_routines.py

¦   ¦       ¦   ¦   ¦   ¦   test\_semicolon\_split.py

¦   ¦       ¦   ¦   ¦   ¦   test\_size.py

¦   ¦       ¦   ¦   ¦   ¦   test\_string.py

¦   ¦       ¦   ¦   ¦   ¦   test\_symbolic.py

¦   ¦       ¦   ¦   ¦   ¦   test\_value\_attrspec.py

¦   ¦       ¦   ¦   ¦   ¦   util.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---src

¦   ¦       ¦   ¦   ¦   ¦   +---abstract\_interface

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh18403\_mod.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---array\_from\_pyobj

¦   ¦       ¦   ¦   ¦   ¦   ¦       wrapmodule.c

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---assumed\_shape

¦   ¦       ¦   ¦   ¦   ¦   ¦       .f2py\_f2cmap

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo\_free.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo\_mod.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo\_use.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       precision.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---block\_docstring

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---callback

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh17797.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh18335.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh25211.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh25211.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh26681.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---cli

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh\_22819.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       hi77.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       hiworld.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---common

¦   ¦       ¦   ¦   ¦   ¦   ¦       block.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh19161.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---crackfortran

¦   ¦       ¦   ¦   ¦   ¦   ¦       accesstype.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       common\_with\_division.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       data\_common.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       data\_multiplier.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       data\_stmts.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       data\_with\_comments.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo\_deps.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh15035.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh17859.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh22648.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh23533.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh23598.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh23598Warn.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh23879.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh27697.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh2848.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       operators.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       privatemod.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       publicmod.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       pubprivmod.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       unicode\_comment.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---f2cmap

¦   ¦       ¦   ¦   ¦   ¦   ¦       .f2py\_f2cmap

¦   ¦       ¦   ¦   ¦   ¦   ¦       isoFortranEnvMap.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---inplace

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---isocintrin

¦   ¦       ¦   ¦   ¦   ¦   ¦       isoCtests.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---kind

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---mixed

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo\_fixed.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo\_free.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---modules

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   module\_data\_docstring.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   use\_modules.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---gh25337

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦       data.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦       use\_data.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---gh26920

¦   ¦       ¦   ¦   ¦   ¦   ¦           two\_mods\_with\_no\_public\_entities.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦           two\_mods\_with\_one\_public\_routine.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---negative\_bounds

¦   ¦       ¦   ¦   ¦   ¦   ¦       issue\_20853.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---parameter

¦   ¦       ¦   ¦   ¦   ¦   ¦       constant\_array.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       constant\_both.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       constant\_compound.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       constant\_integer.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       constant\_non\_compound.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       constant\_real.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---quoted\_character

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---regression

¦   ¦       ¦   ¦   ¦   ¦   ¦       AB.inc

¦   ¦       ¦   ¦   ¦   ¦   ¦       assignOnlyModule.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       complex\_struct\_compat.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       complex\_struct\_compat.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       datonly.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       f77comments.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       f77fixedform.f95

¦   ¦       ¦   ¦   ¦   ¦   ¦       f90continuation.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       incfile.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       inout.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       lower\_f2py\_fortran.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       mod\_derived\_types.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---return\_character

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---return\_complex

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---return\_integer

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---return\_logical

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---return\_real

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---routines

¦   ¦       ¦   ¦   ¦   ¦   ¦       funcfortranname.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       funcfortranname.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       subrout.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       subrout.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---size

¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---string

¦   ¦       ¦   ¦   ¦   ¦   ¦       char.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       fixed\_string.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh24008.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh24662.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh25286.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh25286.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       gh25286\_bc.pyf

¦   ¦       ¦   ¦   ¦   ¦   ¦       scalar\_string.f90

¦   ¦       ¦   ¦   ¦   ¦   ¦       string.f

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---value\_attrspec

¦   ¦       ¦   ¦   ¦   ¦           gh21665.f90

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_abstract\_interface.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array\_from\_pyobj.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assumed\_shape.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_block\_docstring.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_callback.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_capi\_maps.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_character.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_crackfortran.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_data.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_docs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_f2cmap.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_f2py2e.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_inplace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_isoc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_kind.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_mixed.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_modules.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_parameter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pyf\_src.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_quoted\_character.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_return\_character.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_return\_complex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_return\_integer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_return\_logical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_return\_real.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_routines.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_semicolon\_split.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_size.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_symbolic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_value\_attrspec.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_backends

¦   ¦       ¦   ¦   ¦   ¦   meson.build.template

¦   ¦       ¦   ¦   ¦   ¦   \_backend.py

¦   ¦       ¦   ¦   ¦   ¦   \_backend.pyi

¦   ¦       ¦   ¦   ¦   ¦   \_meson.py

¦   ¦       ¦   ¦   ¦   ¦   \_meson.pyi

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_backend.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_meson.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           auxfuncs.cpython-314.pyc

¦   ¦       ¦   ¦           capi\_maps.cpython-314.pyc

¦   ¦       ¦   ¦           cb\_rules.cpython-314.pyc

¦   ¦       ¦   ¦           cfuncs.cpython-314.pyc

¦   ¦       ¦   ¦           common\_rules.cpython-314.pyc

¦   ¦       ¦   ¦           crackfortran.cpython-314.pyc

¦   ¦       ¦   ¦           diagnose.cpython-314.pyc

¦   ¦       ¦   ¦           f2py2e.cpython-314.pyc

¦   ¦       ¦   ¦           f90mod\_rules.cpython-314.pyc

¦   ¦       ¦   ¦           func2subr.cpython-314.pyc

¦   ¦       ¦   ¦           rules.cpython-314.pyc

¦   ¦       ¦   ¦           symbolic.cpython-314.pyc

¦   ¦       ¦   ¦           use\_rules.cpython-314.pyc

¦   ¦       ¦   ¦           \_isocbind.cpython-314.pyc

¦   ¦       ¦   ¦           \_src\_pyf.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_version\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---fft

¦   ¦       ¦   ¦   ¦   \_helper.py

¦   ¦       ¦   ¦   ¦   \_helper.pyi

¦   ¦       ¦   ¦   ¦   \_pocketfft.py

¦   ¦       ¦   ¦   ¦   \_pocketfft.pyi

¦   ¦       ¦   ¦   ¦   \_pocketfft\_umath.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_pocketfft\_umath.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_helper.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pocketfft.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_helper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pocketfft.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_helper.cpython-314.pyc

¦   ¦       ¦   ¦           \_pocketfft.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---lib

¦   ¦       ¦   ¦   ¦   array\_utils.py

¦   ¦       ¦   ¦   ¦   array\_utils.pyi

¦   ¦       ¦   ¦   ¦   format.py

¦   ¦       ¦   ¦   ¦   format.pyi

¦   ¦       ¦   ¦   ¦   introspect.py

¦   ¦       ¦   ¦   ¦   introspect.pyi

¦   ¦       ¦   ¦   ¦   mixins.py

¦   ¦       ¦   ¦   ¦   mixins.pyi

¦   ¦       ¦   ¦   ¦   npyio.py

¦   ¦       ¦   ¦   ¦   npyio.pyi

¦   ¦       ¦   ¦   ¦   recfunctions.py

¦   ¦       ¦   ¦   ¦   recfunctions.pyi

¦   ¦       ¦   ¦   ¦   scimath.py

¦   ¦       ¦   ¦   ¦   scimath.pyi

¦   ¦       ¦   ¦   ¦   stride\_tricks.py

¦   ¦       ¦   ¦   ¦   stride\_tricks.pyi

¦   ¦       ¦   ¦   ¦   user\_array.py

¦   ¦       ¦   ¦   ¦   user\_array.pyi

¦   ¦       ¦   ¦   ¦   \_arraypad\_impl.py

¦   ¦       ¦   ¦   ¦   \_arraypad\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_arraysetops\_impl.py

¦   ¦       ¦   ¦   ¦   \_arraysetops\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_arrayterator\_impl.py

¦   ¦       ¦   ¦   ¦   \_arrayterator\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_array\_utils\_impl.py

¦   ¦       ¦   ¦   ¦   \_array\_utils\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_datasource.py

¦   ¦       ¦   ¦   ¦   \_datasource.pyi

¦   ¦       ¦   ¦   ¦   \_format\_impl.py

¦   ¦       ¦   ¦   ¦   \_format\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_function\_base\_impl.py

¦   ¦       ¦   ¦   ¦   \_function\_base\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_histograms\_impl.py

¦   ¦       ¦   ¦   ¦   \_histograms\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_index\_tricks\_impl.py

¦   ¦       ¦   ¦   ¦   \_index\_tricks\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_iotools.py

¦   ¦       ¦   ¦   ¦   \_iotools.pyi

¦   ¦       ¦   ¦   ¦   \_nanfunctions\_impl.py

¦   ¦       ¦   ¦   ¦   \_nanfunctions\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_npyio\_impl.py

¦   ¦       ¦   ¦   ¦   \_npyio\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_polynomial\_impl.py

¦   ¦       ¦   ¦   ¦   \_polynomial\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_scimath\_impl.py

¦   ¦       ¦   ¦   ¦   \_scimath\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_shape\_base\_impl.py

¦   ¦       ¦   ¦   ¦   \_shape\_base\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_stride\_tricks\_impl.py

¦   ¦       ¦   ¦   ¦   \_stride\_tricks\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_twodim\_base\_impl.py

¦   ¦       ¦   ¦   ¦   \_twodim\_base\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_type\_check\_impl.py

¦   ¦       ¦   ¦   ¦   \_type\_check\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_ufunclike\_impl.py

¦   ¦       ¦   ¦   ¦   \_ufunclike\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_user\_array\_impl.py

¦   ¦       ¦   ¦   ¦   \_user\_array\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_utils\_impl.py

¦   ¦       ¦   ¦   ¦   \_utils\_impl.pyi

¦   ¦       ¦   ¦   ¦   \_version.py

¦   ¦       ¦   ¦   ¦   \_version.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_arraypad.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arraysetops.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arrayterator.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   test\_format.py

¦   ¦       ¦   ¦   ¦   ¦   test\_function\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_histograms.py

¦   ¦       ¦   ¦   ¦   ¦   test\_index\_tricks.py

¦   ¦       ¦   ¦   ¦   ¦   test\_io.py

¦   ¦       ¦   ¦   ¦   ¦   test\_loadtxt.py

¦   ¦       ¦   ¦   ¦   ¦   test\_mixins.py

¦   ¦       ¦   ¦   ¦   ¦   test\_nanfunctions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_packbits.py

¦   ¦       ¦   ¦   ¦   ¦   test\_polynomial.py

¦   ¦       ¦   ¦   ¦   ¦   test\_recfunctions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   test\_shape\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_stride\_tricks.py

¦   ¦       ¦   ¦   ¦   ¦   test\_twodim\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_type\_check.py

¦   ¦       ¦   ¦   ¦   ¦   test\_ufunclike.py

¦   ¦       ¦   ¦   ¦   ¦   test\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   test\_\_datasource.py

¦   ¦       ¦   ¦   ¦   ¦   test\_\_iotools.py

¦   ¦       ¦   ¦   ¦   ¦   test\_\_version.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---data

¦   ¦       ¦   ¦   ¦   ¦       py2-np0-objarr.npy

¦   ¦       ¦   ¦   ¦   ¦       py2-objarr.npy

¦   ¦       ¦   ¦   ¦   ¦       py2-objarr.npz

¦   ¦       ¦   ¦   ¦   ¦       py3-objarr.npy

¦   ¦       ¦   ¦   ¦   ¦       py3-objarr.npz

¦   ¦       ¦   ¦   ¦   ¦       python3.npy

¦   ¦       ¦   ¦   ¦   ¦       win64python2.npy

¦   ¦       ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_arraypad.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arraysetops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arrayterator.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_format.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_function\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_histograms.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_index\_tricks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_io.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_loadtxt.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_mixins.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_nanfunctions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_packbits.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_polynomial.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_recfunctions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_shape\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_stride\_tricks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_twodim\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_type\_check.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_ufunclike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_\_datasource.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_\_iotools.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_\_version.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           array\_utils.cpython-314.pyc

¦   ¦       ¦   ¦           format.cpython-314.pyc

¦   ¦       ¦   ¦           introspect.cpython-314.pyc

¦   ¦       ¦   ¦           mixins.cpython-314.pyc

¦   ¦       ¦   ¦           npyio.cpython-314.pyc

¦   ¦       ¦   ¦           recfunctions.cpython-314.pyc

¦   ¦       ¦   ¦           scimath.cpython-314.pyc

¦   ¦       ¦   ¦           stride\_tricks.cpython-314.pyc

¦   ¦       ¦   ¦           user\_array.cpython-314.pyc

¦   ¦       ¦   ¦           \_arraypad\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_arraysetops\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_arrayterator\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_array\_utils\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_datasource.cpython-314.pyc

¦   ¦       ¦   ¦           \_format\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_function\_base\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_histograms\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_index\_tricks\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_iotools.cpython-314.pyc

¦   ¦       ¦   ¦           \_nanfunctions\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_npyio\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_polynomial\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_scimath\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_shape\_base\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_stride\_tricks\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_twodim\_base\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_type\_check\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_ufunclike\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_user\_array\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_utils\_impl.cpython-314.pyc

¦   ¦       ¦   ¦           \_version.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---linalg

¦   ¦       ¦   ¦   ¦   lapack\_lite.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   lapack\_lite.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   lapack\_lite.pyi

¦   ¦       ¦   ¦   ¦   \_linalg.py

¦   ¦       ¦   ¦   ¦   \_linalg.pyi

¦   ¦       ¦   ¦   ¦   \_umath\_linalg.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_umath\_linalg.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_umath\_linalg.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_deprecations.py

¦   ¦       ¦   ¦   ¦   ¦   test\_linalg.py

¦   ¦       ¦   ¦   ¦   ¦   test\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_deprecations.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_linalg.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_linalg.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---ma

¦   ¦       ¦   ¦   ¦   API\_CHANGES.txt

¦   ¦       ¦   ¦   ¦   core.py

¦   ¦       ¦   ¦   ¦   core.pyi

¦   ¦       ¦   ¦   ¦   extras.py

¦   ¦       ¦   ¦   ¦   extras.pyi

¦   ¦       ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   mrecords.py

¦   ¦       ¦   ¦   ¦   mrecords.pyi

¦   ¦       ¦   ¦   ¦   README.rst

¦   ¦       ¦   ¦   ¦   testutils.py

¦   ¦       ¦   ¦   ¦   testutils.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_arrayobject.py

¦   ¦       ¦   ¦   ¦   ¦   test\_core.py

¦   ¦       ¦   ¦   ¦   ¦   test\_deprecations.py

¦   ¦       ¦   ¦   ¦   ¦   test\_extras.py

¦   ¦       ¦   ¦   ¦   ¦   test\_mrecords.py

¦   ¦       ¦   ¦   ¦   ¦   test\_old\_ma.py

¦   ¦       ¦   ¦   ¦   ¦   test\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   test\_subclassing.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_arrayobject.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_core.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_deprecations.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_extras.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_mrecords.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_old\_ma.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_subclassing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           core.cpython-314.pyc

¦   ¦       ¦   ¦           extras.cpython-314.pyc

¦   ¦       ¦   ¦           mrecords.cpython-314.pyc

¦   ¦       ¦   ¦           testutils.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---matrixlib

¦   ¦       ¦   ¦   ¦   defmatrix.py

¦   ¦       ¦   ¦   ¦   defmatrix.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_defmatrix.py

¦   ¦       ¦   ¦   ¦   ¦   test\_interaction.py

¦   ¦       ¦   ¦   ¦   ¦   test\_masked\_matrix.py

¦   ¦       ¦   ¦   ¦   ¦   test\_matrix\_linalg.py

¦   ¦       ¦   ¦   ¦   ¦   test\_multiarray.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numeric.py

¦   ¦       ¦   ¦   ¦   ¦   test\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_defmatrix.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_interaction.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_masked\_matrix.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_matrix\_linalg.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_multiarray.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           defmatrix.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---polynomial

¦   ¦       ¦   ¦   ¦   chebyshev.py

¦   ¦       ¦   ¦   ¦   chebyshev.pyi

¦   ¦       ¦   ¦   ¦   hermite.py

¦   ¦       ¦   ¦   ¦   hermite.pyi

¦   ¦       ¦   ¦   ¦   hermite\_e.py

¦   ¦       ¦   ¦   ¦   hermite\_e.pyi

¦   ¦       ¦   ¦   ¦   laguerre.py

¦   ¦       ¦   ¦   ¦   laguerre.pyi

¦   ¦       ¦   ¦   ¦   legendre.py

¦   ¦       ¦   ¦   ¦   legendre.pyi

¦   ¦       ¦   ¦   ¦   polynomial.py

¦   ¦       ¦   ¦   ¦   polynomial.pyi

¦   ¦       ¦   ¦   ¦   polyutils.py

¦   ¦       ¦   ¦   ¦   polyutils.pyi

¦   ¦       ¦   ¦   ¦   \_polybase.py

¦   ¦       ¦   ¦   ¦   \_polybase.pyi

¦   ¦       ¦   ¦   ¦   \_polytypes.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_chebyshev.py

¦   ¦       ¦   ¦   ¦   ¦   test\_classes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_hermite.py

¦   ¦       ¦   ¦   ¦   ¦   test\_hermite\_e.py

¦   ¦       ¦   ¦   ¦   ¦   test\_laguerre.py

¦   ¦       ¦   ¦   ¦   ¦   test\_legendre.py

¦   ¦       ¦   ¦   ¦   ¦   test\_polynomial.py

¦   ¦       ¦   ¦   ¦   ¦   test\_polyutils.py

¦   ¦       ¦   ¦   ¦   ¦   test\_printing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_symbol.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_chebyshev.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_classes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_hermite.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_hermite\_e.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_laguerre.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_legendre.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_polynomial.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_polyutils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_printing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_symbol.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           chebyshev.cpython-314.pyc

¦   ¦       ¦   ¦           hermite.cpython-314.pyc

¦   ¦       ¦   ¦           hermite\_e.cpython-314.pyc

¦   ¦       ¦   ¦           laguerre.cpython-314.pyc

¦   ¦       ¦   ¦           legendre.cpython-314.pyc

¦   ¦       ¦   ¦           polynomial.cpython-314.pyc

¦   ¦       ¦   ¦           polyutils.cpython-314.pyc

¦   ¦       ¦   ¦           \_polybase.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---random

¦   ¦       ¦   ¦   ¦   bit\_generator.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   bit\_generator.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   bit\_generator.pxd

¦   ¦       ¦   ¦   ¦   bit\_generator.pyi

¦   ¦       ¦   ¦   ¦   c\_distributions.pxd

¦   ¦       ¦   ¦   ¦   LICENSE.md

¦   ¦       ¦   ¦   ¦   mtrand.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   mtrand.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   mtrand.pyi

¦   ¦       ¦   ¦   ¦   \_bounded\_integers.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_bounded\_integers.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_bounded\_integers.pxd

¦   ¦       ¦   ¦   ¦   \_bounded\_integers.pyi

¦   ¦       ¦   ¦   ¦   \_common.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_common.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_common.pxd

¦   ¦       ¦   ¦   ¦   \_common.pyi

¦   ¦       ¦   ¦   ¦   \_generator.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_generator.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_generator.pyi

¦   ¦       ¦   ¦   ¦   \_mt19937.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_mt19937.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_mt19937.pyi

¦   ¦       ¦   ¦   ¦   \_pcg64.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_pcg64.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_pcg64.pyi

¦   ¦       ¦   ¦   ¦   \_philox.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_philox.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_philox.pyi

¦   ¦       ¦   ¦   ¦   \_pickle.py

¦   ¦       ¦   ¦   ¦   \_pickle.pyi

¦   ¦       ¦   ¦   ¦   \_sfc64.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_sfc64.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_sfc64.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pxd

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---lib

¦   ¦       ¦   ¦   ¦       npyrandom.lib

¦   ¦       ¦   ¦   ¦       

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_direct.py

¦   ¦       ¦   ¦   ¦   ¦   test\_extending.py

¦   ¦       ¦   ¦   ¦   ¦   test\_generator\_mt19937.py

¦   ¦       ¦   ¦   ¦   ¦   test\_generator\_mt19937\_regressions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_random.py

¦   ¦       ¦   ¦   ¦   ¦   test\_randomstate.py

¦   ¦       ¦   ¦   ¦   ¦   test\_randomstate\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   test\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   test\_seed\_sequence.py

¦   ¦       ¦   ¦   ¦   ¦   test\_smoke.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---data

¦   ¦       ¦   ¦   ¦   ¦   ¦   generator\_pcg64\_np121.pkl.gz

¦   ¦       ¦   ¦   ¦   ¦   ¦   generator\_pcg64\_np126.pkl.gz

¦   ¦       ¦   ¦   ¦   ¦   ¦   mt19937-testset-1.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   mt19937-testset-2.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64-testset-1.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64-testset-2.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64dxsm-testset-1.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64dxsm-testset-2.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   philox-testset-1.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   philox-testset-2.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   sfc64-testset-1.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   sfc64-testset-2.csv

¦   ¦       ¦   ¦   ¦   ¦   ¦   sfc64\_np126.pkl.gz

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_direct.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_extending.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_generator\_mt19937.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_generator\_mt19937\_regressions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_random.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_randomstate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_randomstate\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_seed\_sequence.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_smoke.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_examples

¦   ¦       ¦   ¦   ¦   +---cffi

¦   ¦       ¦   ¦   ¦   ¦   ¦   extending.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   parse.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           extending.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           parse.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---cython

¦   ¦       ¦   ¦   ¦   ¦       extending.pyx

¦   ¦       ¦   ¦   ¦   ¦       extending\_distributions.pyx

¦   ¦       ¦   ¦   ¦   ¦       meson.build

¦   ¦       ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   +---numba

¦   ¦       ¦   ¦   ¦       ¦   extending.py

¦   ¦       ¦   ¦   ¦       ¦   extending\_distributions.py

¦   ¦       ¦   ¦   ¦       ¦   

¦   ¦       ¦   ¦   ¦       +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦               extending.cpython-314.pyc

¦   ¦       ¦   ¦   ¦               extending\_distributions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦               

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_pickle.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---rec

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---strings

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---testing

¦   ¦       ¦   ¦   ¦   overrides.py

¦   ¦       ¦   ¦   ¦   overrides.pyi

¦   ¦       ¦   ¦   ¦   print\_coercion\_tables.py

¦   ¦       ¦   ¦   ¦   print\_coercion\_tables.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_private

¦   ¦       ¦   ¦   ¦   ¦   extbuild.py

¦   ¦       ¦   ¦   ¦   ¦   extbuild.pyi

¦   ¦       ¦   ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   ¦   utils.pyi

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           extbuild.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           overrides.cpython-314.pyc

¦   ¦       ¦   ¦           print\_coercion\_tables.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---tests

¦   ¦       ¦   ¦   ¦   test\_configtool.py

¦   ¦       ¦   ¦   ¦   test\_ctypeslib.py

¦   ¦       ¦   ¦   ¦   test\_lazyloading.py

¦   ¦       ¦   ¦   ¦   test\_matlib.py

¦   ¦       ¦   ¦   ¦   test\_numpy\_config.py

¦   ¦       ¦   ¦   ¦   test\_numpy\_version.py

¦   ¦       ¦   ¦   ¦   test\_public\_api.py

¦   ¦       ¦   ¦   ¦   test\_reloading.py

¦   ¦       ¦   ¦   ¦   test\_scripts.py

¦   ¦       ¦   ¦   ¦   test\_warnings.py

¦   ¦       ¦   ¦   ¦   test\_\_all\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           test\_configtool.cpython-314.pyc

¦   ¦       ¦   ¦           test\_ctypeslib.cpython-314.pyc

¦   ¦       ¦   ¦           test\_lazyloading.cpython-314.pyc

¦   ¦       ¦   ¦           test\_matlib.cpython-314.pyc

¦   ¦       ¦   ¦           test\_numpy\_config.cpython-314.pyc

¦   ¦       ¦   ¦           test\_numpy\_version.cpython-314.pyc

¦   ¦       ¦   ¦           test\_public\_api.cpython-314.pyc

¦   ¦       ¦   ¦           test\_reloading.cpython-314.pyc

¦   ¦       ¦   ¦           test\_scripts.cpython-314.pyc

¦   ¦       ¦   ¦           test\_warnings.cpython-314.pyc

¦   ¦       ¦   ¦           test\_\_all\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---typing

¦   ¦       ¦   ¦   ¦   mypy\_plugin.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_isfile.py

¦   ¦       ¦   ¦   ¦   ¦   test\_runtime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_typing.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---data

¦   ¦       ¦   ¦   ¦   ¦   ¦   mypy.ini

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---fail

¦   ¦       ¦   ¦   ¦   ¦   ¦       arithmetic.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       arrayprint.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       arrayterator.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       array\_constructors.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       array\_like.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       array\_pad.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       bitwise\_ops.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       char.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       chararray.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       comparisons.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       constants.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       datasource.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       dtype.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       einsumfunc.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       flatiter.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       fromnumeric.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       histograms.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       index\_tricks.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       lib\_function\_base.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       lib\_polynomial.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       lib\_utils.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       lib\_version.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       linalg.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       ma.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       memmap.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       modules.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       multiarray.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       ndarray.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       ndarray\_misc.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       nditer.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       nested\_sequence.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       npyio.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       numerictypes.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       random.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       rec.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       scalars.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       shape.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       shape\_base.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       stride\_tricks.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       strings.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       testing.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       twodim\_base.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       type\_check.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       ufunclike.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       ufuncs.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       ufunc\_config.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       warnings\_and\_errors.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---misc

¦   ¦       ¦   ¦   ¦   ¦   ¦       extended\_precision.pyi

¦   ¦       ¦   ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   ¦   +---pass

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   arrayprint.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   arrayterator.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   array\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   array\_like.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   bitwise\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   comparisons.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   dtype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   einsumfunc.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   flatiter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   fromnumeric.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   index\_tricks.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   lib\_user\_array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   lib\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   lib\_version.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   literal.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ma.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   mod.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   modules.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   multiarray.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ndarray\_conversion.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ndarray\_misc.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ndarray\_shape\_manipulation.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   nditer.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   numeric.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   numerictypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   random.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   recfunctions.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   scalars.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   shape.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   simple.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ufunclike.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ufuncs.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ufunc\_config.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   warnings\_and\_errors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           arrayprint.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           arrayterator.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           array\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           array\_like.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           bitwise\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           comparisons.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           dtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           einsumfunc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           flatiter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           fromnumeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           index\_tricks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           lib\_user\_array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           lib\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           lib\_version.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           literal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           ma.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           mod.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           modules.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           multiarray.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           ndarray\_conversion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           ndarray\_misc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           ndarray\_shape\_manipulation.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           nditer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           numerictypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           random.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           recfunctions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           scalars.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           shape.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           simple.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           ufunclike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           ufuncs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           ufunc\_config.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           warnings\_and\_errors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---reveal

¦   ¦       ¦   ¦   ¦   ¦           arithmetic.pyi

¦   ¦       ¦   ¦   ¦   ¦           arraypad.pyi

¦   ¦       ¦   ¦   ¦   ¦           arrayprint.pyi

¦   ¦       ¦   ¦   ¦   ¦           arraysetops.pyi

¦   ¦       ¦   ¦   ¦   ¦           arrayterator.pyi

¦   ¦       ¦   ¦   ¦   ¦           array\_api\_info.pyi

¦   ¦       ¦   ¦   ¦   ¦           array\_constructors.pyi

¦   ¦       ¦   ¦   ¦   ¦           bitwise\_ops.pyi

¦   ¦       ¦   ¦   ¦   ¦           char.pyi

¦   ¦       ¦   ¦   ¦   ¦           chararray.pyi

¦   ¦       ¦   ¦   ¦   ¦           comparisons.pyi

¦   ¦       ¦   ¦   ¦   ¦           constants.pyi

¦   ¦       ¦   ¦   ¦   ¦           ctypeslib.pyi

¦   ¦       ¦   ¦   ¦   ¦           datasource.pyi

¦   ¦       ¦   ¦   ¦   ¦           dtype.pyi

¦   ¦       ¦   ¦   ¦   ¦           einsumfunc.pyi

¦   ¦       ¦   ¦   ¦   ¦           emath.pyi

¦   ¦       ¦   ¦   ¦   ¦           fft.pyi

¦   ¦       ¦   ¦   ¦   ¦           flatiter.pyi

¦   ¦       ¦   ¦   ¦   ¦           fromnumeric.pyi

¦   ¦       ¦   ¦   ¦   ¦           getlimits.pyi

¦   ¦       ¦   ¦   ¦   ¦           histograms.pyi

¦   ¦       ¦   ¦   ¦   ¦           index\_tricks.pyi

¦   ¦       ¦   ¦   ¦   ¦           lib\_function\_base.pyi

¦   ¦       ¦   ¦   ¦   ¦           lib\_polynomial.pyi

¦   ¦       ¦   ¦   ¦   ¦           lib\_utils.pyi

¦   ¦       ¦   ¦   ¦   ¦           lib\_version.pyi

¦   ¦       ¦   ¦   ¦   ¦           linalg.pyi

¦   ¦       ¦   ¦   ¦   ¦           ma.pyi

¦   ¦       ¦   ¦   ¦   ¦           matrix.pyi

¦   ¦       ¦   ¦   ¦   ¦           memmap.pyi

¦   ¦       ¦   ¦   ¦   ¦           mod.pyi

¦   ¦       ¦   ¦   ¦   ¦           modules.pyi

¦   ¦       ¦   ¦   ¦   ¦           multiarray.pyi

¦   ¦       ¦   ¦   ¦   ¦           nbit\_base\_example.pyi

¦   ¦       ¦   ¦   ¦   ¦           ndarray\_assignability.pyi

¦   ¦       ¦   ¦   ¦   ¦           ndarray\_conversion.pyi

¦   ¦       ¦   ¦   ¦   ¦           ndarray\_misc.pyi

¦   ¦       ¦   ¦   ¦   ¦           ndarray\_shape\_manipulation.pyi

¦   ¦       ¦   ¦   ¦   ¦           nditer.pyi

¦   ¦       ¦   ¦   ¦   ¦           nested\_sequence.pyi

¦   ¦       ¦   ¦   ¦   ¦           npyio.pyi

¦   ¦       ¦   ¦   ¦   ¦           numeric.pyi

¦   ¦       ¦   ¦   ¦   ¦           numerictypes.pyi

¦   ¦       ¦   ¦   ¦   ¦           polynomial\_polybase.pyi

¦   ¦       ¦   ¦   ¦   ¦           polynomial\_polyutils.pyi

¦   ¦       ¦   ¦   ¦   ¦           polynomial\_series.pyi

¦   ¦       ¦   ¦   ¦   ¦           random.pyi

¦   ¦       ¦   ¦   ¦   ¦           rec.pyi

¦   ¦       ¦   ¦   ¦   ¦           scalars.pyi

¦   ¦       ¦   ¦   ¦   ¦           shape.pyi

¦   ¦       ¦   ¦   ¦   ¦           shape\_base.pyi

¦   ¦       ¦   ¦   ¦   ¦           stride\_tricks.pyi

¦   ¦       ¦   ¦   ¦   ¦           strings.pyi

¦   ¦       ¦   ¦   ¦   ¦           testing.pyi

¦   ¦       ¦   ¦   ¦   ¦           twodim\_base.pyi

¦   ¦       ¦   ¦   ¦   ¦           type\_check.pyi

¦   ¦       ¦   ¦   ¦   ¦           ufunclike.pyi

¦   ¦       ¦   ¦   ¦   ¦           ufuncs.pyi

¦   ¦       ¦   ¦   ¦   ¦           ufunc\_config.pyi

¦   ¦       ¦   ¦   ¦   ¦           warnings\_and\_errors.pyi

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_isfile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_runtime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_typing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           mypy\_plugin.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_core

¦   ¦       ¦   ¦   ¦   arrayprint.py

¦   ¦       ¦   ¦   ¦   arrayprint.pyi

¦   ¦       ¦   ¦   ¦   cversions.py

¦   ¦       ¦   ¦   ¦   defchararray.py

¦   ¦       ¦   ¦   ¦   defchararray.pyi

¦   ¦       ¦   ¦   ¦   einsumfunc.py

¦   ¦       ¦   ¦   ¦   einsumfunc.pyi

¦   ¦       ¦   ¦   ¦   fromnumeric.py

¦   ¦       ¦   ¦   ¦   fromnumeric.pyi

¦   ¦       ¦   ¦   ¦   function\_base.py

¦   ¦       ¦   ¦   ¦   function\_base.pyi

¦   ¦       ¦   ¦   ¦   getlimits.py

¦   ¦       ¦   ¦   ¦   getlimits.pyi

¦   ¦       ¦   ¦   ¦   memmap.py

¦   ¦       ¦   ¦   ¦   memmap.pyi

¦   ¦       ¦   ¦   ¦   multiarray.py

¦   ¦       ¦   ¦   ¦   multiarray.pyi

¦   ¦       ¦   ¦   ¦   numeric.py

¦   ¦       ¦   ¦   ¦   numeric.pyi

¦   ¦       ¦   ¦   ¦   numerictypes.py

¦   ¦       ¦   ¦   ¦   numerictypes.pyi

¦   ¦       ¦   ¦   ¦   overrides.py

¦   ¦       ¦   ¦   ¦   overrides.pyi

¦   ¦       ¦   ¦   ¦   printoptions.py

¦   ¦       ¦   ¦   ¦   printoptions.pyi

¦   ¦       ¦   ¦   ¦   records.py

¦   ¦       ¦   ¦   ¦   records.pyi

¦   ¦       ¦   ¦   ¦   shape\_base.py

¦   ¦       ¦   ¦   ¦   shape\_base.pyi

¦   ¦       ¦   ¦   ¦   strings.py

¦   ¦       ¦   ¦   ¦   strings.pyi

¦   ¦       ¦   ¦   ¦   umath.py

¦   ¦       ¦   ¦   ¦   umath.pyi

¦   ¦       ¦   ¦   ¦   \_add\_newdocs.py

¦   ¦       ¦   ¦   ¦   \_add\_newdocs.pyi

¦   ¦       ¦   ¦   ¦   \_add\_newdocs\_scalars.py

¦   ¦       ¦   ¦   ¦   \_add\_newdocs\_scalars.pyi

¦   ¦       ¦   ¦   ¦   \_asarray.py

¦   ¦       ¦   ¦   ¦   \_asarray.pyi

¦   ¦       ¦   ¦   ¦   \_dtype.py

¦   ¦       ¦   ¦   ¦   \_dtype.pyi

¦   ¦       ¦   ¦   ¦   \_dtype\_ctypes.py

¦   ¦       ¦   ¦   ¦   \_dtype\_ctypes.pyi

¦   ¦       ¦   ¦   ¦   \_exceptions.py

¦   ¦       ¦   ¦   ¦   \_exceptions.pyi

¦   ¦       ¦   ¦   ¦   \_internal.py

¦   ¦       ¦   ¦   ¦   \_internal.pyi

¦   ¦       ¦   ¦   ¦   \_methods.py

¦   ¦       ¦   ¦   ¦   \_methods.pyi

¦   ¦       ¦   ¦   ¦   \_multiarray\_tests.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_multiarray\_tests.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_multiarray\_umath.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_multiarray\_umath.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_operand\_flag\_tests.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_operand\_flag\_tests.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_rational\_tests.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_rational\_tests.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_simd.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_simd.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_simd.pyi

¦   ¦       ¦   ¦   ¦   \_string\_helpers.py

¦   ¦       ¦   ¦   ¦   \_string\_helpers.pyi

¦   ¦       ¦   ¦   ¦   \_struct\_ufunc\_tests.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_struct\_ufunc\_tests.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_type\_aliases.py

¦   ¦       ¦   ¦   ¦   \_type\_aliases.pyi

¦   ¦       ¦   ¦   ¦   \_ufunc\_config.py

¦   ¦       ¦   ¦   ¦   \_ufunc\_config.pyi

¦   ¦       ¦   ¦   ¦   \_umath\_tests.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_umath\_tests.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_umath\_tests.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---include

¦   ¦       ¦   ¦   ¦   +---numpy

¦   ¦       ¦   ¦   ¦       ¦   arrayobject.h

¦   ¦       ¦   ¦   ¦       ¦   arrayscalars.h

¦   ¦       ¦   ¦   ¦       ¦   dtype\_api.h

¦   ¦       ¦   ¦   ¦       ¦   halffloat.h

¦   ¦       ¦   ¦   ¦       ¦   ndarrayobject.h

¦   ¦       ¦   ¦   ¦       ¦   ndarraytypes.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_2\_compat.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_2\_complexcompat.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_3kcompat.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_common.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_cpu.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_endian.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_math.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_no\_deprecated\_api.h

¦   ¦       ¦   ¦   ¦       ¦   npy\_os.h

¦   ¦       ¦   ¦   ¦       ¦   numpyconfig.h

¦   ¦       ¦   ¦   ¦       ¦   ufuncobject.h

¦   ¦       ¦   ¦   ¦       ¦   utils.h

¦   ¦       ¦   ¦   ¦       ¦   \_neighborhood\_iterator\_imp.h

¦   ¦       ¦   ¦   ¦       ¦   \_numpyconfig.h

¦   ¦       ¦   ¦   ¦       ¦   \_public\_dtype\_api\_table.h

¦   ¦       ¦   ¦   ¦       ¦   \_\_multiarray\_api.c

¦   ¦       ¦   ¦   ¦       ¦   \_\_multiarray\_api.h

¦   ¦       ¦   ¦   ¦       ¦   \_\_ufunc\_api.c

¦   ¦       ¦   ¦   ¦       ¦   \_\_ufunc\_api.h

¦   ¦       ¦   ¦   ¦       ¦   

¦   ¦       ¦   ¦   ¦       +---random

¦   ¦       ¦   ¦   ¦               bitgen.h

¦   ¦       ¦   ¦   ¦               distributions.h

¦   ¦       ¦   ¦   ¦               libdivide.h

¦   ¦       ¦   ¦   ¦               LICENSE.txt

¦   ¦       ¦   ¦   ¦               

¦   ¦       ¦   ¦   +---lib

¦   ¦       ¦   ¦   ¦   ¦   npymath.lib

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---pkgconfig

¦   ¦       ¦   ¦   ¦           numpy.pc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   test\_abc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_argparse.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arraymethod.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arrayobject.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arrayprint.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array\_api\_info.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array\_coercion.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array\_interface.py

¦   ¦       ¦   ¦   ¦   ¦   test\_casting\_floatingpoint\_errors.py

¦   ¦       ¦   ¦   ¦   ¦   test\_casting\_unittests.py

¦   ¦       ¦   ¦   ¦   ¦   test\_conversion\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cpu\_dispatcher.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cpu\_features.py

¦   ¦       ¦   ¦   ¦   ¦   test\_custom\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cython.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_defchararray.py

¦   ¦       ¦   ¦   ¦   ¦   test\_deprecations.py

¦   ¦       ¦   ¦   ¦   ¦   test\_dlpack.py

¦   ¦       ¦   ¦   ¦   ¦   test\_dtype.py

¦   ¦       ¦   ¦   ¦   ¦   test\_einsum.py

¦   ¦       ¦   ¦   ¦   ¦   test\_errstate.py

¦   ¦       ¦   ¦   ¦   ¦   test\_extint128.py

¦   ¦       ¦   ¦   ¦   ¦   test\_finfo.py

¦   ¦       ¦   ¦   ¦   ¦   test\_function\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_getlimits.py

¦   ¦       ¦   ¦   ¦   ¦   test\_half.py

¦   ¦       ¦   ¦   ¦   ¦   test\_hashtable.py

¦   ¦       ¦   ¦   ¦   ¦   test\_indexerrors.py

¦   ¦       ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_item\_selection.py

¦   ¦       ¦   ¦   ¦   ¦   test\_limited\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_longdouble.py

¦   ¦       ¦   ¦   ¦   ¦   test\_memmap.py

¦   ¦       ¦   ¦   ¦   ¦   test\_mem\_overlap.py

¦   ¦       ¦   ¦   ¦   ¦   test\_mem\_policy.py

¦   ¦       ¦   ¦   ¦   ¦   test\_multiarray.py

¦   ¦       ¦   ¦   ¦   ¦   test\_multiprocessing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_multithreading.py

¦   ¦       ¦   ¦   ¦   ¦   test\_nditer.py

¦   ¦       ¦   ¦   ¦   ¦   test\_nep50\_promotions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numeric.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numerictypes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_overrides.py

¦   ¦       ¦   ¦   ¦   ¦   test\_print.py

¦   ¦       ¦   ¦   ¦   ¦   test\_protocols.py

¦   ¦       ¦   ¦   ¦   ¦   test\_records.py

¦   ¦       ¦   ¦   ¦   ¦   test\_regression.py

¦   ¦       ¦   ¦   ¦   ¦   test\_scalarbuffer.py

¦   ¦       ¦   ¦   ¦   ¦   test\_scalarinherit.py

¦   ¦       ¦   ¦   ¦   ¦   test\_scalarmath.py

¦   ¦       ¦   ¦   ¦   ¦   test\_scalarprint.py

¦   ¦       ¦   ¦   ¦   ¦   test\_scalar\_ctors.py

¦   ¦       ¦   ¦   ¦   ¦   test\_scalar\_methods.py

¦   ¦       ¦   ¦   ¦   ¦   test\_shape\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_simd.py

¦   ¦       ¦   ¦   ¦   ¦   test\_simd\_module.py

¦   ¦       ¦   ¦   ¦   ¦   test\_stringdtype.py

¦   ¦       ¦   ¦   ¦   ¦   test\_strings.py

¦   ¦       ¦   ¦   ¦   ¦   test\_ufunc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_umath.py

¦   ¦       ¦   ¦   ¦   ¦   test\_umath\_accuracy.py

¦   ¦       ¦   ¦   ¦   ¦   test\_umath\_complex.py

¦   ¦       ¦   ¦   ¦   ¦   test\_unicode.py

¦   ¦       ¦   ¦   ¦   ¦   test\_\_exceptions.py

¦   ¦       ¦   ¦   ¦   ¦   \_locales.py

¦   ¦       ¦   ¦   ¦   ¦   \_natype.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---data

¦   ¦       ¦   ¦   ¦   ¦       astype\_copy.pkl

¦   ¦       ¦   ¦   ¦   ¦       generate\_umath\_validation\_data.cpp

¦   ¦       ¦   ¦   ¦   ¦       recarray\_from\_file.fits

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arccos.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arccosh.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arcsin.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arcsinh.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arctan.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arctanh.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-cbrt.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-cos.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-cosh.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-exp.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-exp2.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-expm1.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log10.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log1p.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log2.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-README.txt

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-sin.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-sinh.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-tan.csv

¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-tanh.csv

¦   ¦       ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   +---examples

¦   ¦       ¦   ¦   ¦   ¦   +---cython

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   checks.pyx

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   meson.build

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   setup.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           setup.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---limited\_api

¦   ¦       ¦   ¦   ¦   ¦       ¦   limited\_api.c

¦   ¦       ¦   ¦   ¦   ¦       ¦   limited\_api\_cython.pyx

¦   ¦       ¦   ¦   ¦   ¦       ¦   meson.build

¦   ¦       ¦   ¦   ¦   ¦       ¦   setup.py

¦   ¦       ¦   ¦   ¦   ¦       ¦   

¦   ¦       ¦   ¦   ¦   ¦       +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦               setup.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦               

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_abc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_argparse.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arraymethod.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arrayobject.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arrayprint.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array\_api\_info.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array\_coercion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array\_interface.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_casting\_floatingpoint\_errors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_casting\_unittests.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_conversion\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cpu\_dispatcher.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cpu\_features.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_custom\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cython.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_defchararray.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_deprecations.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_dlpack.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_dtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_einsum.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_errstate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_extint128.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_finfo.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_function\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_getlimits.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_half.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_hashtable.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_indexerrors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_item\_selection.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_limited\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_longdouble.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_memmap.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_mem\_overlap.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_mem\_policy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_multiarray.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_multiprocessing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_multithreading.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_nditer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_nep50\_promotions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numerictypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_overrides.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_print.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_protocols.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_records.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_regression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_scalarbuffer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_scalarinherit.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_scalarmath.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_scalarprint.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_scalar\_ctors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_scalar\_methods.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_shape\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_simd.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_simd\_module.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_stringdtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_strings.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_ufunc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_umath.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_umath\_accuracy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_umath\_complex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_unicode.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_\_exceptions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_locales.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_natype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           arrayprint.cpython-314.pyc

¦   ¦       ¦   ¦           cversions.cpython-314.pyc

¦   ¦       ¦   ¦           defchararray.cpython-314.pyc

¦   ¦       ¦   ¦           einsumfunc.cpython-314.pyc

¦   ¦       ¦   ¦           fromnumeric.cpython-314.pyc

¦   ¦       ¦   ¦           function\_base.cpython-314.pyc

¦   ¦       ¦   ¦           getlimits.cpython-314.pyc

¦   ¦       ¦   ¦           memmap.cpython-314.pyc

¦   ¦       ¦   ¦           multiarray.cpython-314.pyc

¦   ¦       ¦   ¦           numeric.cpython-314.pyc

¦   ¦       ¦   ¦           numerictypes.cpython-314.pyc

¦   ¦       ¦   ¦           overrides.cpython-314.pyc

¦   ¦       ¦   ¦           printoptions.cpython-314.pyc

¦   ¦       ¦   ¦           records.cpython-314.pyc

¦   ¦       ¦   ¦           shape\_base.cpython-314.pyc

¦   ¦       ¦   ¦           strings.cpython-314.pyc

¦   ¦       ¦   ¦           umath.cpython-314.pyc

¦   ¦       ¦   ¦           \_add\_newdocs.cpython-314.pyc

¦   ¦       ¦   ¦           \_add\_newdocs\_scalars.cpython-314.pyc

¦   ¦       ¦   ¦           \_asarray.cpython-314.pyc

¦   ¦       ¦   ¦           \_dtype.cpython-314.pyc

¦   ¦       ¦   ¦           \_dtype\_ctypes.cpython-314.pyc

¦   ¦       ¦   ¦           \_exceptions.cpython-314.pyc

¦   ¦       ¦   ¦           \_internal.cpython-314.pyc

¦   ¦       ¦   ¦           \_methods.cpython-314.pyc

¦   ¦       ¦   ¦           \_string\_helpers.cpython-314.pyc

¦   ¦       ¦   ¦           \_type\_aliases.cpython-314.pyc

¦   ¦       ¦   ¦           \_ufunc\_config.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_pyinstaller

¦   ¦       ¦   ¦   ¦   hook-numpy.py

¦   ¦       ¦   ¦   ¦   hook-numpy.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tests

¦   ¦       ¦   ¦   ¦   ¦   pyinstaller-smoke.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pyinstaller.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           pyinstaller-smoke.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pyinstaller.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           hook-numpy.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_typing

¦   ¦       ¦   ¦   ¦   \_add\_docstring.py

¦   ¦       ¦   ¦   ¦   \_array\_like.py

¦   ¦       ¦   ¦   ¦   \_char\_codes.py

¦   ¦       ¦   ¦   ¦   \_dtype\_like.py

¦   ¦       ¦   ¦   ¦   \_extended\_precision.py

¦   ¦       ¦   ¦   ¦   \_nbit.py

¦   ¦       ¦   ¦   ¦   \_nbit\_base.py

¦   ¦       ¦   ¦   ¦   \_nbit\_base.pyi

¦   ¦       ¦   ¦   ¦   \_nested\_sequence.py

¦   ¦       ¦   ¦   ¦   \_scalars.py

¦   ¦       ¦   ¦   ¦   \_shape.py

¦   ¦       ¦   ¦   ¦   \_ufunc.py

¦   ¦       ¦   ¦   ¦   \_ufunc.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_add\_docstring.cpython-314.pyc

¦   ¦       ¦   ¦           \_array\_like.cpython-314.pyc

¦   ¦       ¦   ¦           \_char\_codes.cpython-314.pyc

¦   ¦       ¦   ¦           \_dtype\_like.cpython-314.pyc

¦   ¦       ¦   ¦           \_extended\_precision.cpython-314.pyc

¦   ¦       ¦   ¦           \_nbit.cpython-314.pyc

¦   ¦       ¦   ¦           \_nbit\_base.cpython-314.pyc

¦   ¦       ¦   ¦           \_nested\_sequence.cpython-314.pyc

¦   ¦       ¦   ¦           \_scalars.cpython-314.pyc

¦   ¦       ¦   ¦           \_shape.cpython-314.pyc

¦   ¦       ¦   ¦           \_ufunc.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_utils

¦   ¦       ¦   ¦   ¦   \_conversions.py

¦   ¦       ¦   ¦   ¦   \_conversions.pyi

¦   ¦       ¦   ¦   ¦   \_inspect.py

¦   ¦       ¦   ¦   ¦   \_inspect.pyi

¦   ¦       ¦   ¦   ¦   \_pep440.py

¦   ¦       ¦   ¦   ¦   \_pep440.pyi

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.pyi

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_conversions.cpython-314.pyc

¦   ¦       ¦   ¦           \_inspect.cpython-314.pyc

¦   ¦       ¦   ¦           \_pep440.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           conftest.cpython-314.pyc

¦   ¦       ¦           dtypes.cpython-314.pyc

¦   ¦       ¦           exceptions.cpython-314.pyc

¦   ¦       ¦           matlib.cpython-314.pyc

¦   ¦       ¦           version.cpython-314.pyc

¦   ¦       ¦           \_array\_api\_info.cpython-314.pyc

¦   ¦       ¦           \_configtool.cpython-314.pyc

¦   ¦       ¦           \_distributor\_init.cpython-314.pyc

¦   ¦       ¦           \_expired\_attrs\_2\_0.cpython-314.pyc

¦   ¦       ¦           \_globals.cpython-314.pyc

¦   ¦       ¦           \_pytesttester.cpython-314.pyc

¦   ¦       ¦           \_\_config\_\_.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---numpy-2.5.3.dist-info

¦   ¦       ¦   ¦   DELVEWHEEL

¦   ¦       ¦   ¦   entry\_points.txt

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   REQUESTED

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦       ¦   LICENSE.txt

¦   ¦       ¦       ¦   

¦   ¦       ¦       +---numpy

¦   ¦       ¦           +---fft

¦   ¦       ¦           ¦   +---pocketfft

¦   ¦       ¦           ¦           LICENSE.md

¦   ¦       ¦           ¦           

¦   ¦       ¦           +---linalg

¦   ¦       ¦           ¦   +---lapack\_lite

¦   ¦       ¦           ¦           LICENSE.txt

¦   ¦       ¦           ¦           

¦   ¦       ¦           +---ma

¦   ¦       ¦           ¦       LICENSE

¦   ¦       ¦           ¦       

¦   ¦       ¦           +---random

¦   ¦       ¦           ¦   ¦   LICENSE.md

¦   ¦       ¦           ¦   ¦   

¦   ¦       ¦           ¦   +---src

¦   ¦       ¦           ¦       +---distributions

¦   ¦       ¦           ¦       ¦       LICENSE.md

¦   ¦       ¦           ¦       ¦       

¦   ¦       ¦           ¦       +---mt19937

¦   ¦       ¦           ¦       ¦       LICENSE.md

¦   ¦       ¦           ¦       ¦       

¦   ¦       ¦           ¦       +---pcg64

¦   ¦       ¦           ¦       ¦       LICENSE.md

¦   ¦       ¦           ¦       ¦       

¦   ¦       ¦           ¦       +---philox

¦   ¦       ¦           ¦       ¦       LICENSE.md

¦   ¦       ¦           ¦       ¦       

¦   ¦       ¦           ¦       +---sfc64

¦   ¦       ¦           ¦       ¦       LICENSE.md

¦   ¦       ¦           ¦       ¦       

¦   ¦       ¦           ¦       +---splitmix64

¦   ¦       ¦           ¦               LICENSE.md

¦   ¦       ¦           ¦               

¦   ¦       ¦           +---\_core

¦   ¦       ¦               +---include

¦   ¦       ¦               ¦   +---numpy

¦   ¦       ¦               ¦       +---libdivide

¦   ¦       ¦               ¦               LICENSE.txt

¦   ¦       ¦               ¦               

¦   ¦       ¦               +---src

¦   ¦       ¦                   +---common

¦   ¦       ¦                   ¦   +---pythoncapi-compat

¦   ¦       ¦                   ¦           COPYING

¦   ¦       ¦                   ¦           

¦   ¦       ¦                   +---highway

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---multiarray

¦   ¦       ¦                   ¦       dragon4\_LICENSE.txt

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---npysort

¦   ¦       ¦                   ¦   +---x86-simd-sort

¦   ¦       ¦                   ¦           LICENSE.md

¦   ¦       ¦                   ¦           

¦   ¦       ¦                   +---umath

¦   ¦       ¦                       +---svml

¦   ¦       ¦                               LICENSE

¦   ¦       ¦                               

¦   ¦       +---numpy.libs

¦   ¦       ¦       libscipy\_openblas64\_-ed4f167a5330424524f45258e7ca2c8d.dll

¦   ¦       ¦       msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll

¦   ¦       ¦       

¦   ¦       +---pandas

¦   ¦       ¦   ¦   conftest.py

¦   ¦       ¦   ¦   pyproject.toml

¦   ¦       ¦   ¦   testing.py

¦   ¦       ¦   ¦   \_typing.py

¦   ¦       ¦   ¦   \_version.py

¦   ¦       ¦   ¦   \_version\_meson.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---api

¦   ¦       ¦   ¦   ¦   internals.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---executors

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---extensions

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---indexers

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---interchange

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---types

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---typing

¦   ¦       ¦   ¦   ¦   ¦   aliases.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           aliases.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           internals.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---arrays

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---compat

¦   ¦       ¦   ¦   ¦   pickle\_compat.py

¦   ¦       ¦   ¦   ¦   pyarrow.py

¦   ¦       ¦   ¦   ¦   \_constants.py

¦   ¦       ¦   ¦   ¦   \_optional.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---numpy

¦   ¦       ¦   ¦   ¦   ¦   function.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           function.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           pickle\_compat.cpython-314.pyc

¦   ¦       ¦   ¦           pyarrow.cpython-314.pyc

¦   ¦       ¦   ¦           \_constants.cpython-314.pyc

¦   ¦       ¦   ¦           \_optional.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---core

¦   ¦       ¦   ¦   ¦   accessor.py

¦   ¦       ¦   ¦   ¦   algorithms.py

¦   ¦       ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   apply.py

¦   ¦       ¦   ¦   ¦   arraylike.py

¦   ¦       ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   col.py

¦   ¦       ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   config\_init.py

¦   ¦       ¦   ¦   ¦   construction.py

¦   ¦       ¦   ¦   ¦   flags.py

¦   ¦       ¦   ¦   ¦   frame.py

¦   ¦       ¦   ¦   ¦   generic.py

¦   ¦       ¦   ¦   ¦   indexing.py

¦   ¦       ¦   ¦   ¦   missing.py

¦   ¦       ¦   ¦   ¦   nanops.py

¦   ¦       ¦   ¦   ¦   resample.py

¦   ¦       ¦   ¦   ¦   roperator.py

¦   ¦       ¦   ¦   ¦   sample.py

¦   ¦       ¦   ¦   ¦   series.py

¦   ¦       ¦   ¦   ¦   shared\_docs.py

¦   ¦       ¦   ¦   ¦   sorting.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---arrays

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   boolean.py

¦   ¦       ¦   ¦   ¦   ¦   categorical.py

¦   ¦       ¦   ¦   ¦   ¦   datetimelike.py

¦   ¦       ¦   ¦   ¦   ¦   datetimes.py

¦   ¦       ¦   ¦   ¦   ¦   floating.py

¦   ¦       ¦   ¦   ¦   ¦   integer.py

¦   ¦       ¦   ¦   ¦   ¦   interval.py

¦   ¦       ¦   ¦   ¦   ¦   masked.py

¦   ¦       ¦   ¦   ¦   ¦   numeric.py

¦   ¦       ¦   ¦   ¦   ¦   numpy\_.py

¦   ¦       ¦   ¦   ¦   ¦   period.py

¦   ¦       ¦   ¦   ¦   ¦   string\_.py

¦   ¦       ¦   ¦   ¦   ¦   string\_arrow.py

¦   ¦       ¦   ¦   ¦   ¦   timedeltas.py

¦   ¦       ¦   ¦   ¦   ¦   \_arrow\_string\_mixins.py

¦   ¦       ¦   ¦   ¦   ¦   \_mixins.py

¦   ¦       ¦   ¦   ¦   ¦   \_ranges.py

¦   ¦       ¦   ¦   ¦   ¦   \_utils.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---arrow

¦   ¦       ¦   ¦   ¦   ¦   ¦   accessors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   extension\_types.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_arrow\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           accessors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           extension\_types.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_arrow\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---sparse

¦   ¦       ¦   ¦   ¦   ¦   ¦   accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   scipy\_sparse.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           scipy\_sparse.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           boolean.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           datetimelike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           datetimes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           floating.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           integer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           masked.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           numpy\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           string\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           string\_arrow.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           timedeltas.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_arrow\_string\_mixins.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_mixins.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_ranges.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---array\_algos

¦   ¦       ¦   ¦   ¦   ¦   datetimelike\_accumulations.py

¦   ¦       ¦   ¦   ¦   ¦   masked\_accumulations.py

¦   ¦       ¦   ¦   ¦   ¦   masked\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   putmask.py

¦   ¦       ¦   ¦   ¦   ¦   quantile.py

¦   ¦       ¦   ¦   ¦   ¦   replace.py

¦   ¦       ¦   ¦   ¦   ¦   take.py

¦   ¦       ¦   ¦   ¦   ¦   transforms.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           datetimelike\_accumulations.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           masked\_accumulations.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           masked\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           putmask.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           quantile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           take.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           transforms.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---computation

¦   ¦       ¦   ¦   ¦   ¦   align.py

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   check.py

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   engines.py

¦   ¦       ¦   ¦   ¦   ¦   eval.py

¦   ¦       ¦   ¦   ¦   ¦   expr.py

¦   ¦       ¦   ¦   ¦   ¦   expressions.py

¦   ¦       ¦   ¦   ¦   ¦   ops.py

¦   ¦       ¦   ¦   ¦   ¦   parsing.py

¦   ¦       ¦   ¦   ¦   ¦   pytables.py

¦   ¦       ¦   ¦   ¦   ¦   scope.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           align.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           check.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           engines.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           eval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           expr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           expressions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           parsing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pytables.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           scope.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---dtypes

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   astype.py

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   cast.py

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   concat.py

¦   ¦       ¦   ¦   ¦   ¦   dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   generic.py

¦   ¦       ¦   ¦   ¦   ¦   inference.py

¦   ¦       ¦   ¦   ¦   ¦   missing.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           cast.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           generic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           inference.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---groupby

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   categorical.py

¦   ¦       ¦   ¦   ¦   ¦   generic.py

¦   ¦       ¦   ¦   ¦   ¦   groupby.py

¦   ¦       ¦   ¦   ¦   ¦   grouper.py

¦   ¦       ¦   ¦   ¦   ¦   indexing.py

¦   ¦       ¦   ¦   ¦   ¦   numba\_.py

¦   ¦       ¦   ¦   ¦   ¦   ops.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           generic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           grouper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           numba\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---indexers

¦   ¦       ¦   ¦   ¦   ¦   objects.py

¦   ¦       ¦   ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           objects.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---indexes

¦   ¦       ¦   ¦   ¦   ¦   accessors.py

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   category.py

¦   ¦       ¦   ¦   ¦   ¦   datetimelike.py

¦   ¦       ¦   ¦   ¦   ¦   datetimes.py

¦   ¦       ¦   ¦   ¦   ¦   extension.py

¦   ¦       ¦   ¦   ¦   ¦   frozen.py

¦   ¦       ¦   ¦   ¦   ¦   interval.py

¦   ¦       ¦   ¦   ¦   ¦   multi.py

¦   ¦       ¦   ¦   ¦   ¦   period.py

¦   ¦       ¦   ¦   ¦   ¦   range.py

¦   ¦       ¦   ¦   ¦   ¦   timedeltas.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           accessors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           category.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           datetimelike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           datetimes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           extension.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           frozen.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           multi.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           range.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           timedeltas.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---interchange

¦   ¦       ¦   ¦   ¦   ¦   buffer.py

¦   ¦       ¦   ¦   ¦   ¦   column.py

¦   ¦       ¦   ¦   ¦   ¦   dataframe.py

¦   ¦       ¦   ¦   ¦   ¦   dataframe\_protocol.py

¦   ¦       ¦   ¦   ¦   ¦   from\_dataframe.py

¦   ¦       ¦   ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           buffer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           column.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           dataframe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           dataframe\_protocol.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           from\_dataframe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---internals

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   blocks.py

¦   ¦       ¦   ¦   ¦   ¦   concat.py

¦   ¦       ¦   ¦   ¦   ¦   construction.py

¦   ¦       ¦   ¦   ¦   ¦   managers.py

¦   ¦       ¦   ¦   ¦   ¦   ops.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           blocks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           construction.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           managers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   describe.py

¦   ¦       ¦   ¦   ¦   ¦   selectn.py

¦   ¦       ¦   ¦   ¦   ¦   to\_dict.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           describe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           selectn.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           to\_dict.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---ops

¦   ¦       ¦   ¦   ¦   ¦   array\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   dispatch.py

¦   ¦       ¦   ¦   ¦   ¦   docstrings.py

¦   ¦       ¦   ¦   ¦   ¦   invalid.py

¦   ¦       ¦   ¦   ¦   ¦   mask\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   missing.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           array\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           dispatch.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           docstrings.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           invalid.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           mask\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---reshape

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   concat.py

¦   ¦       ¦   ¦   ¦   ¦   encoding.py

¦   ¦       ¦   ¦   ¦   ¦   melt.py

¦   ¦       ¦   ¦   ¦   ¦   merge.py

¦   ¦       ¦   ¦   ¦   ¦   pivot.py

¦   ¦       ¦   ¦   ¦   ¦   reshape.py

¦   ¦       ¦   ¦   ¦   ¦   tile.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           encoding.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           melt.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           merge.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pivot.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           reshape.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           tile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---sparse

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---strings

¦   ¦       ¦   ¦   ¦   ¦   accessor.py

¦   ¦       ¦   ¦   ¦   ¦   object\_array.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           object\_array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---tools

¦   ¦       ¦   ¦   ¦   ¦   datetimes.py

¦   ¦       ¦   ¦   ¦   ¦   numeric.py

¦   ¦       ¦   ¦   ¦   ¦   timedeltas.py

¦   ¦       ¦   ¦   ¦   ¦   times.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           datetimes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           timedeltas.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           times.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---util

¦   ¦       ¦   ¦   ¦   ¦   hashing.py

¦   ¦       ¦   ¦   ¦   ¦   numba\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           hashing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           numba\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---window

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   doc.py

¦   ¦       ¦   ¦   ¦   ¦   ewm.py

¦   ¦       ¦   ¦   ¦   ¦   expanding.py

¦   ¦       ¦   ¦   ¦   ¦   numba\_.py

¦   ¦       ¦   ¦   ¦   ¦   online.py

¦   ¦       ¦   ¦   ¦   ¦   rolling.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           doc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           ewm.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           expanding.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           numba\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           online.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           rolling.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_numba

¦   ¦       ¦   ¦   ¦   ¦   executor.py

¦   ¦       ¦   ¦   ¦   ¦   extensions.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---kernels

¦   ¦       ¦   ¦   ¦   ¦   ¦   mean\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   min\_max\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   shared.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   sum\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   var\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           mean\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           min\_max\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           shared.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           sum\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           var\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           executor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           extensions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           accessor.cpython-314.pyc

¦   ¦       ¦   ¦           algorithms.cpython-314.pyc

¦   ¦       ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦           apply.cpython-314.pyc

¦   ¦       ¦   ¦           arraylike.cpython-314.pyc

¦   ¦       ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦           col.cpython-314.pyc

¦   ¦       ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦           config\_init.cpython-314.pyc

¦   ¦       ¦   ¦           construction.cpython-314.pyc

¦   ¦       ¦   ¦           flags.cpython-314.pyc

¦   ¦       ¦   ¦           frame.cpython-314.pyc

¦   ¦       ¦   ¦           generic.cpython-314.pyc

¦   ¦       ¦   ¦           indexing.cpython-314.pyc

¦   ¦       ¦   ¦           missing.cpython-314.pyc

¦   ¦       ¦   ¦           nanops.cpython-314.pyc

¦   ¦       ¦   ¦           resample.cpython-314.pyc

¦   ¦       ¦   ¦           roperator.cpython-314.pyc

¦   ¦       ¦   ¦           sample.cpython-314.pyc

¦   ¦       ¦   ¦           series.cpython-314.pyc

¦   ¦       ¦   ¦           shared\_docs.cpython-314.pyc

¦   ¦       ¦   ¦           sorting.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---errors

¦   ¦       ¦   ¦   ¦   cow.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           cow.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---io

¦   ¦       ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   clipboards.py

¦   ¦       ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   feather\_format.py

¦   ¦       ¦   ¦   ¦   html.py

¦   ¦       ¦   ¦   ¦   iceberg.py

¦   ¦       ¦   ¦   ¦   orc.py

¦   ¦       ¦   ¦   ¦   parquet.py

¦   ¦       ¦   ¦   ¦   pickle.py

¦   ¦       ¦   ¦   ¦   pytables.py

¦   ¦       ¦   ¦   ¦   spss.py

¦   ¦       ¦   ¦   ¦   sql.py

¦   ¦       ¦   ¦   ¦   stata.py

¦   ¦       ¦   ¦   ¦   xml.py

¦   ¦       ¦   ¦   ¦   \_util.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---clipboard

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---excel

¦   ¦       ¦   ¦   ¦   ¦   \_base.py

¦   ¦       ¦   ¦   ¦   ¦   \_calamine.py

¦   ¦       ¦   ¦   ¦   ¦   \_odfreader.py

¦   ¦       ¦   ¦   ¦   ¦   \_odswriter.py

¦   ¦       ¦   ¦   ¦   ¦   \_openpyxl.py

¦   ¦       ¦   ¦   ¦   ¦   \_pyxlsb.py

¦   ¦       ¦   ¦   ¦   ¦   \_util.py

¦   ¦       ¦   ¦   ¦   ¦   \_xlrd.py

¦   ¦       ¦   ¦   ¦   ¦   \_xlsxwriter.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_calamine.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_odfreader.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_odswriter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_openpyxl.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_pyxlsb.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_xlrd.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_xlsxwriter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---formats

¦   ¦       ¦   ¦   ¦   ¦   console.py

¦   ¦       ¦   ¦   ¦   ¦   css.py

¦   ¦       ¦   ¦   ¦   ¦   csvs.py

¦   ¦       ¦   ¦   ¦   ¦   excel.py

¦   ¦       ¦   ¦   ¦   ¦   format.py

¦   ¦       ¦   ¦   ¦   ¦   html.py

¦   ¦       ¦   ¦   ¦   ¦   info.py

¦   ¦       ¦   ¦   ¦   ¦   printing.py

¦   ¦       ¦   ¦   ¦   ¦   string.py

¦   ¦       ¦   ¦   ¦   ¦   style.py

¦   ¦       ¦   ¦   ¦   ¦   style\_render.py

¦   ¦       ¦   ¦   ¦   ¦   xml.py

¦   ¦       ¦   ¦   ¦   ¦   \_color\_data.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---templates

¦   ¦       ¦   ¦   ¦   ¦       html.tpl

¦   ¦       ¦   ¦   ¦   ¦       html\_style.tpl

¦   ¦       ¦   ¦   ¦   ¦       html\_table.tpl

¦   ¦       ¦   ¦   ¦   ¦       latex.tpl

¦   ¦       ¦   ¦   ¦   ¦       latex\_longtable.tpl

¦   ¦       ¦   ¦   ¦   ¦       latex\_table.tpl

¦   ¦       ¦   ¦   ¦   ¦       string.tpl

¦   ¦       ¦   ¦   ¦   ¦       typst.tpl

¦   ¦       ¦   ¦   ¦   ¦       

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           console.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           css.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           csvs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           excel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           format.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           html.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           info.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           printing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           style.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           style\_render.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           xml.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_color\_data.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---json

¦   ¦       ¦   ¦   ¦   ¦   \_json.py

¦   ¦       ¦   ¦   ¦   ¦   \_normalize.py

¦   ¦       ¦   ¦   ¦   ¦   \_table\_schema.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_json.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_normalize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_table\_schema.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---parsers

¦   ¦       ¦   ¦   ¦   ¦   arrow\_parser\_wrapper.py

¦   ¦       ¦   ¦   ¦   ¦   base\_parser.py

¦   ¦       ¦   ¦   ¦   ¦   c\_parser\_wrapper.py

¦   ¦       ¦   ¦   ¦   ¦   python\_parser.py

¦   ¦       ¦   ¦   ¦   ¦   readers.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           arrow\_parser\_wrapper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           base\_parser.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           c\_parser\_wrapper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           python\_parser.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           readers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---sas

¦   ¦       ¦   ¦   ¦   ¦   sas7bdat.py

¦   ¦       ¦   ¦   ¦   ¦   sasreader.py

¦   ¦       ¦   ¦   ¦   ¦   sas\_constants.py

¦   ¦       ¦   ¦   ¦   ¦   sas\_xport.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           sas7bdat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           sasreader.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           sas\_constants.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           sas\_xport.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦           clipboards.cpython-314.pyc

¦   ¦       ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦           feather\_format.cpython-314.pyc

¦   ¦       ¦   ¦           html.cpython-314.pyc

¦   ¦       ¦   ¦           iceberg.cpython-314.pyc

¦   ¦       ¦   ¦           orc.cpython-314.pyc

¦   ¦       ¦   ¦           parquet.cpython-314.pyc

¦   ¦       ¦   ¦           pickle.cpython-314.pyc

¦   ¦       ¦   ¦           pytables.cpython-314.pyc

¦   ¦       ¦   ¦           spss.cpython-314.pyc

¦   ¦       ¦   ¦           sql.cpython-314.pyc

¦   ¦       ¦   ¦           stata.cpython-314.pyc

¦   ¦       ¦   ¦           xml.cpython-314.pyc

¦   ¦       ¦   ¦           \_util.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---plotting

¦   ¦       ¦   ¦   ¦   \_core.py

¦   ¦       ¦   ¦   ¦   \_misc.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_matplotlib

¦   ¦       ¦   ¦   ¦   ¦   boxplot.py

¦   ¦       ¦   ¦   ¦   ¦   converter.py

¦   ¦       ¦   ¦   ¦   ¦   core.py

¦   ¦       ¦   ¦   ¦   ¦   groupby.py

¦   ¦       ¦   ¦   ¦   ¦   hist.py

¦   ¦       ¦   ¦   ¦   ¦   misc.py

¦   ¦       ¦   ¦   ¦   ¦   style.py

¦   ¦       ¦   ¦   ¦   ¦   timeseries.py

¦   ¦       ¦   ¦   ¦   ¦   tools.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           boxplot.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           converter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           core.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           hist.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           misc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           style.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           timeseries.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           tools.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_core.cpython-314.pyc

¦   ¦       ¦   ¦           \_misc.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---tests

¦   ¦       ¦   ¦   ¦   test\_aggregation.py

¦   ¦       ¦   ¦   ¦   test\_algos.py

¦   ¦       ¦   ¦   ¦   test\_col.py

¦   ¦       ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   test\_downstream.py

¦   ¦       ¦   ¦   ¦   test\_errors.py

¦   ¦       ¦   ¦   ¦   test\_expressions.py

¦   ¦       ¦   ¦   ¦   test\_flags.py

¦   ¦       ¦   ¦   ¦   test\_multilevel.py

¦   ¦       ¦   ¦   ¦   test\_nanops.py

¦   ¦       ¦   ¦   ¦   test\_optional\_dependency.py

¦   ¦       ¦   ¦   ¦   test\_register\_accessor.py

¦   ¦       ¦   ¦   ¦   test\_sorting.py

¦   ¦       ¦   ¦   ¦   test\_take.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---api

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_types.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_types.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---apply

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_frame\_apply.py

¦   ¦       ¦   ¦   ¦   ¦   test\_frame\_apply\_relabeling.py

¦   ¦       ¦   ¦   ¦   ¦   test\_frame\_transform.py

¦   ¦       ¦   ¦   ¦   ¦   test\_invalid\_arg.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numba.py

¦   ¦       ¦   ¦   ¦   ¦   test\_series\_apply.py

¦   ¦       ¦   ¦   ¦   ¦   test\_series\_apply\_relabeling.py

¦   ¦       ¦   ¦   ¦   ¦   test\_series\_transform.py

¦   ¦       ¦   ¦   ¦   ¦   test\_str.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_frame\_apply.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_frame\_apply\_relabeling.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_frame\_transform.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_invalid\_arg.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numba.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_series\_apply.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_series\_apply\_relabeling.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_series\_transform.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_str.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---arithmetic

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   test\_bool.py

¦   ¦       ¦   ¦   ¦   ¦   test\_categorical.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetime64.py

¦   ¦       ¦   ¦   ¦   ¦   test\_interval.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numeric.py

¦   ¦       ¦   ¦   ¦   ¦   test\_object.py

¦   ¦       ¦   ¦   ¦   ¦   test\_period.py

¦   ¦       ¦   ¦   ¦   ¦   test\_string.py

¦   ¦       ¦   ¦   ¦   ¦   test\_timedelta64.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_bool.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetime64.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_object.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_timedelta64.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---arrays

¦   ¦       ¦   ¦   ¦   ¦   masked\_shared.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetimelike.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetimes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_ndarray\_backed.py

¦   ¦       ¦   ¦   ¦   ¦   test\_period.py

¦   ¦       ¦   ¦   ¦   ¦   test\_timedeltas.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---boolean

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_comparison.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_construction.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_function.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_logical.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reduction.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_repr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_comparison.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_construction.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_function.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_logical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reduction.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_repr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---categorical

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_algos.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_analytics.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_map.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_missing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_operators.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_replace.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_repr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sorting.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_subclass.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_take.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_warnings.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_algos.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_analytics.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_map.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_operators.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_repr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sorting.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_subclass.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_take.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_warnings.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---datetimes

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_cumulative.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_cumulative.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---floating

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_comparison.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_concat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_construction.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_contains.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_function.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_repr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_numpy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_comparison.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_construction.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_contains.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_function.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_repr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_numpy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---integer

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_comparison.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_concat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_construction.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_function.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reduction.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_repr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_comparison.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_construction.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_function.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reduction.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_repr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---interval

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval\_pyarrow.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_overlaps.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interval\_pyarrow.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_overlaps.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---masked

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arrow\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_function.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_arrow\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_function.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---numpy\_

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_numpy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_numpy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---period

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arrow\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arrow\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---sparse

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetics.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_combine\_concat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dtype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_libsparse.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_unary.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetics.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_combine\_concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_libsparse.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_unary.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---string\_

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_concat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_string.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_string\_arrow.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_string\_arrow.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---timedeltas

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_cumulative.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_cumulative.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           masked\_shared.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetimelike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetimes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_ndarray\_backed.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_timedeltas.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---base

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   test\_conversion.py

¦   ¦       ¦   ¦   ¦   ¦   test\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   test\_misc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_transpose.py

¦   ¦       ¦   ¦   ¦   ¦   test\_unique.py

¦   ¦       ¦   ¦   ¦   ¦   test\_value\_counts.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_conversion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_misc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_transpose.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_unique.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_value\_counts.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---computation

¦   ¦       ¦   ¦   ¦   ¦   test\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   test\_eval.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_eval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---config

¦   ¦       ¦   ¦   ¦   ¦   test\_config.py

¦   ¦       ¦   ¦   ¦   ¦   test\_localization.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_config.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_localization.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---construction

¦   ¦       ¦   ¦   ¦   ¦   test\_extract\_array.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_extract\_array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---copy\_view

¦   ¦       ¦   ¦   ¦   ¦   test\_array.py

¦   ¦       ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   test\_chained\_assignment\_deprecation.py

¦   ¦       ¦   ¦   ¦   ¦   test\_clip.py

¦   ¦       ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   test\_copy\_deprecation.py

¦   ¦       ¦   ¦   ¦   ¦   test\_core\_functionalities.py

¦   ¦       ¦   ¦   ¦   ¦   test\_functions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_internals.py

¦   ¦       ¦   ¦   ¦   ¦   test\_interp\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   test\_methods.py

¦   ¦       ¦   ¦   ¦   ¦   test\_replace.py

¦   ¦       ¦   ¦   ¦   ¦   test\_setitem.py

¦   ¦       ¦   ¦   ¦   ¦   test\_util.py

¦   ¦       ¦   ¦   ¦   ¦   util.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---index

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_datetimeindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_intervalindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_periodindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timedeltaindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_datetimeindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_intervalindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_periodindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timedeltaindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_chained\_assignment\_deprecation.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_clip.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_copy\_deprecation.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_core\_functionalities.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_functions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_internals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_interp\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_methods.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_setitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---dtypes

¦   ¦       ¦   ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_concat.py

¦   ¦       ¦   ¦   ¦   ¦   test\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_generic.py

¦   ¦       ¦   ¦   ¦   ¦   test\_inference.py

¦   ¦       ¦   ¦   ¦   ¦   test\_missing.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---cast

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_box\_unbox.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_can\_hold\_element.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_construct\_from\_scalar.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_construct\_ndarray.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_construct\_object\_arr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dict\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_downcast.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_find\_common\_type.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_infer\_datetimelike.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_infer\_dtype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_promote.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_box\_unbox.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_can\_hold\_element.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_construct\_from\_scalar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_construct\_ndarray.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_construct\_object\_arr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dict\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_downcast.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_find\_common\_type.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_infer\_datetimelike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_infer\_dtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_promote.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_generic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_inference.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---extension

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arrow.py

¦   ¦       ¦   ¦   ¦   ¦   test\_categorical.py

¦   ¦       ¦   ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_extension.py

¦   ¦       ¦   ¦   ¦   ¦   test\_interval.py

¦   ¦       ¦   ¦   ¦   ¦   test\_masked.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numpy.py

¦   ¦       ¦   ¦   ¦   ¦   test\_period.py

¦   ¦       ¦   ¦   ¦   ¦   test\_sparse.py

¦   ¦       ¦   ¦   ¦   ¦   test\_string.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---array\_with\_attr

¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_array\_with\_attr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_array\_with\_attr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---base

¦   ¦       ¦   ¦   ¦   ¦   ¦   accumulate.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   casting.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   dim2.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   dtype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   getitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   groupby.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   interface.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   io.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   methods.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   missing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   printing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   reduce.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   reshaping.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   setitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           accumulate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           casting.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           dim2.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           dtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           getitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           interface.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           io.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           methods.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           printing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           reduce.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           reshaping.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           setitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---date

¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---decimal

¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_decimal.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_decimal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---json

¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_json.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_json.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---list

¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_list.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_list.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---uuid

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_uuid.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_uuid.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arrow.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_extension.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_masked.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numpy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_sparse.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---frame

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_alter\_axes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arrow\_interface.py

¦   ¦       ¦   ¦   ¦   ¦   test\_block\_internals.py

¦   ¦       ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cumulative.py

¦   ¦       ¦   ¦   ¦   ¦   test\_iteration.py

¦   ¦       ¦   ¦   ¦   ¦   test\_logical\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   test\_nonunique\_indexes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_npfuncs.py

¦   ¦       ¦   ¦   ¦   ¦   test\_query\_eval.py

¦   ¦       ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_repr.py

¦   ¦       ¦   ¦   ¦   ¦   test\_stack\_unstack.py

¦   ¦       ¦   ¦   ¦   ¦   test\_subclass.py

¦   ¦       ¦   ¦   ¦   ¦   test\_ufunc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_unary.py

¦   ¦       ¦   ¦   ¦   ¦   test\_validate.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---constructors

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_from\_dict.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_from\_records.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_from\_dict.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_from\_records.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---indexing

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_coercion.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_delitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_get.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_getitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_get\_value.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_insert.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_mask.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_set\_value.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_take.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_where.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_xs.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_coercion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_delitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_get.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_getitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_get\_value.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_insert.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_mask.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_set\_value.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_take.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_where.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_xs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_add\_prefix\_suffix.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_align.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_asfreq.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_asof.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_assign.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_at\_time.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_between\_time.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_clip.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_combine.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_combine\_first.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_compare.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_convert\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_copy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_count.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_cov\_corr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_describe.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_diff.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dot.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_drop.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_droplevel.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dropna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_drop\_duplicates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_duplicated.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_equals.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_explode.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_filter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_first\_valid\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_get\_numeric\_data.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_head\_tail.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_infer\_objects.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_info.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interpolate.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_isetitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_isin.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_is\_homogeneous\_dtype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_iterrows.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_map.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_matmul.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_nlargest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pct\_change.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pipe.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pop.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_quantile.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_rank.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reindex\_like.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_rename.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_rename\_axis.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reorder\_levels.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_replace.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reset\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_round.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sample.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_select\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_set\_axis.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_set\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_shift.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_size.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sort\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sort\_values.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_swaplevel.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_csv.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_dict.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_dict\_of\_blocks.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_numpy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_period.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_records.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_timestamp.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_transpose.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_truncate.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_tz\_convert.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_tz\_localize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_update.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_values.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_value\_counts.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_add\_prefix\_suffix.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_align.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_asfreq.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_asof.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_assign.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_at\_time.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_between\_time.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_clip.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_combine.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_combine\_first.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_compare.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_convert\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_copy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_count.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_cov\_corr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_describe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_diff.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dot.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_drop.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_droplevel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dropna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_drop\_duplicates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_duplicated.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_equals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_explode.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_filter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_first\_valid\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_get\_numeric\_data.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_head\_tail.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_infer\_objects.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_info.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interpolate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_isetitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_isin.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_is\_homogeneous\_dtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_iterrows.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_map.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_matmul.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_nlargest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pct\_change.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pipe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pop.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_quantile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_rank.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reindex\_like.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_rename.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_rename\_axis.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reorder\_levels.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reset\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_round.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sample.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_select\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_set\_axis.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_set\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_shift.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_size.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sort\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sort\_values.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_swaplevel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_csv.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_dict.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_dict\_of\_blocks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_numpy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_records.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_timestamp.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_transpose.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_truncate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_tz\_convert.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_tz\_localize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_update.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_values.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_value\_counts.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_alter\_axes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arrow\_interface.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_block\_internals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cumulative.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_iteration.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_logical\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_nonunique\_indexes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_npfuncs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_query\_eval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_repr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_stack\_unstack.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_subclass.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_ufunc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_unary.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_validate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---generic

¦   ¦       ¦   ¦   ¦   ¦   test\_duplicate\_labels.py

¦   ¦       ¦   ¦   ¦   ¦   test\_finalize.py

¦   ¦       ¦   ¦   ¦   ¦   test\_frame.py

¦   ¦       ¦   ¦   ¦   ¦   test\_generic.py

¦   ¦       ¦   ¦   ¦   ¦   test\_label\_or\_level\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   test\_series.py

¦   ¦       ¦   ¦   ¦   ¦   test\_to\_xarray.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_duplicate\_labels.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_finalize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_frame.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_generic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_label\_or\_level\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_series.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_to\_xarray.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---groupby

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_all\_methods.py

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_apply.py

¦   ¦       ¦   ¦   ¦   ¦   test\_bin\_groupby.py

¦   ¦       ¦   ¦   ¦   ¦   test\_categorical.py

¦   ¦       ¦   ¦   ¦   ¦   test\_counting.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cumulative.py

¦   ¦       ¦   ¦   ¦   ¦   test\_filters.py

¦   ¦       ¦   ¦   ¦   ¦   test\_groupby.py

¦   ¦       ¦   ¦   ¦   ¦   test\_groupby\_dropna.py

¦   ¦       ¦   ¦   ¦   ¦   test\_groupby\_subclass.py

¦   ¦       ¦   ¦   ¦   ¦   test\_grouping.py

¦   ¦       ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_index\_as\_string.py

¦   ¦       ¦   ¦   ¦   ¦   test\_libgroupby.py

¦   ¦       ¦   ¦   ¦   ¦   test\_missing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numba.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numeric\_only.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pipe.py

¦   ¦       ¦   ¦   ¦   ¦   test\_raises.py

¦   ¦       ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_timegrouper.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---aggregate

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_aggregate.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_cython.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_numba.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_other.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_aggregate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_cython.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_numba.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_other.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_describe.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_groupby\_shift\_diff.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_is\_monotonic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_kurt.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_nlargest\_nsmallest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_nth.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_quantile.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_rank.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sample.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_size.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_skew.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_value\_counts.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_describe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_groupby\_shift\_diff.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_is\_monotonic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_kurt.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_nlargest\_nsmallest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_nth.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_quantile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_rank.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sample.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_size.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_skew.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_value\_counts.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---transform

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_numba.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_transform.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_numba.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_transform.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_all\_methods.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_apply.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_bin\_groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_counting.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cumulative.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_filters.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_groupby\_dropna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_groupby\_subclass.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_grouping.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_index\_as\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_libgroupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numba.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numeric\_only.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pipe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_raises.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_timegrouper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---indexes

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_any\_index.py

¦   ¦       ¦   ¦   ¦   ¦   test\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetimelike.py

¦   ¦       ¦   ¦   ¦   ¦   test\_engines.py

¦   ¦       ¦   ¦   ¦   ¦   test\_frozen.py

¦   ¦       ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_index\_new.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numpy\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   test\_old\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   test\_subclass.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---base\_class

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pickle.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reshape.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_where.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pickle.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reshape.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_where.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---categorical

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_append.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_category.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_equals.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_map.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_append.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_category.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_equals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_map.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---datetimelike\_

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_drop\_duplicates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_equals.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_is\_monotonic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_nat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sort\_values.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_value\_counts.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_drop\_duplicates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_equals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_is\_monotonic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_nat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sort\_values.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_value\_counts.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---datetimes

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_date\_range.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_freq\_attr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_iter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_npfuncs.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_partial\_slicing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pickle.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_scalar\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timezones.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_asof.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_delete.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_factorize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_insert.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_isocalendar.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_map.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_normalize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_repeat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_resolution.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_round.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_shift.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_snap.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_frame.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_julian\_date.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_period.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_pydatetime.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_series.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_tz\_convert.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_tz\_localize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_unique.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_asof.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_delete.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_factorize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_insert.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_isocalendar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_map.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_normalize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_repeat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_resolution.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_round.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_shift.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_snap.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_frame.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_julian\_date.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_pydatetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_series.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_tz\_convert.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_tz\_localize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_unique.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_date\_range.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_freq\_attr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_iter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_npfuncs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_partial\_slicing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pickle.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_scalar\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timezones.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---interval

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_equals.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval\_range.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval\_tree.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pickle.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_equals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interval\_range.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interval\_tree.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pickle.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---multi

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_analytics.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_conversion.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_copy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_drop.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_duplicates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_equivalence.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_get\_level\_values.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_get\_set.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_integrity.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_isin.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_lexsort.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_missing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_monotonic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_names.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_partial\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pickle.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reshape.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sorting.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_take.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_util.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_analytics.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_conversion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_copy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_drop.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_duplicates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_equivalence.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_get\_level\_values.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_get\_set.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_integrity.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_isin.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_lexsort.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_monotonic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_names.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_partial\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pickle.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reshape.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sorting.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_take.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---numeric

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_numeric.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---object

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---period

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_freq\_attr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_monotonic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_partial\_slicing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_period.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_period\_range.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pickle.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_resolution.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_scalar\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_searchsorted.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_tools.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_asfreq.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_factorize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_insert.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_is\_full.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_repeat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_shift.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_timestamp.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_asfreq.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_factorize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_insert.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_is\_full.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_repeat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_shift.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_timestamp.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_freq\_attr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_monotonic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_partial\_slicing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_period\_range.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pickle.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_resolution.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_scalar\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_searchsorted.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_tools.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---ranges

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_range.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_range.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---string

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---timedeltas

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_delete.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_freq\_attr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pickle.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_scalar\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_searchsorted.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setops.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timedelta.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timedelta\_range.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_factorize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_insert.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_repeat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_shift.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_factorize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_insert.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_repeat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_shift.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_delete.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_freq\_attr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pickle.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_scalar\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_searchsorted.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timedelta.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timedelta\_range.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_any\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetimelike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_engines.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_frozen.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_index\_new.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numpy\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_old\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_setops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_subclass.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---indexing

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_at.py

¦   ¦       ¦   ¦   ¦   ¦   test\_categorical.py

¦   ¦       ¦   ¦   ¦   ¦   test\_chaining\_and\_caching.py

¦   ¦       ¦   ¦   ¦   ¦   test\_check\_indexer.py

¦   ¦       ¦   ¦   ¦   ¦   test\_coercion.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_floats.py

¦   ¦       ¦   ¦   ¦   ¦   test\_iat.py

¦   ¦       ¦   ¦   ¦   ¦   test\_iloc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_indexers.py

¦   ¦       ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_loc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_na\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_partial.py

¦   ¦       ¦   ¦   ¦   ¦   test\_scalar.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---interval

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval\_new.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interval\_new.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---multiindex

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_chaining\_and\_caching.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_getitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_iloc.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing\_slow.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_loc.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_multiindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_partial.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_slice.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sorted.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_chaining\_and\_caching.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_getitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_iloc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing\_slow.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_loc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_multiindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_partial.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_slice.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sorted.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_at.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_chaining\_and\_caching.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_check\_indexer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_coercion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_floats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_iat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_iloc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_indexers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_loc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_na\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_partial.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_scalar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---interchange

¦   ¦       ¦   ¦   ¦   ¦   test\_impl.py

¦   ¦       ¦   ¦   ¦   ¦   test\_spec\_conformance.py

¦   ¦       ¦   ¦   ¦   ¦   test\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_impl.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_spec\_conformance.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---internals

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_internals.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_internals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---io

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   generate\_legacy\_storage\_files.py

¦   ¦       ¦   ¦   ¦   ¦   test\_clipboard.py

¦   ¦       ¦   ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_compression.py

¦   ¦       ¦   ¦   ¦   ¦   test\_feather.py

¦   ¦       ¦   ¦   ¦   ¦   test\_fsspec.py

¦   ¦       ¦   ¦   ¦   ¦   test\_gcs.py

¦   ¦       ¦   ¦   ¦   ¦   test\_html.py

¦   ¦       ¦   ¦   ¦   ¦   test\_http\_headers.py

¦   ¦       ¦   ¦   ¦   ¦   test\_iceberg.py

¦   ¦       ¦   ¦   ¦   ¦   test\_orc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_parquet.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pickle.py

¦   ¦       ¦   ¦   ¦   ¦   test\_s3.py

¦   ¦       ¦   ¦   ¦   ¦   test\_spss.py

¦   ¦       ¦   ¦   ¦   ¦   test\_sql.py

¦   ¦       ¦   ¦   ¦   ¦   test\_stata.py

¦   ¦       ¦   ¦   ¦   ¦   test\_util.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---excel

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_odf.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_odswriter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_openpyxl.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_readers.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_style.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_writers.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_xlrd.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_xlsxwriter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_odf.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_odswriter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_openpyxl.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_readers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_style.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_writers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_xlrd.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_xlsxwriter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---formats

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_console.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_css.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_eng\_formatting.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_format.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_ipython\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_printing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_csv.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_excel.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_html.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_latex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_markdown.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_string.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---style

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_bar.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_exceptions.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_format.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_highlight.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_html.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_matplotlib.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_non\_unique.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_style.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_tooltip.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_latex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_string.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_typst.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_bar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_exceptions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_format.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_highlight.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_html.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_matplotlib.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_non\_unique.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_style.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_tooltip.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_latex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_typst.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_console.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_css.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_eng\_formatting.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_format.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_ipython\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_printing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_csv.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_excel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_html.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_latex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_markdown.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---json

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_compression.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_deprecated\_kwargs.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_json\_table\_schema.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_json\_table\_schema\_ext\_dtype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_normalize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pandas.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_readlines.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_ujson.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_compression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_deprecated\_kwargs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_json\_table\_schema.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_json\_table\_schema\_ext\_dtype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_normalize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pandas.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_readlines.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_ujson.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---parser

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_comment.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_compression.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_concatenate\_chunks.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_converters.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_c\_parser\_only.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dialect.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_encoding.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_header.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_index\_col.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_mangle\_dupes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_multi\_thread.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_na\_values.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_network.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_parse\_dates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_python\_parser\_only.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_quoting.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_read\_fwf.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_skiprows.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_textreader.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_unsupported.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_upcast.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---common

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_chunksize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_common\_basic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_data\_list.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_decimal.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_file\_buffer\_url.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_float.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_inf.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_ints.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_iterator.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_read\_errors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_chunksize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_common\_basic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_data\_list.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_decimal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_file\_buffer\_url.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_float.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_inf.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_ints.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_iterator.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_read\_errors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---dtypes

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_categorical.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_dtypes\_basic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_empty.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_dtypes\_basic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_empty.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---usecols

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_parse\_dates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_strings.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_usecols\_basic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_parse\_dates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_strings.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_usecols\_basic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_comment.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_compression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_concatenate\_chunks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_converters.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_c\_parser\_only.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dialect.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_encoding.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_header.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_index\_col.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_mangle\_dupes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_multi\_thread.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_na\_values.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_network.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_parse\_dates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_python\_parser\_only.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_quoting.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_read\_fwf.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_skiprows.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_textreader.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_unsupported.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_upcast.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---pytables

¦   ¦       ¦   ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_append.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_categorical.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_complex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_errors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_file\_handling.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_keys.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_put.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pytables\_missing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_read.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_retain\_attributes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_round\_trip.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_select.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_store.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_subclass.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timezones.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_time\_series.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_append.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_complex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_errors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_file\_handling.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_keys.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_put.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pytables\_missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_read.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_retain\_attributes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_round\_trip.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_select.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_store.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_subclass.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timezones.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_time\_series.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---sas

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_byteswap.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sas.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sas7bdat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_xport.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_byteswap.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sas.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sas7bdat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_xport.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---xml

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_xml.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_xml.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_xml\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_xml.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_xml.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_xml\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           generate\_legacy\_storage\_files.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_clipboard.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_compression.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_feather.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_fsspec.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_gcs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_html.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_http\_headers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_iceberg.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_orc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_parquet.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pickle.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_s3.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_spss.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_sql.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_stata.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---libs

¦   ¦       ¦   ¦   ¦   ¦   test\_hashtable.py

¦   ¦       ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   test\_lib.py

¦   ¦       ¦   ¦   ¦   ¦   test\_libalgos.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_hashtable.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_lib.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_libalgos.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---plotting

¦   ¦       ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_backend.py

¦   ¦       ¦   ¦   ¦   ¦   test\_boxplot\_method.py

¦   ¦       ¦   ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   ¦   test\_converter.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetimelike.py

¦   ¦       ¦   ¦   ¦   ¦   test\_groupby.py

¦   ¦       ¦   ¦   ¦   ¦   test\_hist\_method.py

¦   ¦       ¦   ¦   ¦   ¦   test\_misc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_series.py

¦   ¦       ¦   ¦   ¦   ¦   test\_style.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---frame

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_frame.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_frame\_color.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_frame\_groupby.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_frame\_legend.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_frame\_subplots.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_hist\_box\_by.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_frame.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_frame\_color.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_frame\_groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_frame\_legend.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_frame\_subplots.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_hist\_box\_by.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_backend.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_boxplot\_method.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_converter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetimelike.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_hist\_method.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_misc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_series.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_style.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---reductions

¦   ¦       ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_stat\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_stat\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---resample

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_base.py

¦   ¦       ¦   ¦   ¦   ¦   test\_datetime\_index.py

¦   ¦       ¦   ¦   ¦   ¦   test\_period\_index.py

¦   ¦       ¦   ¦   ¦   ¦   test\_resampler\_grouper.py

¦   ¦       ¦   ¦   ¦   ¦   test\_resample\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_timedelta.py

¦   ¦       ¦   ¦   ¦   ¦   test\_time\_grouper.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_datetime\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_period\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_resampler\_grouper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_resample\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_timedelta.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_time\_grouper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---reshape

¦   ¦       ¦   ¦   ¦   ¦   test\_crosstab.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cut.py

¦   ¦       ¦   ¦   ¦   ¦   test\_from\_dummies.py

¦   ¦       ¦   ¦   ¦   ¦   test\_get\_dummies.py

¦   ¦       ¦   ¦   ¦   ¦   test\_melt.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pivot.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pivot\_multilevel.py

¦   ¦       ¦   ¦   ¦   ¦   test\_qcut.py

¦   ¦       ¦   ¦   ¦   ¦   test\_union\_categoricals.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---concat

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_append.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_append\_common.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_categorical.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_concat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dataframe.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_datetimes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_empty.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_invalid.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_series.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sort.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_append.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_append\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_categorical.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_concat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dataframe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_datetimes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_empty.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_invalid.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_series.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sort.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---merge

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_join.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_merge.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_merge\_antijoin.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_merge\_asof.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_merge\_cross.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_merge\_index\_as\_string.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_merge\_ordered.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_multi.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_join.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_merge.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_merge\_antijoin.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_merge\_asof.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_merge\_cross.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_merge\_index\_as\_string.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_merge\_ordered.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_multi.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_crosstab.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cut.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_from\_dummies.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_get\_dummies.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_melt.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pivot.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pivot\_multilevel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_qcut.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_union\_categoricals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---scalar

¦   ¦       ¦   ¦   ¦   ¦   test\_nat.py

¦   ¦       ¦   ¦   ¦   ¦   test\_na\_scalar.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---interval

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_contains.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interval.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_overlaps.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_contains.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interval.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_overlaps.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---period

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_asfreq.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_period.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_asfreq.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---timedelta

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timedelta.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_as\_unit.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_round.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_as\_unit.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_round.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timedelta.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---timestamp

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_comparisons.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timestamp.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_timezones.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_as\_unit.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_normalize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_replace.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_round.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_timestamp\_method.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_julian\_date.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_to\_pydatetime.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_tz\_convert.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test\_tz\_localize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_as\_unit.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_normalize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_round.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_timestamp\_method.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_julian\_date.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_to\_pydatetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_tz\_convert.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           test\_tz\_localize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_comparisons.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timestamp.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_timezones.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_nat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_na\_scalar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---series

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arithmetic.py

¦   ¦       ¦   ¦   ¦   ¦   test\_arrow\_interface.py

¦   ¦       ¦   ¦   ¦   ¦   test\_constructors.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cumulative.py

¦   ¦       ¦   ¦   ¦   ¦   test\_formats.py

¦   ¦       ¦   ¦   ¦   ¦   test\_iteration.py

¦   ¦       ¦   ¦   ¦   ¦   test\_logical\_ops.py

¦   ¦       ¦   ¦   ¦   ¦   test\_missing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_npfuncs.py

¦   ¦       ¦   ¦   ¦   ¦   test\_reductions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_subclass.py

¦   ¦       ¦   ¦   ¦   ¦   test\_ufunc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_unary.py

¦   ¦       ¦   ¦   ¦   ¦   test\_validate.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---accessors

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_cat\_accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dt\_accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_list\_accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sparse\_accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_struct\_accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_str\_accessor.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_cat\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dt\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_list\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sparse\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_struct\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_str\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---indexing

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_delitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_get.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_getitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_indexing.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_mask.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_setitem.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_set\_value.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_take.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_where.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_xs.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_delitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_get.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_getitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_indexing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_mask.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_setitem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_set\_value.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_take.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_where.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_xs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---methods

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_add\_prefix\_suffix.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_align.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_argsort.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_asof.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_astype.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_autocorr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_between.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_case\_when.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_clip.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_combine.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_combine\_first.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_compare.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_convert\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_copy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_count.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_cov\_corr.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_describe.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_diff.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_drop.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dropna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_drop\_duplicates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_duplicated.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_equals.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_explode.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_fillna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_get\_numeric\_data.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_head\_tail.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_infer\_objects.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_info.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_interpolate.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_isin.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_isna.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_is\_monotonic.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_is\_unique.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_item.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_map.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_matmul.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_nlargest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_nunique.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pct\_change.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_pop.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_quantile.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_rank.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reindex.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reindex\_like.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_rename.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_rename\_axis.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_repeat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_replace.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_reset\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_round.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_searchsorted.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_set\_name.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_size.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sort\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_sort\_values.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_tolist.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_csv.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_dict.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_frame.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_to\_numpy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_truncate.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_tz\_localize.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_unique.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_unstack.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_update.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_values.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_value\_counts.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_add\_prefix\_suffix.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_align.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_argsort.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_asof.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_astype.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_autocorr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_between.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_case\_when.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_clip.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_combine.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_combine\_first.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_compare.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_convert\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_copy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_count.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_cov\_corr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_describe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_diff.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_drop.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dropna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_drop\_duplicates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_duplicated.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_equals.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_explode.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_fillna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_get\_numeric\_data.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_head\_tail.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_infer\_objects.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_info.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_interpolate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_isin.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_isna.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_is\_monotonic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_is\_unique.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_item.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_map.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_matmul.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_nlargest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_nunique.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pct\_change.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_pop.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_quantile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_rank.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reindex.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reindex\_like.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_rename.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_rename\_axis.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_repeat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_reset\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_round.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_searchsorted.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_set\_name.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_size.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sort\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_sort\_values.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_tolist.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_csv.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_dict.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_frame.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_to\_numpy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_truncate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_tz\_localize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_unique.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_unstack.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_update.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_values.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_value\_counts.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arithmetic.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_arrow\_interface.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cumulative.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_formats.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_iteration.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_logical\_ops.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_missing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_npfuncs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_reductions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_subclass.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_ufunc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_unary.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_validate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---strings

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_case\_justify.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cat.py

¦   ¦       ¦   ¦   ¦   ¦   test\_extract.py

¦   ¦       ¦   ¦   ¦   ¦   test\_find\_replace.py

¦   ¦       ¦   ¦   ¦   ¦   test\_get\_dummies.py

¦   ¦       ¦   ¦   ¦   ¦   test\_split\_partition.py

¦   ¦       ¦   ¦   ¦   ¦   test\_strings.py

¦   ¦       ¦   ¦   ¦   ¦   test\_string\_array.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_case\_justify.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_extract.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_find\_replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_get\_dummies.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_split\_partition.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_strings.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_string\_array.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---tools

¦   ¦       ¦   ¦   ¦   ¦   test\_to\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_to\_numeric.py

¦   ¦       ¦   ¦   ¦   ¦   test\_to\_time.py

¦   ¦       ¦   ¦   ¦   ¦   test\_to\_timedelta.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_to\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_to\_numeric.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_to\_time.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_to\_timedelta.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---tseries

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---frequencies

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_frequencies.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_freq\_code.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_inference.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_frequencies.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_freq\_code.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_inference.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---holiday

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_calendar.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_federal.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_holiday.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_observance.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           test\_calendar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_federal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_holiday.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_observance.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---offsets

¦   ¦       ¦   ¦   ¦   ¦   ¦   common.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_business\_day.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_business\_halfyear.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_business\_hour.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_business\_month.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_business\_quarter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_business\_year.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_common.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_custom\_business\_day.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_custom\_business\_hour.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_custom\_business\_month.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_dst.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_easter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_fiscal.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_halfyear.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_index.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_month.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_offsets.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_offsets\_properties.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_quarter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_ticks.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_week.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_year.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_business\_day.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_business\_halfyear.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_business\_hour.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_business\_month.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_business\_quarter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_business\_year.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_custom\_business\_day.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_custom\_business\_hour.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_custom\_business\_month.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_dst.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_easter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_fiscal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_halfyear.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_month.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_offsets.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_offsets\_properties.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_quarter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_ticks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_week.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_year.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---tslibs

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_array\_to\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_ccalendar.py

¦   ¦       ¦   ¦   ¦   ¦   test\_conversion.py

¦   ¦       ¦   ¦   ¦   ¦   test\_fields.py

¦   ¦       ¦   ¦   ¦   ¦   test\_libfrequencies.py

¦   ¦       ¦   ¦   ¦   ¦   test\_liboffsets.py

¦   ¦       ¦   ¦   ¦   ¦   test\_npy\_units.py

¦   ¦       ¦   ¦   ¦   ¦   test\_np\_datetime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_parse\_iso8601.py

¦   ¦       ¦   ¦   ¦   ¦   test\_parsing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_period.py

¦   ¦       ¦   ¦   ¦   ¦   test\_resolution.py

¦   ¦       ¦   ¦   ¦   ¦   test\_strptime.py

¦   ¦       ¦   ¦   ¦   ¦   test\_timedeltas.py

¦   ¦       ¦   ¦   ¦   ¦   test\_timezones.py

¦   ¦       ¦   ¦   ¦   ¦   test\_to\_offset.py

¦   ¦       ¦   ¦   ¦   ¦   test\_tzconversion.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_array\_to\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_ccalendar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_conversion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_fields.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_libfrequencies.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_liboffsets.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_npy\_units.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_np\_datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_parse\_iso8601.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_parsing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_period.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_resolution.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_strptime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_timedeltas.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_timezones.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_to\_offset.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_tzconversion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---util

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_almost\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_attr\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_categorical\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_extension\_array\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_frame\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_index\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_interval\_array\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_numpy\_array\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_produces\_warning.py

¦   ¦       ¦   ¦   ¦   ¦   test\_assert\_series\_equal.py

¦   ¦       ¦   ¦   ¦   ¦   test\_deprecate.py

¦   ¦       ¦   ¦   ¦   ¦   test\_deprecate\_kwarg.py

¦   ¦       ¦   ¦   ¦   ¦   test\_deprecate\_nonkeyword\_arguments.py

¦   ¦       ¦   ¦   ¦   ¦   test\_doc.py

¦   ¦       ¦   ¦   ¦   ¦   test\_hashing.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numba.py

¦   ¦       ¦   ¦   ¦   ¦   test\_rewrite\_warning.py

¦   ¦       ¦   ¦   ¦   ¦   test\_shares\_memory.py

¦   ¦       ¦   ¦   ¦   ¦   test\_show\_versions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_util.py

¦   ¦       ¦   ¦   ¦   ¦   test\_validate\_args.py

¦   ¦       ¦   ¦   ¦   ¦   test\_validate\_args\_and\_kwargs.py

¦   ¦       ¦   ¦   ¦   ¦   test\_validate\_inclusive.py

¦   ¦       ¦   ¦   ¦   ¦   test\_validate\_kwargs.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_almost\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_attr\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_categorical\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_extension\_array\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_frame\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_index\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_interval\_array\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_numpy\_array\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_produces\_warning.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_assert\_series\_equal.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_deprecate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_deprecate\_kwarg.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_deprecate\_nonkeyword\_arguments.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_doc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_hashing.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numba.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_rewrite\_warning.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_shares\_memory.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_show\_versions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_validate\_args.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_validate\_args\_and\_kwargs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_validate\_inclusive.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_validate\_kwargs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---window

¦   ¦       ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   test\_api.py

¦   ¦       ¦   ¦   ¦   ¦   test\_apply.py

¦   ¦       ¦   ¦   ¦   ¦   test\_base\_indexer.py

¦   ¦       ¦   ¦   ¦   ¦   test\_cython\_aggregations.py

¦   ¦       ¦   ¦   ¦   ¦   test\_dtypes.py

¦   ¦       ¦   ¦   ¦   ¦   test\_ewm.py

¦   ¦       ¦   ¦   ¦   ¦   test\_expanding.py

¦   ¦       ¦   ¦   ¦   ¦   test\_groupby.py

¦   ¦       ¦   ¦   ¦   ¦   test\_numba.py

¦   ¦       ¦   ¦   ¦   ¦   test\_online.py

¦   ¦       ¦   ¦   ¦   ¦   test\_pairwise.py

¦   ¦       ¦   ¦   ¦   ¦   test\_rolling.py

¦   ¦       ¦   ¦   ¦   ¦   test\_rolling\_functions.py

¦   ¦       ¦   ¦   ¦   ¦   test\_rolling\_quantile.py

¦   ¦       ¦   ¦   ¦   ¦   test\_rolling\_skew\_kurt.py

¦   ¦       ¦   ¦   ¦   ¦   test\_timeseries\_window.py

¦   ¦       ¦   ¦   ¦   ¦   test\_win\_type.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---moments

¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_moments\_consistency\_ewm.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_moments\_consistency\_expanding.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   test\_moments\_consistency\_rolling.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_moments\_consistency\_ewm.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_moments\_consistency\_expanding.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           test\_moments\_consistency\_rolling.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           conftest.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_apply.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_base\_indexer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_cython\_aggregations.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_dtypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_ewm.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_expanding.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_groupby.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_numba.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_online.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_pairwise.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_rolling.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_rolling\_functions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_rolling\_quantile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_rolling\_skew\_kurt.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_timeseries\_window.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           test\_win\_type.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           test\_aggregation.cpython-314.pyc

¦   ¦       ¦   ¦           test\_algos.cpython-314.pyc

¦   ¦       ¦   ¦           test\_col.cpython-314.pyc

¦   ¦       ¦   ¦           test\_common.cpython-314.pyc

¦   ¦       ¦   ¦           test\_downstream.cpython-314.pyc

¦   ¦       ¦   ¦           test\_errors.cpython-314.pyc

¦   ¦       ¦   ¦           test\_expressions.cpython-314.pyc

¦   ¦       ¦   ¦           test\_flags.cpython-314.pyc

¦   ¦       ¦   ¦           test\_multilevel.cpython-314.pyc

¦   ¦       ¦   ¦           test\_nanops.cpython-314.pyc

¦   ¦       ¦   ¦           test\_optional\_dependency.cpython-314.pyc

¦   ¦       ¦   ¦           test\_register\_accessor.cpython-314.pyc

¦   ¦       ¦   ¦           test\_sorting.cpython-314.pyc

¦   ¦       ¦   ¦           test\_take.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---tseries

¦   ¦       ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   frequencies.py

¦   ¦       ¦   ¦   ¦   holiday.py

¦   ¦       ¦   ¦   ¦   offsets.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦           frequencies.cpython-314.pyc

¦   ¦       ¦   ¦           holiday.cpython-314.pyc

¦   ¦       ¦   ¦           offsets.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---util

¦   ¦       ¦   ¦   ¦   \_decorators.py

¦   ¦       ¦   ¦   ¦   \_doctools.py

¦   ¦       ¦   ¦   ¦   \_exceptions.py

¦   ¦       ¦   ¦   ¦   \_print\_versions.py

¦   ¦       ¦   ¦   ¦   \_tester.py

¦   ¦       ¦   ¦   ¦   \_test\_decorators.py

¦   ¦       ¦   ¦   ¦   \_validators.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---version

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_decorators.cpython-314.pyc

¦   ¦       ¦   ¦           \_doctools.cpython-314.pyc

¦   ¦       ¦   ¦           \_exceptions.cpython-314.pyc

¦   ¦       ¦   ¦           \_print\_versions.cpython-314.pyc

¦   ¦       ¦   ¦           \_tester.cpython-314.pyc

¦   ¦       ¦   ¦           \_test\_decorators.cpython-314.pyc

¦   ¦       ¦   ¦           \_validators.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_config

¦   ¦       ¦   ¦   ¦   config.py

¦   ¦       ¦   ¦   ¦   dates.py

¦   ¦       ¦   ¦   ¦   display.py

¦   ¦       ¦   ¦   ¦   localization.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           config.cpython-314.pyc

¦   ¦       ¦   ¦           dates.cpython-314.pyc

¦   ¦       ¦   ¦           display.cpython-314.pyc

¦   ¦       ¦   ¦           localization.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_libs

¦   ¦       ¦   ¦   ¦   algos.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   algos.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   algos.pyi

¦   ¦       ¦   ¦   ¦   arrays.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   arrays.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   arrays.pyi

¦   ¦       ¦   ¦   ¦   byteswap.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   byteswap.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   byteswap.pyi

¦   ¦       ¦   ¦   ¦   groupby.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   groupby.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   groupby.pyi

¦   ¦       ¦   ¦   ¦   hashing.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   hashing.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   hashing.pyi

¦   ¦       ¦   ¦   ¦   hashtable.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   hashtable.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   hashtable.pyi

¦   ¦       ¦   ¦   ¦   index.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   index.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   index.pyi

¦   ¦       ¦   ¦   ¦   indexing.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   indexing.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   indexing.pyi

¦   ¦       ¦   ¦   ¦   internals.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   internals.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   internals.pyi

¦   ¦       ¦   ¦   ¦   interval.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   interval.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   interval.pyi

¦   ¦       ¦   ¦   ¦   join.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   join.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   join.pyi

¦   ¦       ¦   ¦   ¦   json.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   json.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   json.pyi

¦   ¦       ¦   ¦   ¦   lib.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   lib.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   lib.pyi

¦   ¦       ¦   ¦   ¦   missing.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   missing.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   missing.pyi

¦   ¦       ¦   ¦   ¦   ops.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ops.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ops.pyi

¦   ¦       ¦   ¦   ¦   ops\_dispatch.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ops\_dispatch.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ops\_dispatch.pyi

¦   ¦       ¦   ¦   ¦   pandas\_datetime.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   pandas\_datetime.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   pandas\_parser.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   pandas\_parser.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   parsers.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   parsers.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   parsers.pyi

¦   ¦       ¦   ¦   ¦   properties.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   properties.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   properties.pyi

¦   ¦       ¦   ¦   ¦   reshape.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   reshape.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   reshape.pyi

¦   ¦       ¦   ¦   ¦   sas.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   sas.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   sas.pyi

¦   ¦       ¦   ¦   ¦   sparse.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   sparse.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   sparse.pyi

¦   ¦       ¦   ¦   ¦   testing.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   testing.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   testing.pyi

¦   ¦       ¦   ¦   ¦   tslib.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   tslib.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   tslib.pyi

¦   ¦       ¦   ¦   ¦   writers.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   writers.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   writers.pyi

¦   ¦       ¦   ¦   ¦   \_cyutility.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   \_cyutility.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---tslibs

¦   ¦       ¦   ¦   ¦   ¦   base.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   base.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   ccalendar.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   ccalendar.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   ccalendar.pyi

¦   ¦       ¦   ¦   ¦   ¦   conversion.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   conversion.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   conversion.pyi

¦   ¦       ¦   ¦   ¦   ¦   dtypes.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   dtypes.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   dtypes.pyi

¦   ¦       ¦   ¦   ¦   ¦   fields.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   fields.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   fields.pyi

¦   ¦       ¦   ¦   ¦   ¦   nattype.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   nattype.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   nattype.pyi

¦   ¦       ¦   ¦   ¦   ¦   np\_datetime.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   np\_datetime.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   np\_datetime.pyi

¦   ¦       ¦   ¦   ¦   ¦   offsets.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   offsets.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   offsets.pyi

¦   ¦       ¦   ¦   ¦   ¦   parsing.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   parsing.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   parsing.pyi

¦   ¦       ¦   ¦   ¦   ¦   period.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   period.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   period.pyi

¦   ¦       ¦   ¦   ¦   ¦   strptime.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   strptime.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   strptime.pyi

¦   ¦       ¦   ¦   ¦   ¦   timedeltas.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   timedeltas.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   timedeltas.pyi

¦   ¦       ¦   ¦   ¦   ¦   timestamps.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   timestamps.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   timestamps.pyi

¦   ¦       ¦   ¦   ¦   ¦   timezones.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   timezones.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   timezones.pyi

¦   ¦       ¦   ¦   ¦   ¦   tzconversion.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   tzconversion.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   tzconversion.pyi

¦   ¦       ¦   ¦   ¦   ¦   vectorized.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   vectorized.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   vectorized.pyi

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---window

¦   ¦       ¦   ¦   ¦   ¦   aggregations.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   aggregations.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   aggregations.pyi

¦   ¦       ¦   ¦   ¦   ¦   indexers.cp314-win\_amd64.lib

¦   ¦       ¦   ¦   ¦   ¦   indexers.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   ¦   ¦   indexers.pyi

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_testing

¦   ¦       ¦   ¦   ¦   asserters.py

¦   ¦       ¦   ¦   ¦   compat.py

¦   ¦       ¦   ¦   ¦   contexts.py

¦   ¦       ¦   ¦   ¦   \_hypothesis.py

¦   ¦       ¦   ¦   ¦   \_io.py

¦   ¦       ¦   ¦   ¦   \_warnings.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           asserters.cpython-314.pyc

¦   ¦       ¦   ¦           compat.cpython-314.pyc

¦   ¦       ¦   ¦           contexts.cpython-314.pyc

¦   ¦       ¦   ¦           \_hypothesis.cpython-314.pyc

¦   ¦       ¦   ¦           \_io.cpython-314.pyc

¦   ¦       ¦   ¦           \_warnings.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           conftest.cpython-314.pyc

¦   ¦       ¦           testing.cpython-314.pyc

¦   ¦       ¦           \_typing.cpython-314.pyc

¦   ¦       ¦           \_version.cpython-314.pyc

¦   ¦       ¦           \_version\_meson.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---pandas-3.0.6.dist-info

¦   ¦       ¦       DELVEWHEEL

¦   ¦       ¦       entry\_points.txt

¦   ¦       ¦       INSTALLER

¦   ¦       ¦       LICENSE

¦   ¦       ¦       METADATA

¦   ¦       ¦       RECORD

¦   ¦       ¦       REQUESTED

¦   ¦       ¦       WHEEL

¦   ¦       ¦       

¦   ¦       +---pandas.libs

¦   ¦       ¦       msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll

¦   ¦       ¦       

¦   ¦       +---pip

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   \_\_pip-runner\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_internal

¦   ¦       ¦   ¦   ¦   cache.py

¦   ¦       ¦   ¦   ¦   configuration.py

¦   ¦       ¦   ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   ¦   main.py

¦   ¦       ¦   ¦   ¦   pyproject.py

¦   ¦       ¦   ¦   ¦   self\_outdated\_check.py

¦   ¦       ¦   ¦   ¦   wheel\_builder.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---build\_env

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   installer.py

¦   ¦       ¦   ¦   ¦   ¦   noop.py

¦   ¦       ¦   ¦   ¦   ¦   venv.py

¦   ¦       ¦   ¦   ¦   ¦   virtual.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           installer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           noop.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           venv.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           virtual.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---cli

¦   ¦       ¦   ¦   ¦   ¦   autocompletion.py

¦   ¦       ¦   ¦   ¦   ¦   base\_command.py

¦   ¦       ¦   ¦   ¦   ¦   cmdoptions.py

¦   ¦       ¦   ¦   ¦   ¦   command\_context.py

¦   ¦       ¦   ¦   ¦   ¦   index\_command.py

¦   ¦       ¦   ¦   ¦   ¦   main.py

¦   ¦       ¦   ¦   ¦   ¦   main\_parser.py

¦   ¦       ¦   ¦   ¦   ¦   parser.py

¦   ¦       ¦   ¦   ¦   ¦   progress\_bars.py

¦   ¦       ¦   ¦   ¦   ¦   req\_command.py

¦   ¦       ¦   ¦   ¦   ¦   spinners.py

¦   ¦       ¦   ¦   ¦   ¦   status\_codes.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           autocompletion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           base\_command.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           cmdoptions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           command\_context.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           index\_command.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           main.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           main\_parser.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           parser.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           progress\_bars.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           req\_command.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           spinners.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           status\_codes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---commands

¦   ¦       ¦   ¦   ¦   ¦   cache.py

¦   ¦       ¦   ¦   ¦   ¦   check.py

¦   ¦       ¦   ¦   ¦   ¦   completion.py

¦   ¦       ¦   ¦   ¦   ¦   configuration.py

¦   ¦       ¦   ¦   ¦   ¦   debug.py

¦   ¦       ¦   ¦   ¦   ¦   download.py

¦   ¦       ¦   ¦   ¦   ¦   freeze.py

¦   ¦       ¦   ¦   ¦   ¦   hash.py

¦   ¦       ¦   ¦   ¦   ¦   help.py

¦   ¦       ¦   ¦   ¦   ¦   index.py

¦   ¦       ¦   ¦   ¦   ¦   inspect.py

¦   ¦       ¦   ¦   ¦   ¦   install.py

¦   ¦       ¦   ¦   ¦   ¦   list.py

¦   ¦       ¦   ¦   ¦   ¦   lock.py

¦   ¦       ¦   ¦   ¦   ¦   search.py

¦   ¦       ¦   ¦   ¦   ¦   show.py

¦   ¦       ¦   ¦   ¦   ¦   uninstall.py

¦   ¦       ¦   ¦   ¦   ¦   wheel.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           cache.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           check.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           completion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           configuration.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           debug.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           download.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           freeze.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           hash.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           help.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           inspect.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           install.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           list.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           lock.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           search.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           show.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           uninstall.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           wheel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---distributions

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   installed.py

¦   ¦       ¦   ¦   ¦   ¦   sdist.py

¦   ¦       ¦   ¦   ¦   ¦   wheel.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           installed.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           sdist.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           wheel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---index

¦   ¦       ¦   ¦   ¦   ¦   collector.py

¦   ¦       ¦   ¦   ¦   ¦   package\_finder.py

¦   ¦       ¦   ¦   ¦   ¦   sources.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           collector.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           package\_finder.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           sources.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---locations

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   \_distutils.py

¦   ¦       ¦   ¦   ¦   ¦   \_sysconfig.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_distutils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_sysconfig.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---metadata

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   pkg\_resources.py

¦   ¦       ¦   ¦   ¦   ¦   \_json.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---importlib

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_compat.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_dists.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_envs.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_dists.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_envs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pkg\_resources.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_json.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---models

¦   ¦       ¦   ¦   ¦   ¦   candidate.py

¦   ¦       ¦   ¦   ¦   ¦   direct\_url.py

¦   ¦       ¦   ¦   ¦   ¦   format\_control.py

¦   ¦       ¦   ¦   ¦   ¦   index.py

¦   ¦       ¦   ¦   ¦   ¦   installation\_report.py

¦   ¦       ¦   ¦   ¦   ¦   link.py

¦   ¦       ¦   ¦   ¦   ¦   release\_control.py

¦   ¦       ¦   ¦   ¦   ¦   scheme.py

¦   ¦       ¦   ¦   ¦   ¦   search\_scope.py

¦   ¦       ¦   ¦   ¦   ¦   selection\_prefs.py

¦   ¦       ¦   ¦   ¦   ¦   target\_python.py

¦   ¦       ¦   ¦   ¦   ¦   wheel.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           candidate.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           direct\_url.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           format\_control.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           index.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           installation\_report.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           link.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           release\_control.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           scheme.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           search\_scope.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           selection\_prefs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           target\_python.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           wheel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---network

¦   ¦       ¦   ¦   ¦   ¦   auth.py

¦   ¦       ¦   ¦   ¦   ¦   cache.py

¦   ¦       ¦   ¦   ¦   ¦   download.py

¦   ¦       ¦   ¦   ¦   ¦   lazy\_wheel.py

¦   ¦       ¦   ¦   ¦   ¦   session.py

¦   ¦       ¦   ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   ¦   xmlrpc.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           auth.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           cache.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           download.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           lazy\_wheel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           session.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           xmlrpc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---operations

¦   ¦       ¦   ¦   ¦   ¦   check.py

¦   ¦       ¦   ¦   ¦   ¦   freeze.py

¦   ¦       ¦   ¦   ¦   ¦   prepare.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---build

¦   ¦       ¦   ¦   ¦   ¦   ¦   build\_tracker.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   metadata.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   metadata\_editable.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   wheel.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   wheel\_editable.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           build\_tracker.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           metadata.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           metadata\_editable.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           wheel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           wheel\_editable.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---install

¦   ¦       ¦   ¦   ¦   ¦   ¦   wheel.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           wheel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           check.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           freeze.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           prepare.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---req

¦   ¦       ¦   ¦   ¦   ¦   constructors.py

¦   ¦       ¦   ¦   ¦   ¦   pep723.py

¦   ¦       ¦   ¦   ¦   ¦   req\_dependency\_group.py

¦   ¦       ¦   ¦   ¦   ¦   req\_file.py

¦   ¦       ¦   ¦   ¦   ¦   req\_install.py

¦   ¦       ¦   ¦   ¦   ¦   req\_set.py

¦   ¦       ¦   ¦   ¦   ¦   req\_uninstall.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           constructors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pep723.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           req\_dependency\_group.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           req\_file.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           req\_install.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           req\_set.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           req\_uninstall.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---resolution

¦   ¦       ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---legacy

¦   ¦       ¦   ¦   ¦   ¦   ¦   resolver.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           resolver.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---resolvelib

¦   ¦       ¦   ¦   ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   candidates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   factory.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   found\_candidates.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   provider.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   reporter.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   requirements.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   resolver.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           candidates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           factory.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           found\_candidates.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           provider.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           reporter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           requirements.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           resolver.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---utils

¦   ¦       ¦   ¦   ¦   ¦   appdirs.py

¦   ¦       ¦   ¦   ¦   ¦   compat.py

¦   ¦       ¦   ¦   ¦   ¦   compatibility\_tags.py

¦   ¦       ¦   ¦   ¦   ¦   datetime.py

¦   ¦       ¦   ¦   ¦   ¦   deprecation.py

¦   ¦       ¦   ¦   ¦   ¦   direct\_url\_helpers.py

¦   ¦       ¦   ¦   ¦   ¦   egg\_link.py

¦   ¦       ¦   ¦   ¦   ¦   entrypoints.py

¦   ¦       ¦   ¦   ¦   ¦   filesystem.py

¦   ¦       ¦   ¦   ¦   ¦   filetypes.py

¦   ¦       ¦   ¦   ¦   ¦   glibc.py

¦   ¦       ¦   ¦   ¦   ¦   hashes.py

¦   ¦       ¦   ¦   ¦   ¦   logging.py

¦   ¦       ¦   ¦   ¦   ¦   misc.py

¦   ¦       ¦   ¦   ¦   ¦   packaging.py

¦   ¦       ¦   ¦   ¦   ¦   pylock.py

¦   ¦       ¦   ¦   ¦   ¦   retry.py

¦   ¦       ¦   ¦   ¦   ¦   subprocess.py

¦   ¦       ¦   ¦   ¦   ¦   temp\_dir.py

¦   ¦       ¦   ¦   ¦   ¦   unpacking.py

¦   ¦       ¦   ¦   ¦   ¦   urls.py

¦   ¦       ¦   ¦   ¦   ¦   virtualenv.py

¦   ¦       ¦   ¦   ¦   ¦   wheel.py

¦   ¦       ¦   ¦   ¦   ¦   \_jaraco\_text.py

¦   ¦       ¦   ¦   ¦   ¦   \_log.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           appdirs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           compatibility\_tags.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           datetime.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           deprecation.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           direct\_url\_helpers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           egg\_link.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           entrypoints.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           filesystem.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           filetypes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           glibc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           hashes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           logging.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           misc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           packaging.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pylock.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           retry.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           subprocess.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           temp\_dir.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           unpacking.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           urls.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           virtualenv.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           wheel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_jaraco\_text.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_log.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---vcs

¦   ¦       ¦   ¦   ¦   ¦   bazaar.py

¦   ¦       ¦   ¦   ¦   ¦   git.py

¦   ¦       ¦   ¦   ¦   ¦   mercurial.py

¦   ¦       ¦   ¦   ¦   ¦   subversion.py

¦   ¦       ¦   ¦   ¦   ¦   versioncontrol.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           bazaar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           git.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           mercurial.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           subversion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           versioncontrol.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           cache.cpython-314.pyc

¦   ¦       ¦   ¦           configuration.cpython-314.pyc

¦   ¦       ¦   ¦           exceptions.cpython-314.pyc

¦   ¦       ¦   ¦           main.cpython-314.pyc

¦   ¦       ¦   ¦           pyproject.cpython-314.pyc

¦   ¦       ¦   ¦           self\_outdated\_check.cpython-314.pyc

¦   ¦       ¦   ¦           wheel\_builder.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_vendor

¦   ¦       ¦   ¦   ¦   bom.cdx.json

¦   ¦       ¦   ¦   ¦   README.rst

¦   ¦       ¦   ¦   ¦   vendor.txt

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---cachecontrol

¦   ¦       ¦   ¦   ¦   ¦   adapter.py

¦   ¦       ¦   ¦   ¦   ¦   cache.py

¦   ¦       ¦   ¦   ¦   ¦   controller.py

¦   ¦       ¦   ¦   ¦   ¦   filewrapper.py

¦   ¦       ¦   ¦   ¦   ¦   heuristics.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE.txt

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   serialize.py

¦   ¦       ¦   ¦   ¦   ¦   wrapper.py

¦   ¦       ¦   ¦   ¦   ¦   \_cmd.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---caches

¦   ¦       ¦   ¦   ¦   ¦   ¦   file\_cache.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   redis\_cache.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           file\_cache.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           redis\_cache.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           adapter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           cache.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           controller.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           filewrapper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           heuristics.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           serialize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           wrapper.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_cmd.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---certifi

¦   ¦       ¦   ¦   ¦   ¦   cacert.pem

¦   ¦       ¦   ¦   ¦   ¦   core.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           core.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---distlib

¦   ¦       ¦   ¦   ¦   ¦   compat.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE.txt

¦   ¦       ¦   ¦   ¦   ¦   resources.py

¦   ¦       ¦   ¦   ¦   ¦   scripts.py

¦   ¦       ¦   ¦   ¦   ¦   t32.exe

¦   ¦       ¦   ¦   ¦   ¦   t64-arm.exe

¦   ¦       ¦   ¦   ¦   ¦   t64.exe

¦   ¦       ¦   ¦   ¦   ¦   util.py

¦   ¦       ¦   ¦   ¦   ¦   w32.exe

¦   ¦       ¦   ¦   ¦   ¦   w64-arm.exe

¦   ¦       ¦   ¦   ¦   ¦   w64.exe

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           resources.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           scripts.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---distro

¦   ¦       ¦   ¦   ¦   ¦   distro.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           distro.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---idna

¦   ¦       ¦   ¦   ¦   ¦   cli.py

¦   ¦       ¦   ¦   ¦   ¦   codec.py

¦   ¦       ¦   ¦   ¦   ¦   compat.py

¦   ¦       ¦   ¦   ¦   ¦   core.py

¦   ¦       ¦   ¦   ¦   ¦   idnadata.py

¦   ¦       ¦   ¦   ¦   ¦   intranges.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE.md

¦   ¦       ¦   ¦   ¦   ¦   package\_data.py

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   uts46data.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           cli.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           codec.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           core.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           idnadata.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           intranges.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           package\_data.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           uts46data.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---msgpack

¦   ¦       ¦   ¦   ¦   ¦   COPYING

¦   ¦       ¦   ¦   ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   ¦   ¦   ext.py

¦   ¦       ¦   ¦   ¦   ¦   fallback.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           exceptions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           ext.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           fallback.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---packaging

¦   ¦       ¦   ¦   ¦   ¦   dependency\_groups.py

¦   ¦       ¦   ¦   ¦   ¦   direct\_url.py

¦   ¦       ¦   ¦   ¦   ¦   errors.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   LICENSE.APACHE

¦   ¦       ¦   ¦   ¦   ¦   LICENSE.BSD

¦   ¦       ¦   ¦   ¦   ¦   markers.py

¦   ¦       ¦   ¦   ¦   ¦   metadata.py

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   pylock.py

¦   ¦       ¦   ¦   ¦   ¦   requirements.py

¦   ¦       ¦   ¦   ¦   ¦   specifiers.py

¦   ¦       ¦   ¦   ¦   ¦   tags.py

¦   ¦       ¦   ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   ¦   version.py

¦   ¦       ¦   ¦   ¦   ¦   \_elffile.py

¦   ¦       ¦   ¦   ¦   ¦   \_manylinux.py

¦   ¦       ¦   ¦   ¦   ¦   \_musllinux.py

¦   ¦       ¦   ¦   ¦   ¦   \_parser.py

¦   ¦       ¦   ¦   ¦   ¦   \_structures.py

¦   ¦       ¦   ¦   ¦   ¦   \_tokenizer.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---licenses

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_spdx.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_spdx.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           dependency\_groups.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           direct\_url.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           errors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           markers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           metadata.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pylock.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           requirements.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           specifiers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           tags.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           version.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_elffile.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_manylinux.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_musllinux.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_parser.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_structures.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_tokenizer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---pkg\_resources

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---platformdirs

¦   ¦       ¦   ¦   ¦   ¦   android.py

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   macos.py

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   unix.py

¦   ¦       ¦   ¦   ¦   ¦   version.py

¦   ¦       ¦   ¦   ¦   ¦   windows.py

¦   ¦       ¦   ¦   ¦   ¦   \_xdg.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           android.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           macos.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           unix.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           version.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           windows.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_xdg.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---pygments

¦   ¦       ¦   ¦   ¦   ¦   console.py

¦   ¦       ¦   ¦   ¦   ¦   filter.py

¦   ¦       ¦   ¦   ¦   ¦   formatter.py

¦   ¦       ¦   ¦   ¦   ¦   lexer.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   modeline.py

¦   ¦       ¦   ¦   ¦   ¦   plugin.py

¦   ¦       ¦   ¦   ¦   ¦   regexopt.py

¦   ¦       ¦   ¦   ¦   ¦   scanner.py

¦   ¦       ¦   ¦   ¦   ¦   sphinxext.py

¦   ¦       ¦   ¦   ¦   ¦   style.py

¦   ¦       ¦   ¦   ¦   ¦   token.py

¦   ¦       ¦   ¦   ¦   ¦   unistring.py

¦   ¦       ¦   ¦   ¦   ¦   util.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---filters

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---formatters

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_mapping.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_mapping.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---lexers

¦   ¦       ¦   ¦   ¦   ¦   ¦   python.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_mapping.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           python.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_mapping.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---styles

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_mapping.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_mapping.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           console.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           filter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           formatter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           lexer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           modeline.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           plugin.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           regexopt.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           scanner.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           sphinxext.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           style.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           token.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           unistring.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---pyproject\_hooks

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   \_impl.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_in\_process

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_in\_process.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_in\_process.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_impl.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---requests

¦   ¦       ¦   ¦   ¦   ¦   adapters.py

¦   ¦       ¦   ¦   ¦   ¦   api.py

¦   ¦       ¦   ¦   ¦   ¦   auth.py

¦   ¦       ¦   ¦   ¦   ¦   certs.py

¦   ¦       ¦   ¦   ¦   ¦   compat.py

¦   ¦       ¦   ¦   ¦   ¦   cookies.py

¦   ¦       ¦   ¦   ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   ¦   ¦   help.py

¦   ¦       ¦   ¦   ¦   ¦   hooks.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   models.py

¦   ¦       ¦   ¦   ¦   ¦   packages.py

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   sessions.py

¦   ¦       ¦   ¦   ¦   ¦   status\_codes.py

¦   ¦       ¦   ¦   ¦   ¦   structures.py

¦   ¦       ¦   ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   ¦   \_internal\_utils.py

¦   ¦       ¦   ¦   ¦   ¦   \_types.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_version\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           adapters.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           auth.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           certs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           compat.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           cookies.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           exceptions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           help.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           hooks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           models.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           packages.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           sessions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           status\_codes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           structures.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_internal\_utils.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_types.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_version\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---resolvelib

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   providers.py

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   reporters.py

¦   ¦       ¦   ¦   ¦   ¦   structs.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---resolvers

¦   ¦       ¦   ¦   ¦   ¦   ¦   abstract.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   criterion.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   resolution.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           abstract.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           criterion.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           exceptions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           resolution.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           providers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           reporters.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           structs.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---rich

¦   ¦       ¦   ¦   ¦   ¦   abc.py

¦   ¦       ¦   ¦   ¦   ¦   align.py

¦   ¦       ¦   ¦   ¦   ¦   ansi.py

¦   ¦       ¦   ¦   ¦   ¦   bar.py

¦   ¦       ¦   ¦   ¦   ¦   box.py

¦   ¦       ¦   ¦   ¦   ¦   cells.py

¦   ¦       ¦   ¦   ¦   ¦   color.py

¦   ¦       ¦   ¦   ¦   ¦   color\_triplet.py

¦   ¦       ¦   ¦   ¦   ¦   columns.py

¦   ¦       ¦   ¦   ¦   ¦   console.py

¦   ¦       ¦   ¦   ¦   ¦   constrain.py

¦   ¦       ¦   ¦   ¦   ¦   containers.py

¦   ¦       ¦   ¦   ¦   ¦   control.py

¦   ¦       ¦   ¦   ¦   ¦   default\_styles.py

¦   ¦       ¦   ¦   ¦   ¦   diagnose.py

¦   ¦       ¦   ¦   ¦   ¦   emoji.py

¦   ¦       ¦   ¦   ¦   ¦   errors.py

¦   ¦       ¦   ¦   ¦   ¦   filesize.py

¦   ¦       ¦   ¦   ¦   ¦   file\_proxy.py

¦   ¦       ¦   ¦   ¦   ¦   highlighter.py

¦   ¦       ¦   ¦   ¦   ¦   json.py

¦   ¦       ¦   ¦   ¦   ¦   jupyter.py

¦   ¦       ¦   ¦   ¦   ¦   layout.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   live.py

¦   ¦       ¦   ¦   ¦   ¦   live\_render.py

¦   ¦       ¦   ¦   ¦   ¦   logging.py

¦   ¦       ¦   ¦   ¦   ¦   markup.py

¦   ¦       ¦   ¦   ¦   ¦   measure.py

¦   ¦       ¦   ¦   ¦   ¦   padding.py

¦   ¦       ¦   ¦   ¦   ¦   pager.py

¦   ¦       ¦   ¦   ¦   ¦   palette.py

¦   ¦       ¦   ¦   ¦   ¦   panel.py

¦   ¦       ¦   ¦   ¦   ¦   pretty.py

¦   ¦       ¦   ¦   ¦   ¦   progress.py

¦   ¦       ¦   ¦   ¦   ¦   progress\_bar.py

¦   ¦       ¦   ¦   ¦   ¦   prompt.py

¦   ¦       ¦   ¦   ¦   ¦   protocol.py

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   region.py

¦   ¦       ¦   ¦   ¦   ¦   repr.py

¦   ¦       ¦   ¦   ¦   ¦   rule.py

¦   ¦       ¦   ¦   ¦   ¦   scope.py

¦   ¦       ¦   ¦   ¦   ¦   screen.py

¦   ¦       ¦   ¦   ¦   ¦   segment.py

¦   ¦       ¦   ¦   ¦   ¦   spinner.py

¦   ¦       ¦   ¦   ¦   ¦   status.py

¦   ¦       ¦   ¦   ¦   ¦   style.py

¦   ¦       ¦   ¦   ¦   ¦   styled.py

¦   ¦       ¦   ¦   ¦   ¦   syntax.py

¦   ¦       ¦   ¦   ¦   ¦   table.py

¦   ¦       ¦   ¦   ¦   ¦   terminal\_theme.py

¦   ¦       ¦   ¦   ¦   ¦   text.py

¦   ¦       ¦   ¦   ¦   ¦   theme.py

¦   ¦       ¦   ¦   ¦   ¦   themes.py

¦   ¦       ¦   ¦   ¦   ¦   traceback.py

¦   ¦       ¦   ¦   ¦   ¦   tree.py

¦   ¦       ¦   ¦   ¦   ¦   \_cell\_widths.py

¦   ¦       ¦   ¦   ¦   ¦   \_emoji\_codes.py

¦   ¦       ¦   ¦   ¦   ¦   \_emoji\_replace.py

¦   ¦       ¦   ¦   ¦   ¦   \_export\_format.py

¦   ¦       ¦   ¦   ¦   ¦   \_extension.py

¦   ¦       ¦   ¦   ¦   ¦   \_fileno.py

¦   ¦       ¦   ¦   ¦   ¦   \_inspect.py

¦   ¦       ¦   ¦   ¦   ¦   \_log\_render.py

¦   ¦       ¦   ¦   ¦   ¦   \_loop.py

¦   ¦       ¦   ¦   ¦   ¦   \_null\_file.py

¦   ¦       ¦   ¦   ¦   ¦   \_palettes.py

¦   ¦       ¦   ¦   ¦   ¦   \_pick.py

¦   ¦       ¦   ¦   ¦   ¦   \_ratio.py

¦   ¦       ¦   ¦   ¦   ¦   \_spinners.py

¦   ¦       ¦   ¦   ¦   ¦   \_stack.py

¦   ¦       ¦   ¦   ¦   ¦   \_timer.py

¦   ¦       ¦   ¦   ¦   ¦   \_win32\_console.py

¦   ¦       ¦   ¦   ¦   ¦   \_windows.py

¦   ¦       ¦   ¦   ¦   ¦   \_windows\_renderer.py

¦   ¦       ¦   ¦   ¦   ¦   \_wrap.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           abc.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           align.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           ansi.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           bar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           box.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           cells.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           color.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           color\_triplet.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           columns.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           console.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           constrain.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           containers.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           control.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           default\_styles.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           diagnose.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           emoji.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           errors.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           filesize.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           file\_proxy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           highlighter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           json.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           jupyter.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           layout.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           live.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           live\_render.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           logging.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           markup.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           measure.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           padding.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pager.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           palette.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           panel.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           pretty.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           progress.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           progress\_bar.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           prompt.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           protocol.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           region.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           repr.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           rule.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           scope.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           screen.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           segment.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           spinner.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           status.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           style.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           styled.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           syntax.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           table.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           terminal\_theme.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           text.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           theme.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           themes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           traceback.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           tree.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_cell\_widths.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_emoji\_codes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_emoji\_replace.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_export\_format.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_extension.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_fileno.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_inspect.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_log\_render.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_loop.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_null\_file.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_palettes.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_pick.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_ratio.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_spinners.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_stack.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_timer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_win32\_console.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_windows.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_windows\_renderer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_wrap.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---tomli

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   \_parser.py

¦   ¦       ¦   ¦   ¦   ¦   \_re.py

¦   ¦       ¦   ¦   ¦   ¦   \_types.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_parser.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_re.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_types.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---tomli\_w

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   \_writer.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_writer.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---truststore

¦   ¦       ¦   ¦   ¦   ¦   LICENSE

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   \_api.py

¦   ¦       ¦   ¦   ¦   ¦   \_macos.py

¦   ¦       ¦   ¦   ¦   ¦   \_openssl.py

¦   ¦       ¦   ¦   ¦   ¦   \_ssl\_constants.py

¦   ¦       ¦   ¦   ¦   ¦   \_windows.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_api.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_macos.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_openssl.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_ssl\_constants.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_windows.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---urllib3

¦   ¦       ¦   ¦   ¦   ¦   connection.py

¦   ¦       ¦   ¦   ¦   ¦   connectionpool.py

¦   ¦       ¦   ¦   ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   ¦   ¦   fields.py

¦   ¦       ¦   ¦   ¦   ¦   filepost.py

¦   ¦       ¦   ¦   ¦   ¦   LICENSE.txt

¦   ¦       ¦   ¦   ¦   ¦   poolmanager.py

¦   ¦       ¦   ¦   ¦   ¦   py.typed

¦   ¦       ¦   ¦   ¦   ¦   response.py

¦   ¦       ¦   ¦   ¦   ¦   \_base\_connection.py

¦   ¦       ¦   ¦   ¦   ¦   \_collections.py

¦   ¦       ¦   ¦   ¦   ¦   \_request\_methods.py

¦   ¦       ¦   ¦   ¦   ¦   \_version.py

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---contrib

¦   ¦       ¦   ¦   ¦   ¦   ¦   pyopenssl.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   socks.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---emscripten

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   connection.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   emscripten\_fetch\_worker.js

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   fetch.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   request.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   response.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦   ¦           connection.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           fetch.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           request.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           response.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           pyopenssl.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           socks.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---http2

¦   ¦       ¦   ¦   ¦   ¦   ¦   connection.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   probe.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           connection.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           probe.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---util

¦   ¦       ¦   ¦   ¦   ¦   ¦   connection.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   proxy.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   request.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   response.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   retry.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ssltransport.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ssl\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   ssl\_match\_hostname.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   timeout.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   url.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   util.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   wait.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           connection.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           proxy.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           request.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           response.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           retry.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           ssltransport.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           ssl\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           ssl\_match\_hostname.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           timeout.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           url.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           util.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           wait.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           connection.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           connectionpool.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           exceptions.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           fields.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           filepost.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           poolmanager.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           response.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_base\_connection.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_collections.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_request\_methods.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_version.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦           \_\_pip-runner\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---pip-26.2.1.dist-info

¦   ¦       ¦   ¦   entry\_points.txt

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   REQUESTED

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦       ¦   AUTHORS.txt

¦   ¦       ¦       ¦   LICENSE.txt

¦   ¦       ¦       ¦   

¦   ¦       ¦       +---src

¦   ¦       ¦           +---pip

¦   ¦       ¦               +---\_vendor

¦   ¦       ¦                   +---cachecontrol

¦   ¦       ¦                   ¦       LICENSE.txt

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---certifi

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---distlib

¦   ¦       ¦                   ¦       LICENSE.txt

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---distro

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---idna

¦   ¦       ¦                   ¦       LICENSE.md

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---msgpack

¦   ¦       ¦                   ¦       COPYING

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---packaging

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       LICENSE.APACHE

¦   ¦       ¦                   ¦       LICENSE.BSD

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---pkg\_resources

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---platformdirs

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---pygments

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---pyproject\_hooks

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---requests

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---resolvelib

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---rich

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---tomli

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---tomli\_w

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---truststore

¦   ¦       ¦                   ¦       LICENSE

¦   ¦       ¦                   ¦       

¦   ¦       ¦                   +---urllib3

¦   ¦       ¦                           LICENSE.txt

¦   ¦       ¦                           

¦   ¦       +---propcache

¦   ¦       ¦   ¦   api.py

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   \_helpers.py

¦   ¦       ¦   ¦   \_helpers\_c.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   \_helpers\_c.pyx

¦   ¦       ¦   ¦   \_helpers\_py.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           api.cpython-314.pyc

¦   ¦       ¦           \_helpers.cpython-314.pyc

¦   ¦       ¦           \_helpers\_py.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---propcache-0.5.4.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           NOTICE

¦   ¦       ¦           

¦   ¦       +---python\_dateutil-2.9.0.post0.dist-info

¦   ¦       ¦       INSTALLER

¦   ¦       ¦       LICENSE

¦   ¦       ¦       METADATA

¦   ¦       ¦       RECORD

¦   ¦       ¦       top\_level.txt

¦   ¦       ¦       WHEEL

¦   ¦       ¦       zip-safe

¦   ¦       ¦       

¦   ¦       +---python\_dotenv-1.2.3.dist-info

¦   ¦       ¦   ¦   entry\_points.txt

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   REQUESTED

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           

¦   ¦       +---six-1.17.0.dist-info

¦   ¦       ¦       INSTALLER

¦   ¦       ¦       LICENSE

¦   ¦       ¦       METADATA

¦   ¦       ¦       RECORD

¦   ¦       ¦       top\_level.txt

¦   ¦       ¦       WHEEL

¦   ¦       ¦       

¦   ¦       +---tzdata

¦   ¦       ¦   ¦   zones

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---zoneinfo

¦   ¦       ¦   ¦   ¦   CET

¦   ¦       ¦   ¦   ¦   CST6CDT

¦   ¦       ¦   ¦   ¦   Cuba

¦   ¦       ¦   ¦   ¦   EET

¦   ¦       ¦   ¦   ¦   Egypt

¦   ¦       ¦   ¦   ¦   Eire

¦   ¦       ¦   ¦   ¦   EST

¦   ¦       ¦   ¦   ¦   EST5EDT

¦   ¦       ¦   ¦   ¦   Factory

¦   ¦       ¦   ¦   ¦   GB

¦   ¦       ¦   ¦   ¦   GB-Eire

¦   ¦       ¦   ¦   ¦   GMT

¦   ¦       ¦   ¦   ¦   GMT+0

¦   ¦       ¦   ¦   ¦   GMT-0

¦   ¦       ¦   ¦   ¦   GMT0

¦   ¦       ¦   ¦   ¦   Greenwich

¦   ¦       ¦   ¦   ¦   Hongkong

¦   ¦       ¦   ¦   ¦   HST

¦   ¦       ¦   ¦   ¦   Iceland

¦   ¦       ¦   ¦   ¦   Iran

¦   ¦       ¦   ¦   ¦   iso3166.tab

¦   ¦       ¦   ¦   ¦   Israel

¦   ¦       ¦   ¦   ¦   Jamaica

¦   ¦       ¦   ¦   ¦   Japan

¦   ¦       ¦   ¦   ¦   Kwajalein

¦   ¦       ¦   ¦   ¦   leapseconds

¦   ¦       ¦   ¦   ¦   Libya

¦   ¦       ¦   ¦   ¦   MET

¦   ¦       ¦   ¦   ¦   MST

¦   ¦       ¦   ¦   ¦   MST7MDT

¦   ¦       ¦   ¦   ¦   Navajo

¦   ¦       ¦   ¦   ¦   NZ

¦   ¦       ¦   ¦   ¦   NZ-CHAT

¦   ¦       ¦   ¦   ¦   Poland

¦   ¦       ¦   ¦   ¦   Portugal

¦   ¦       ¦   ¦   ¦   PRC

¦   ¦       ¦   ¦   ¦   PST8PDT

¦   ¦       ¦   ¦   ¦   ROC

¦   ¦       ¦   ¦   ¦   ROK

¦   ¦       ¦   ¦   ¦   Singapore

¦   ¦       ¦   ¦   ¦   Turkey

¦   ¦       ¦   ¦   ¦   tzdata.zi

¦   ¦       ¦   ¦   ¦   UCT

¦   ¦       ¦   ¦   ¦   Universal

¦   ¦       ¦   ¦   ¦   UTC

¦   ¦       ¦   ¦   ¦   W-SU

¦   ¦       ¦   ¦   ¦   WET

¦   ¦       ¦   ¦   ¦   zone.tab

¦   ¦       ¦   ¦   ¦   zone1970.tab

¦   ¦       ¦   ¦   ¦   zonenow.tab

¦   ¦       ¦   ¦   ¦   Zulu

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---Africa

¦   ¦       ¦   ¦   ¦   ¦   Abidjan

¦   ¦       ¦   ¦   ¦   ¦   Accra

¦   ¦       ¦   ¦   ¦   ¦   Addis\_Ababa

¦   ¦       ¦   ¦   ¦   ¦   Algiers

¦   ¦       ¦   ¦   ¦   ¦   Asmara

¦   ¦       ¦   ¦   ¦   ¦   Asmera

¦   ¦       ¦   ¦   ¦   ¦   Bamako

¦   ¦       ¦   ¦   ¦   ¦   Bangui

¦   ¦       ¦   ¦   ¦   ¦   Banjul

¦   ¦       ¦   ¦   ¦   ¦   Bissau

¦   ¦       ¦   ¦   ¦   ¦   Blantyre

¦   ¦       ¦   ¦   ¦   ¦   Brazzaville

¦   ¦       ¦   ¦   ¦   ¦   Bujumbura

¦   ¦       ¦   ¦   ¦   ¦   Cairo

¦   ¦       ¦   ¦   ¦   ¦   Casablanca

¦   ¦       ¦   ¦   ¦   ¦   Ceuta

¦   ¦       ¦   ¦   ¦   ¦   Conakry

¦   ¦       ¦   ¦   ¦   ¦   Dakar

¦   ¦       ¦   ¦   ¦   ¦   Dar\_es\_Salaam

¦   ¦       ¦   ¦   ¦   ¦   Djibouti

¦   ¦       ¦   ¦   ¦   ¦   Douala

¦   ¦       ¦   ¦   ¦   ¦   El\_Aaiun

¦   ¦       ¦   ¦   ¦   ¦   Freetown

¦   ¦       ¦   ¦   ¦   ¦   Gaborone

¦   ¦       ¦   ¦   ¦   ¦   Harare

¦   ¦       ¦   ¦   ¦   ¦   Johannesburg

¦   ¦       ¦   ¦   ¦   ¦   Juba

¦   ¦       ¦   ¦   ¦   ¦   Kampala

¦   ¦       ¦   ¦   ¦   ¦   Khartoum

¦   ¦       ¦   ¦   ¦   ¦   Kigali

¦   ¦       ¦   ¦   ¦   ¦   Kinshasa

¦   ¦       ¦   ¦   ¦   ¦   Lagos

¦   ¦       ¦   ¦   ¦   ¦   Libreville

¦   ¦       ¦   ¦   ¦   ¦   Lome

¦   ¦       ¦   ¦   ¦   ¦   Luanda

¦   ¦       ¦   ¦   ¦   ¦   Lubumbashi

¦   ¦       ¦   ¦   ¦   ¦   Lusaka

¦   ¦       ¦   ¦   ¦   ¦   Malabo

¦   ¦       ¦   ¦   ¦   ¦   Maputo

¦   ¦       ¦   ¦   ¦   ¦   Maseru

¦   ¦       ¦   ¦   ¦   ¦   Mbabane

¦   ¦       ¦   ¦   ¦   ¦   Mogadishu

¦   ¦       ¦   ¦   ¦   ¦   Monrovia

¦   ¦       ¦   ¦   ¦   ¦   Nairobi

¦   ¦       ¦   ¦   ¦   ¦   Ndjamena

¦   ¦       ¦   ¦   ¦   ¦   Niamey

¦   ¦       ¦   ¦   ¦   ¦   Nouakchott

¦   ¦       ¦   ¦   ¦   ¦   Ouagadougou

¦   ¦       ¦   ¦   ¦   ¦   Porto-Novo

¦   ¦       ¦   ¦   ¦   ¦   Sao\_Tome

¦   ¦       ¦   ¦   ¦   ¦   Timbuktu

¦   ¦       ¦   ¦   ¦   ¦   Tripoli

¦   ¦       ¦   ¦   ¦   ¦   Tunis

¦   ¦       ¦   ¦   ¦   ¦   Windhoek

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---America

¦   ¦       ¦   ¦   ¦   ¦   Adak

¦   ¦       ¦   ¦   ¦   ¦   Anchorage

¦   ¦       ¦   ¦   ¦   ¦   Anguilla

¦   ¦       ¦   ¦   ¦   ¦   Antigua

¦   ¦       ¦   ¦   ¦   ¦   Araguaina

¦   ¦       ¦   ¦   ¦   ¦   Aruba

¦   ¦       ¦   ¦   ¦   ¦   Asuncion

¦   ¦       ¦   ¦   ¦   ¦   Atikokan

¦   ¦       ¦   ¦   ¦   ¦   Atka

¦   ¦       ¦   ¦   ¦   ¦   Bahia

¦   ¦       ¦   ¦   ¦   ¦   Bahia\_Banderas

¦   ¦       ¦   ¦   ¦   ¦   Barbados

¦   ¦       ¦   ¦   ¦   ¦   Belem

¦   ¦       ¦   ¦   ¦   ¦   Belize

¦   ¦       ¦   ¦   ¦   ¦   Blanc-Sablon

¦   ¦       ¦   ¦   ¦   ¦   Boa\_Vista

¦   ¦       ¦   ¦   ¦   ¦   Bogota

¦   ¦       ¦   ¦   ¦   ¦   Boise

¦   ¦       ¦   ¦   ¦   ¦   Buenos\_Aires

¦   ¦       ¦   ¦   ¦   ¦   Cambridge\_Bay

¦   ¦       ¦   ¦   ¦   ¦   Campo\_Grande

¦   ¦       ¦   ¦   ¦   ¦   Cancun

¦   ¦       ¦   ¦   ¦   ¦   Caracas

¦   ¦       ¦   ¦   ¦   ¦   Catamarca

¦   ¦       ¦   ¦   ¦   ¦   Cayenne

¦   ¦       ¦   ¦   ¦   ¦   Cayman

¦   ¦       ¦   ¦   ¦   ¦   Chicago

¦   ¦       ¦   ¦   ¦   ¦   Chihuahua

¦   ¦       ¦   ¦   ¦   ¦   Ciudad\_Juarez

¦   ¦       ¦   ¦   ¦   ¦   Coral\_Harbour

¦   ¦       ¦   ¦   ¦   ¦   Cordoba

¦   ¦       ¦   ¦   ¦   ¦   Costa\_Rica

¦   ¦       ¦   ¦   ¦   ¦   Coyhaique

¦   ¦       ¦   ¦   ¦   ¦   Creston

¦   ¦       ¦   ¦   ¦   ¦   Cuiaba

¦   ¦       ¦   ¦   ¦   ¦   Curacao

¦   ¦       ¦   ¦   ¦   ¦   Danmarkshavn

¦   ¦       ¦   ¦   ¦   ¦   Dawson

¦   ¦       ¦   ¦   ¦   ¦   Dawson\_Creek

¦   ¦       ¦   ¦   ¦   ¦   Denver

¦   ¦       ¦   ¦   ¦   ¦   Detroit

¦   ¦       ¦   ¦   ¦   ¦   Dominica

¦   ¦       ¦   ¦   ¦   ¦   Edmonton

¦   ¦       ¦   ¦   ¦   ¦   Eirunepe

¦   ¦       ¦   ¦   ¦   ¦   El\_Salvador

¦   ¦       ¦   ¦   ¦   ¦   Ensenada

¦   ¦       ¦   ¦   ¦   ¦   Fortaleza

¦   ¦       ¦   ¦   ¦   ¦   Fort\_Nelson

¦   ¦       ¦   ¦   ¦   ¦   Fort\_Wayne

¦   ¦       ¦   ¦   ¦   ¦   Glace\_Bay

¦   ¦       ¦   ¦   ¦   ¦   Godthab

¦   ¦       ¦   ¦   ¦   ¦   Goose\_Bay

¦   ¦       ¦   ¦   ¦   ¦   Grand\_Turk

¦   ¦       ¦   ¦   ¦   ¦   Grenada

¦   ¦       ¦   ¦   ¦   ¦   Guadeloupe

¦   ¦       ¦   ¦   ¦   ¦   Guatemala

¦   ¦       ¦   ¦   ¦   ¦   Guayaquil

¦   ¦       ¦   ¦   ¦   ¦   Guyana

¦   ¦       ¦   ¦   ¦   ¦   Halifax

¦   ¦       ¦   ¦   ¦   ¦   Havana

¦   ¦       ¦   ¦   ¦   ¦   Hermosillo

¦   ¦       ¦   ¦   ¦   ¦   Indianapolis

¦   ¦       ¦   ¦   ¦   ¦   Inuvik

¦   ¦       ¦   ¦   ¦   ¦   Iqaluit

¦   ¦       ¦   ¦   ¦   ¦   Jamaica

¦   ¦       ¦   ¦   ¦   ¦   Jujuy

¦   ¦       ¦   ¦   ¦   ¦   Juneau

¦   ¦       ¦   ¦   ¦   ¦   Knox\_IN

¦   ¦       ¦   ¦   ¦   ¦   Kralendijk

¦   ¦       ¦   ¦   ¦   ¦   La\_Paz

¦   ¦       ¦   ¦   ¦   ¦   Lima

¦   ¦       ¦   ¦   ¦   ¦   Los\_Angeles

¦   ¦       ¦   ¦   ¦   ¦   Louisville

¦   ¦       ¦   ¦   ¦   ¦   Lower\_Princes

¦   ¦       ¦   ¦   ¦   ¦   Maceio

¦   ¦       ¦   ¦   ¦   ¦   Managua

¦   ¦       ¦   ¦   ¦   ¦   Manaus

¦   ¦       ¦   ¦   ¦   ¦   Marigot

¦   ¦       ¦   ¦   ¦   ¦   Martinique

¦   ¦       ¦   ¦   ¦   ¦   Matamoros

¦   ¦       ¦   ¦   ¦   ¦   Mazatlan

¦   ¦       ¦   ¦   ¦   ¦   Mendoza

¦   ¦       ¦   ¦   ¦   ¦   Menominee

¦   ¦       ¦   ¦   ¦   ¦   Merida

¦   ¦       ¦   ¦   ¦   ¦   Metlakatla

¦   ¦       ¦   ¦   ¦   ¦   Mexico\_City

¦   ¦       ¦   ¦   ¦   ¦   Miquelon

¦   ¦       ¦   ¦   ¦   ¦   Moncton

¦   ¦       ¦   ¦   ¦   ¦   Monterrey

¦   ¦       ¦   ¦   ¦   ¦   Montevideo

¦   ¦       ¦   ¦   ¦   ¦   Montreal

¦   ¦       ¦   ¦   ¦   ¦   Montserrat

¦   ¦       ¦   ¦   ¦   ¦   Nassau

¦   ¦       ¦   ¦   ¦   ¦   New\_York

¦   ¦       ¦   ¦   ¦   ¦   Nipigon

¦   ¦       ¦   ¦   ¦   ¦   Nome

¦   ¦       ¦   ¦   ¦   ¦   Noronha

¦   ¦       ¦   ¦   ¦   ¦   Nuuk

¦   ¦       ¦   ¦   ¦   ¦   Ojinaga

¦   ¦       ¦   ¦   ¦   ¦   Panama

¦   ¦       ¦   ¦   ¦   ¦   Pangnirtung

¦   ¦       ¦   ¦   ¦   ¦   Paramaribo

¦   ¦       ¦   ¦   ¦   ¦   Phoenix

¦   ¦       ¦   ¦   ¦   ¦   Port-au-Prince

¦   ¦       ¦   ¦   ¦   ¦   Porto\_Acre

¦   ¦       ¦   ¦   ¦   ¦   Porto\_Velho

¦   ¦       ¦   ¦   ¦   ¦   Port\_of\_Spain

¦   ¦       ¦   ¦   ¦   ¦   Puerto\_Rico

¦   ¦       ¦   ¦   ¦   ¦   Punta\_Arenas

¦   ¦       ¦   ¦   ¦   ¦   Rainy\_River

¦   ¦       ¦   ¦   ¦   ¦   Rankin\_Inlet

¦   ¦       ¦   ¦   ¦   ¦   Recife

¦   ¦       ¦   ¦   ¦   ¦   Regina

¦   ¦       ¦   ¦   ¦   ¦   Resolute

¦   ¦       ¦   ¦   ¦   ¦   Rio\_Branco

¦   ¦       ¦   ¦   ¦   ¦   Rosario

¦   ¦       ¦   ¦   ¦   ¦   Santarem

¦   ¦       ¦   ¦   ¦   ¦   Santa\_Isabel

¦   ¦       ¦   ¦   ¦   ¦   Santiago

¦   ¦       ¦   ¦   ¦   ¦   Santo\_Domingo

¦   ¦       ¦   ¦   ¦   ¦   Sao\_Paulo

¦   ¦       ¦   ¦   ¦   ¦   Scoresbysund

¦   ¦       ¦   ¦   ¦   ¦   Shiprock

¦   ¦       ¦   ¦   ¦   ¦   Sitka

¦   ¦       ¦   ¦   ¦   ¦   St\_Barthelemy

¦   ¦       ¦   ¦   ¦   ¦   St\_Johns

¦   ¦       ¦   ¦   ¦   ¦   St\_Kitts

¦   ¦       ¦   ¦   ¦   ¦   St\_Lucia

¦   ¦       ¦   ¦   ¦   ¦   St\_Thomas

¦   ¦       ¦   ¦   ¦   ¦   St\_Vincent

¦   ¦       ¦   ¦   ¦   ¦   Swift\_Current

¦   ¦       ¦   ¦   ¦   ¦   Tegucigalpa

¦   ¦       ¦   ¦   ¦   ¦   Thule

¦   ¦       ¦   ¦   ¦   ¦   Thunder\_Bay

¦   ¦       ¦   ¦   ¦   ¦   Tijuana

¦   ¦       ¦   ¦   ¦   ¦   Toronto

¦   ¦       ¦   ¦   ¦   ¦   Tortola

¦   ¦       ¦   ¦   ¦   ¦   Vancouver

¦   ¦       ¦   ¦   ¦   ¦   Virgin

¦   ¦       ¦   ¦   ¦   ¦   Whitehorse

¦   ¦       ¦   ¦   ¦   ¦   Winnipeg

¦   ¦       ¦   ¦   ¦   ¦   Yakutat

¦   ¦       ¦   ¦   ¦   ¦   Yellowknife

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---Argentina

¦   ¦       ¦   ¦   ¦   ¦   ¦   Buenos\_Aires

¦   ¦       ¦   ¦   ¦   ¦   ¦   Catamarca

¦   ¦       ¦   ¦   ¦   ¦   ¦   ComodRivadavia

¦   ¦       ¦   ¦   ¦   ¦   ¦   Cordoba

¦   ¦       ¦   ¦   ¦   ¦   ¦   Jujuy

¦   ¦       ¦   ¦   ¦   ¦   ¦   La\_Rioja

¦   ¦       ¦   ¦   ¦   ¦   ¦   Mendoza

¦   ¦       ¦   ¦   ¦   ¦   ¦   Rio\_Gallegos

¦   ¦       ¦   ¦   ¦   ¦   ¦   Salta

¦   ¦       ¦   ¦   ¦   ¦   ¦   San\_Juan

¦   ¦       ¦   ¦   ¦   ¦   ¦   San\_Luis

¦   ¦       ¦   ¦   ¦   ¦   ¦   Tucuman

¦   ¦       ¦   ¦   ¦   ¦   ¦   Ushuaia

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---Indiana

¦   ¦       ¦   ¦   ¦   ¦   ¦   Indianapolis

¦   ¦       ¦   ¦   ¦   ¦   ¦   Knox

¦   ¦       ¦   ¦   ¦   ¦   ¦   Marengo

¦   ¦       ¦   ¦   ¦   ¦   ¦   Petersburg

¦   ¦       ¦   ¦   ¦   ¦   ¦   Tell\_City

¦   ¦       ¦   ¦   ¦   ¦   ¦   Vevay

¦   ¦       ¦   ¦   ¦   ¦   ¦   Vincennes

¦   ¦       ¦   ¦   ¦   ¦   ¦   Winamac

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---Kentucky

¦   ¦       ¦   ¦   ¦   ¦   ¦   Louisville

¦   ¦       ¦   ¦   ¦   ¦   ¦   Monticello

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---North\_Dakota

¦   ¦       ¦   ¦   ¦   ¦   ¦   Beulah

¦   ¦       ¦   ¦   ¦   ¦   ¦   Center

¦   ¦       ¦   ¦   ¦   ¦   ¦   New\_Salem

¦   ¦       ¦   ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦   ¦           

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Antarctica

¦   ¦       ¦   ¦   ¦   ¦   Casey

¦   ¦       ¦   ¦   ¦   ¦   Davis

¦   ¦       ¦   ¦   ¦   ¦   DumontDUrville

¦   ¦       ¦   ¦   ¦   ¦   Macquarie

¦   ¦       ¦   ¦   ¦   ¦   Mawson

¦   ¦       ¦   ¦   ¦   ¦   McMurdo

¦   ¦       ¦   ¦   ¦   ¦   Palmer

¦   ¦       ¦   ¦   ¦   ¦   Rothera

¦   ¦       ¦   ¦   ¦   ¦   South\_Pole

¦   ¦       ¦   ¦   ¦   ¦   Syowa

¦   ¦       ¦   ¦   ¦   ¦   Troll

¦   ¦       ¦   ¦   ¦   ¦   Vostok

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Arctic

¦   ¦       ¦   ¦   ¦   ¦   Longyearbyen

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Asia

¦   ¦       ¦   ¦   ¦   ¦   Aden

¦   ¦       ¦   ¦   ¦   ¦   Almaty

¦   ¦       ¦   ¦   ¦   ¦   Amman

¦   ¦       ¦   ¦   ¦   ¦   Anadyr

¦   ¦       ¦   ¦   ¦   ¦   Aqtau

¦   ¦       ¦   ¦   ¦   ¦   Aqtobe

¦   ¦       ¦   ¦   ¦   ¦   Ashgabat

¦   ¦       ¦   ¦   ¦   ¦   Ashkhabad

¦   ¦       ¦   ¦   ¦   ¦   Atyrau

¦   ¦       ¦   ¦   ¦   ¦   Baghdad

¦   ¦       ¦   ¦   ¦   ¦   Bahrain

¦   ¦       ¦   ¦   ¦   ¦   Baku

¦   ¦       ¦   ¦   ¦   ¦   Bangkok

¦   ¦       ¦   ¦   ¦   ¦   Barnaul

¦   ¦       ¦   ¦   ¦   ¦   Beirut

¦   ¦       ¦   ¦   ¦   ¦   Bishkek

¦   ¦       ¦   ¦   ¦   ¦   Brunei

¦   ¦       ¦   ¦   ¦   ¦   Calcutta

¦   ¦       ¦   ¦   ¦   ¦   Chita

¦   ¦       ¦   ¦   ¦   ¦   Choibalsan

¦   ¦       ¦   ¦   ¦   ¦   Chongqing

¦   ¦       ¦   ¦   ¦   ¦   Chungking

¦   ¦       ¦   ¦   ¦   ¦   Colombo

¦   ¦       ¦   ¦   ¦   ¦   Dacca

¦   ¦       ¦   ¦   ¦   ¦   Damascus

¦   ¦       ¦   ¦   ¦   ¦   Dhaka

¦   ¦       ¦   ¦   ¦   ¦   Dili

¦   ¦       ¦   ¦   ¦   ¦   Dubai

¦   ¦       ¦   ¦   ¦   ¦   Dushanbe

¦   ¦       ¦   ¦   ¦   ¦   Famagusta

¦   ¦       ¦   ¦   ¦   ¦   Gaza

¦   ¦       ¦   ¦   ¦   ¦   Harbin

¦   ¦       ¦   ¦   ¦   ¦   Hebron

¦   ¦       ¦   ¦   ¦   ¦   Hong\_Kong

¦   ¦       ¦   ¦   ¦   ¦   Hovd

¦   ¦       ¦   ¦   ¦   ¦   Ho\_Chi\_Minh

¦   ¦       ¦   ¦   ¦   ¦   Irkutsk

¦   ¦       ¦   ¦   ¦   ¦   Istanbul

¦   ¦       ¦   ¦   ¦   ¦   Jakarta

¦   ¦       ¦   ¦   ¦   ¦   Jayapura

¦   ¦       ¦   ¦   ¦   ¦   Jerusalem

¦   ¦       ¦   ¦   ¦   ¦   Kabul

¦   ¦       ¦   ¦   ¦   ¦   Kamchatka

¦   ¦       ¦   ¦   ¦   ¦   Karachi

¦   ¦       ¦   ¦   ¦   ¦   Kashgar

¦   ¦       ¦   ¦   ¦   ¦   Kathmandu

¦   ¦       ¦   ¦   ¦   ¦   Katmandu

¦   ¦       ¦   ¦   ¦   ¦   Khandyga

¦   ¦       ¦   ¦   ¦   ¦   Kolkata

¦   ¦       ¦   ¦   ¦   ¦   Krasnoyarsk

¦   ¦       ¦   ¦   ¦   ¦   Kuala\_Lumpur

¦   ¦       ¦   ¦   ¦   ¦   Kuching

¦   ¦       ¦   ¦   ¦   ¦   Kuwait

¦   ¦       ¦   ¦   ¦   ¦   Macao

¦   ¦       ¦   ¦   ¦   ¦   Macau

¦   ¦       ¦   ¦   ¦   ¦   Magadan

¦   ¦       ¦   ¦   ¦   ¦   Makassar

¦   ¦       ¦   ¦   ¦   ¦   Manila

¦   ¦       ¦   ¦   ¦   ¦   Muscat

¦   ¦       ¦   ¦   ¦   ¦   Nicosia

¦   ¦       ¦   ¦   ¦   ¦   Novokuznetsk

¦   ¦       ¦   ¦   ¦   ¦   Novosibirsk

¦   ¦       ¦   ¦   ¦   ¦   Omsk

¦   ¦       ¦   ¦   ¦   ¦   Oral

¦   ¦       ¦   ¦   ¦   ¦   Phnom\_Penh

¦   ¦       ¦   ¦   ¦   ¦   Pontianak

¦   ¦       ¦   ¦   ¦   ¦   Pyongyang

¦   ¦       ¦   ¦   ¦   ¦   Qatar

¦   ¦       ¦   ¦   ¦   ¦   Qostanay

¦   ¦       ¦   ¦   ¦   ¦   Qyzylorda

¦   ¦       ¦   ¦   ¦   ¦   Rangoon

¦   ¦       ¦   ¦   ¦   ¦   Riyadh

¦   ¦       ¦   ¦   ¦   ¦   Saigon

¦   ¦       ¦   ¦   ¦   ¦   Sakhalin

¦   ¦       ¦   ¦   ¦   ¦   Samarkand

¦   ¦       ¦   ¦   ¦   ¦   Seoul

¦   ¦       ¦   ¦   ¦   ¦   Shanghai

¦   ¦       ¦   ¦   ¦   ¦   Singapore

¦   ¦       ¦   ¦   ¦   ¦   Srednekolymsk

¦   ¦       ¦   ¦   ¦   ¦   Taipei

¦   ¦       ¦   ¦   ¦   ¦   Tashkent

¦   ¦       ¦   ¦   ¦   ¦   Tbilisi

¦   ¦       ¦   ¦   ¦   ¦   Tehran

¦   ¦       ¦   ¦   ¦   ¦   Tel\_Aviv

¦   ¦       ¦   ¦   ¦   ¦   Thimbu

¦   ¦       ¦   ¦   ¦   ¦   Thimphu

¦   ¦       ¦   ¦   ¦   ¦   Tokyo

¦   ¦       ¦   ¦   ¦   ¦   Tomsk

¦   ¦       ¦   ¦   ¦   ¦   Ujung\_Pandang

¦   ¦       ¦   ¦   ¦   ¦   Ulaanbaatar

¦   ¦       ¦   ¦   ¦   ¦   Ulan\_Bator

¦   ¦       ¦   ¦   ¦   ¦   Urumqi

¦   ¦       ¦   ¦   ¦   ¦   Ust-Nera

¦   ¦       ¦   ¦   ¦   ¦   Vientiane

¦   ¦       ¦   ¦   ¦   ¦   Vladivostok

¦   ¦       ¦   ¦   ¦   ¦   Yakutsk

¦   ¦       ¦   ¦   ¦   ¦   Yangon

¦   ¦       ¦   ¦   ¦   ¦   Yekaterinburg

¦   ¦       ¦   ¦   ¦   ¦   Yerevan

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Atlantic

¦   ¦       ¦   ¦   ¦   ¦   Azores

¦   ¦       ¦   ¦   ¦   ¦   Bermuda

¦   ¦       ¦   ¦   ¦   ¦   Canary

¦   ¦       ¦   ¦   ¦   ¦   Cape\_Verde

¦   ¦       ¦   ¦   ¦   ¦   Faeroe

¦   ¦       ¦   ¦   ¦   ¦   Faroe

¦   ¦       ¦   ¦   ¦   ¦   Jan\_Mayen

¦   ¦       ¦   ¦   ¦   ¦   Madeira

¦   ¦       ¦   ¦   ¦   ¦   Reykjavik

¦   ¦       ¦   ¦   ¦   ¦   South\_Georgia

¦   ¦       ¦   ¦   ¦   ¦   Stanley

¦   ¦       ¦   ¦   ¦   ¦   St\_Helena

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Australia

¦   ¦       ¦   ¦   ¦   ¦   ACT

¦   ¦       ¦   ¦   ¦   ¦   Adelaide

¦   ¦       ¦   ¦   ¦   ¦   Brisbane

¦   ¦       ¦   ¦   ¦   ¦   Broken\_Hill

¦   ¦       ¦   ¦   ¦   ¦   Canberra

¦   ¦       ¦   ¦   ¦   ¦   Currie

¦   ¦       ¦   ¦   ¦   ¦   Darwin

¦   ¦       ¦   ¦   ¦   ¦   Eucla

¦   ¦       ¦   ¦   ¦   ¦   Hobart

¦   ¦       ¦   ¦   ¦   ¦   LHI

¦   ¦       ¦   ¦   ¦   ¦   Lindeman

¦   ¦       ¦   ¦   ¦   ¦   Lord\_Howe

¦   ¦       ¦   ¦   ¦   ¦   Melbourne

¦   ¦       ¦   ¦   ¦   ¦   North

¦   ¦       ¦   ¦   ¦   ¦   NSW

¦   ¦       ¦   ¦   ¦   ¦   Perth

¦   ¦       ¦   ¦   ¦   ¦   Queensland

¦   ¦       ¦   ¦   ¦   ¦   South

¦   ¦       ¦   ¦   ¦   ¦   Sydney

¦   ¦       ¦   ¦   ¦   ¦   Tasmania

¦   ¦       ¦   ¦   ¦   ¦   Victoria

¦   ¦       ¦   ¦   ¦   ¦   West

¦   ¦       ¦   ¦   ¦   ¦   Yancowinna

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Brazil

¦   ¦       ¦   ¦   ¦   ¦   Acre

¦   ¦       ¦   ¦   ¦   ¦   DeNoronha

¦   ¦       ¦   ¦   ¦   ¦   East

¦   ¦       ¦   ¦   ¦   ¦   West

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Canada

¦   ¦       ¦   ¦   ¦   ¦   Atlantic

¦   ¦       ¦   ¦   ¦   ¦   Central

¦   ¦       ¦   ¦   ¦   ¦   Eastern

¦   ¦       ¦   ¦   ¦   ¦   Mountain

¦   ¦       ¦   ¦   ¦   ¦   Newfoundland

¦   ¦       ¦   ¦   ¦   ¦   Pacific

¦   ¦       ¦   ¦   ¦   ¦   Saskatchewan

¦   ¦       ¦   ¦   ¦   ¦   Yukon

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Chile

¦   ¦       ¦   ¦   ¦   ¦   Continental

¦   ¦       ¦   ¦   ¦   ¦   EasterIsland

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Etc

¦   ¦       ¦   ¦   ¦   ¦   GMT

¦   ¦       ¦   ¦   ¦   ¦   GMT+0

¦   ¦       ¦   ¦   ¦   ¦   GMT+1

¦   ¦       ¦   ¦   ¦   ¦   GMT+10

¦   ¦       ¦   ¦   ¦   ¦   GMT+11

¦   ¦       ¦   ¦   ¦   ¦   GMT+12

¦   ¦       ¦   ¦   ¦   ¦   GMT+2

¦   ¦       ¦   ¦   ¦   ¦   GMT+3

¦   ¦       ¦   ¦   ¦   ¦   GMT+4

¦   ¦       ¦   ¦   ¦   ¦   GMT+5

¦   ¦       ¦   ¦   ¦   ¦   GMT+6

¦   ¦       ¦   ¦   ¦   ¦   GMT+7

¦   ¦       ¦   ¦   ¦   ¦   GMT+8

¦   ¦       ¦   ¦   ¦   ¦   GMT+9

¦   ¦       ¦   ¦   ¦   ¦   GMT-0

¦   ¦       ¦   ¦   ¦   ¦   GMT-1

¦   ¦       ¦   ¦   ¦   ¦   GMT-10

¦   ¦       ¦   ¦   ¦   ¦   GMT-11

¦   ¦       ¦   ¦   ¦   ¦   GMT-12

¦   ¦       ¦   ¦   ¦   ¦   GMT-13

¦   ¦       ¦   ¦   ¦   ¦   GMT-14

¦   ¦       ¦   ¦   ¦   ¦   GMT-2

¦   ¦       ¦   ¦   ¦   ¦   GMT-3

¦   ¦       ¦   ¦   ¦   ¦   GMT-4

¦   ¦       ¦   ¦   ¦   ¦   GMT-5

¦   ¦       ¦   ¦   ¦   ¦   GMT-6

¦   ¦       ¦   ¦   ¦   ¦   GMT-7

¦   ¦       ¦   ¦   ¦   ¦   GMT-8

¦   ¦       ¦   ¦   ¦   ¦   GMT-9

¦   ¦       ¦   ¦   ¦   ¦   GMT0

¦   ¦       ¦   ¦   ¦   ¦   Greenwich

¦   ¦       ¦   ¦   ¦   ¦   UCT

¦   ¦       ¦   ¦   ¦   ¦   Universal

¦   ¦       ¦   ¦   ¦   ¦   UTC

¦   ¦       ¦   ¦   ¦   ¦   Zulu

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Europe

¦   ¦       ¦   ¦   ¦   ¦   Amsterdam

¦   ¦       ¦   ¦   ¦   ¦   Andorra

¦   ¦       ¦   ¦   ¦   ¦   Astrakhan

¦   ¦       ¦   ¦   ¦   ¦   Athens

¦   ¦       ¦   ¦   ¦   ¦   Belfast

¦   ¦       ¦   ¦   ¦   ¦   Belgrade

¦   ¦       ¦   ¦   ¦   ¦   Berlin

¦   ¦       ¦   ¦   ¦   ¦   Bratislava

¦   ¦       ¦   ¦   ¦   ¦   Brussels

¦   ¦       ¦   ¦   ¦   ¦   Bucharest

¦   ¦       ¦   ¦   ¦   ¦   Budapest

¦   ¦       ¦   ¦   ¦   ¦   Busingen

¦   ¦       ¦   ¦   ¦   ¦   Chisinau

¦   ¦       ¦   ¦   ¦   ¦   Copenhagen

¦   ¦       ¦   ¦   ¦   ¦   Dublin

¦   ¦       ¦   ¦   ¦   ¦   Gibraltar

¦   ¦       ¦   ¦   ¦   ¦   Guernsey

¦   ¦       ¦   ¦   ¦   ¦   Helsinki

¦   ¦       ¦   ¦   ¦   ¦   Isle\_of\_Man

¦   ¦       ¦   ¦   ¦   ¦   Istanbul

¦   ¦       ¦   ¦   ¦   ¦   Jersey

¦   ¦       ¦   ¦   ¦   ¦   Kaliningrad

¦   ¦       ¦   ¦   ¦   ¦   Kiev

¦   ¦       ¦   ¦   ¦   ¦   Kirov

¦   ¦       ¦   ¦   ¦   ¦   Kyiv

¦   ¦       ¦   ¦   ¦   ¦   Lisbon

¦   ¦       ¦   ¦   ¦   ¦   Ljubljana

¦   ¦       ¦   ¦   ¦   ¦   London

¦   ¦       ¦   ¦   ¦   ¦   Luxembourg

¦   ¦       ¦   ¦   ¦   ¦   Madrid

¦   ¦       ¦   ¦   ¦   ¦   Malta

¦   ¦       ¦   ¦   ¦   ¦   Mariehamn

¦   ¦       ¦   ¦   ¦   ¦   Minsk

¦   ¦       ¦   ¦   ¦   ¦   Monaco

¦   ¦       ¦   ¦   ¦   ¦   Moscow

¦   ¦       ¦   ¦   ¦   ¦   Nicosia

¦   ¦       ¦   ¦   ¦   ¦   Oslo

¦   ¦       ¦   ¦   ¦   ¦   Paris

¦   ¦       ¦   ¦   ¦   ¦   Podgorica

¦   ¦       ¦   ¦   ¦   ¦   Prague

¦   ¦       ¦   ¦   ¦   ¦   Riga

¦   ¦       ¦   ¦   ¦   ¦   Rome

¦   ¦       ¦   ¦   ¦   ¦   Samara

¦   ¦       ¦   ¦   ¦   ¦   San\_Marino

¦   ¦       ¦   ¦   ¦   ¦   Sarajevo

¦   ¦       ¦   ¦   ¦   ¦   Saratov

¦   ¦       ¦   ¦   ¦   ¦   Simferopol

¦   ¦       ¦   ¦   ¦   ¦   Skopje

¦   ¦       ¦   ¦   ¦   ¦   Sofia

¦   ¦       ¦   ¦   ¦   ¦   Stockholm

¦   ¦       ¦   ¦   ¦   ¦   Tallinn

¦   ¦       ¦   ¦   ¦   ¦   Tirane

¦   ¦       ¦   ¦   ¦   ¦   Tiraspol

¦   ¦       ¦   ¦   ¦   ¦   Ulyanovsk

¦   ¦       ¦   ¦   ¦   ¦   Uzhgorod

¦   ¦       ¦   ¦   ¦   ¦   Vaduz

¦   ¦       ¦   ¦   ¦   ¦   Vatican

¦   ¦       ¦   ¦   ¦   ¦   Vienna

¦   ¦       ¦   ¦   ¦   ¦   Vilnius

¦   ¦       ¦   ¦   ¦   ¦   Volgograd

¦   ¦       ¦   ¦   ¦   ¦   Warsaw

¦   ¦       ¦   ¦   ¦   ¦   Zagreb

¦   ¦       ¦   ¦   ¦   ¦   Zaporozhye

¦   ¦       ¦   ¦   ¦   ¦   Zurich

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Indian

¦   ¦       ¦   ¦   ¦   ¦   Antananarivo

¦   ¦       ¦   ¦   ¦   ¦   Chagos

¦   ¦       ¦   ¦   ¦   ¦   Christmas

¦   ¦       ¦   ¦   ¦   ¦   Cocos

¦   ¦       ¦   ¦   ¦   ¦   Comoro

¦   ¦       ¦   ¦   ¦   ¦   Kerguelen

¦   ¦       ¦   ¦   ¦   ¦   Mahe

¦   ¦       ¦   ¦   ¦   ¦   Maldives

¦   ¦       ¦   ¦   ¦   ¦   Mauritius

¦   ¦       ¦   ¦   ¦   ¦   Mayotte

¦   ¦       ¦   ¦   ¦   ¦   Reunion

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Mexico

¦   ¦       ¦   ¦   ¦   ¦   BajaNorte

¦   ¦       ¦   ¦   ¦   ¦   BajaSur

¦   ¦       ¦   ¦   ¦   ¦   General

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---Pacific

¦   ¦       ¦   ¦   ¦   ¦   Apia

¦   ¦       ¦   ¦   ¦   ¦   Auckland

¦   ¦       ¦   ¦   ¦   ¦   Bougainville

¦   ¦       ¦   ¦   ¦   ¦   Chatham

¦   ¦       ¦   ¦   ¦   ¦   Chuuk

¦   ¦       ¦   ¦   ¦   ¦   Easter

¦   ¦       ¦   ¦   ¦   ¦   Efate

¦   ¦       ¦   ¦   ¦   ¦   Enderbury

¦   ¦       ¦   ¦   ¦   ¦   Fakaofo

¦   ¦       ¦   ¦   ¦   ¦   Fiji

¦   ¦       ¦   ¦   ¦   ¦   Funafuti

¦   ¦       ¦   ¦   ¦   ¦   Galapagos

¦   ¦       ¦   ¦   ¦   ¦   Gambier

¦   ¦       ¦   ¦   ¦   ¦   Guadalcanal

¦   ¦       ¦   ¦   ¦   ¦   Guam

¦   ¦       ¦   ¦   ¦   ¦   Honolulu

¦   ¦       ¦   ¦   ¦   ¦   Johnston

¦   ¦       ¦   ¦   ¦   ¦   Kanton

¦   ¦       ¦   ¦   ¦   ¦   Kiritimati

¦   ¦       ¦   ¦   ¦   ¦   Kosrae

¦   ¦       ¦   ¦   ¦   ¦   Kwajalein

¦   ¦       ¦   ¦   ¦   ¦   Majuro

¦   ¦       ¦   ¦   ¦   ¦   Marquesas

¦   ¦       ¦   ¦   ¦   ¦   Midway

¦   ¦       ¦   ¦   ¦   ¦   Nauru

¦   ¦       ¦   ¦   ¦   ¦   Niue

¦   ¦       ¦   ¦   ¦   ¦   Norfolk

¦   ¦       ¦   ¦   ¦   ¦   Noumea

¦   ¦       ¦   ¦   ¦   ¦   Pago\_Pago

¦   ¦       ¦   ¦   ¦   ¦   Palau

¦   ¦       ¦   ¦   ¦   ¦   Pitcairn

¦   ¦       ¦   ¦   ¦   ¦   Pohnpei

¦   ¦       ¦   ¦   ¦   ¦   Ponape

¦   ¦       ¦   ¦   ¦   ¦   Port\_Moresby

¦   ¦       ¦   ¦   ¦   ¦   Rarotonga

¦   ¦       ¦   ¦   ¦   ¦   Saipan

¦   ¦       ¦   ¦   ¦   ¦   Samoa

¦   ¦       ¦   ¦   ¦   ¦   Tahiti

¦   ¦       ¦   ¦   ¦   ¦   Tarawa

¦   ¦       ¦   ¦   ¦   ¦   Tongatapu

¦   ¦       ¦   ¦   ¦   ¦   Truk

¦   ¦       ¦   ¦   ¦   ¦   Wake

¦   ¦       ¦   ¦   ¦   ¦   Wallis

¦   ¦       ¦   ¦   ¦   ¦   Yap

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---US

¦   ¦       ¦   ¦   ¦   ¦   Alaska

¦   ¦       ¦   ¦   ¦   ¦   Aleutian

¦   ¦       ¦   ¦   ¦   ¦   Arizona

¦   ¦       ¦   ¦   ¦   ¦   Central

¦   ¦       ¦   ¦   ¦   ¦   East-Indiana

¦   ¦       ¦   ¦   ¦   ¦   Eastern

¦   ¦       ¦   ¦   ¦   ¦   Hawaii

¦   ¦       ¦   ¦   ¦   ¦   Indiana-Starke

¦   ¦       ¦   ¦   ¦   ¦   Michigan

¦   ¦       ¦   ¦   ¦   ¦   Mountain

¦   ¦       ¦   ¦   ¦   ¦   Pacific

¦   ¦       ¦   ¦   ¦   ¦   Samoa

¦   ¦       ¦   ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   ¦   

¦   ¦       ¦   ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦   ¦           

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---tzdata-2026.4.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦       ¦   LICENSE

¦   ¦       ¦       ¦   

¦   ¦       ¦       +---licenses

¦   ¦       ¦               LICENSE\_APACHE

¦   ¦       ¦               

¦   ¦       +---websockets

¦   ¦       ¦   ¦   auth.py

¦   ¦       ¦   ¦   cli.py

¦   ¦       ¦   ¦   client.py

¦   ¦       ¦   ¦   connection.py

¦   ¦       ¦   ¦   datastructures.py

¦   ¦       ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   frames.py

¦   ¦       ¦   ¦   headers.py

¦   ¦       ¦   ¦   http11.py

¦   ¦       ¦   ¦   imports.py

¦   ¦       ¦   ¦   protocol.py

¦   ¦       ¦   ¦   proxy.py

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   server.py

¦   ¦       ¦   ¦   speedups.c

¦   ¦       ¦   ¦   speedups.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   speedups.pyi

¦   ¦       ¦   ¦   streams.py

¦   ¦       ¦   ¦   typing.py

¦   ¦       ¦   ¦   uri.py

¦   ¦       ¦   ¦   utils.py

¦   ¦       ¦   ¦   version.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   \_\_main\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---asyncio

¦   ¦       ¦   ¦   ¦   client.py

¦   ¦       ¦   ¦   ¦   connection.py

¦   ¦       ¦   ¦   ¦   messages.py

¦   ¦       ¦   ¦   ¦   router.py

¦   ¦       ¦   ¦   ¦   server.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           client.cpython-314.pyc

¦   ¦       ¦   ¦           connection.cpython-314.pyc

¦   ¦       ¦   ¦           messages.cpython-314.pyc

¦   ¦       ¦   ¦           router.cpython-314.pyc

¦   ¦       ¦   ¦           server.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---extensions

¦   ¦       ¦   ¦   ¦   base.py

¦   ¦       ¦   ¦   ¦   permessage\_deflate.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           base.cpython-314.pyc

¦   ¦       ¦   ¦           permessage\_deflate.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---legacy

¦   ¦       ¦   ¦   ¦   auth.py

¦   ¦       ¦   ¦   ¦   client.py

¦   ¦       ¦   ¦   ¦   exceptions.py

¦   ¦       ¦   ¦   ¦   framing.py

¦   ¦       ¦   ¦   ¦   handshake.py

¦   ¦       ¦   ¦   ¦   http.py

¦   ¦       ¦   ¦   ¦   protocol.py

¦   ¦       ¦   ¦   ¦   server.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           auth.cpython-314.pyc

¦   ¦       ¦   ¦           client.cpython-314.pyc

¦   ¦       ¦   ¦           exceptions.cpython-314.pyc

¦   ¦       ¦   ¦           framing.cpython-314.pyc

¦   ¦       ¦   ¦           handshake.cpython-314.pyc

¦   ¦       ¦   ¦           http.cpython-314.pyc

¦   ¦       ¦   ¦           protocol.cpython-314.pyc

¦   ¦       ¦   ¦           server.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---sync

¦   ¦       ¦   ¦   ¦   client.py

¦   ¦       ¦   ¦   ¦   connection.py

¦   ¦       ¦   ¦   ¦   messages.py

¦   ¦       ¦   ¦   ¦   router.py

¦   ¦       ¦   ¦   ¦   server.py

¦   ¦       ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           client.cpython-314.pyc

¦   ¦       ¦   ¦           connection.cpython-314.pyc

¦   ¦       ¦   ¦           messages.cpython-314.pyc

¦   ¦       ¦   ¦           router.cpython-314.pyc

¦   ¦       ¦   ¦           server.cpython-314.pyc

¦   ¦       ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---trio

¦   ¦       ¦   ¦   ¦   client.py

¦   ¦       ¦   ¦   ¦   connection.py

¦   ¦       ¦   ¦   ¦   messages.py

¦   ¦       ¦   ¦   ¦   router.py

¦   ¦       ¦   ¦   ¦   server.py

¦   ¦       ¦   ¦   ¦   utils.py

¦   ¦       ¦   ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   ¦   

¦   ¦       ¦   ¦   +---\_\_pycache\_\_

¦   ¦       ¦   ¦           client.cpython-314.pyc

¦   ¦       ¦   ¦           connection.cpython-314.pyc

¦   ¦       ¦   ¦           messages.cpython-314.pyc

¦   ¦       ¦   ¦           router.cpython-314.pyc

¦   ¦       ¦   ¦           server.cpython-314.pyc

¦   ¦       ¦   ¦           utils.cpython-314.pyc

¦   ¦       ¦   ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦   ¦           

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           auth.cpython-314.pyc

¦   ¦       ¦           cli.cpython-314.pyc

¦   ¦       ¦           client.cpython-314.pyc

¦   ¦       ¦           connection.cpython-314.pyc

¦   ¦       ¦           datastructures.cpython-314.pyc

¦   ¦       ¦           exceptions.cpython-314.pyc

¦   ¦       ¦           frames.cpython-314.pyc

¦   ¦       ¦           headers.cpython-314.pyc

¦   ¦       ¦           http11.cpython-314.pyc

¦   ¦       ¦           imports.cpython-314.pyc

¦   ¦       ¦           protocol.cpython-314.pyc

¦   ¦       ¦           proxy.cpython-314.pyc

¦   ¦       ¦           server.cpython-314.pyc

¦   ¦       ¦           streams.cpython-314.pyc

¦   ¦       ¦           typing.cpython-314.pyc

¦   ¦       ¦           uri.cpython-314.pyc

¦   ¦       ¦           utils.cpython-314.pyc

¦   ¦       ¦           version.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           \_\_main\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---websockets-17.1.dist-info

¦   ¦       ¦   ¦   entry\_points.txt

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   REQUESTED

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           

¦   ¦       +---yarl

¦   ¦       ¦   ¦   py.typed

¦   ¦       ¦   ¦   \_parse.py

¦   ¦       ¦   ¦   \_path.py

¦   ¦       ¦   ¦   \_query.py

¦   ¦       ¦   ¦   \_quoters.py

¦   ¦       ¦   ¦   \_quoting.py

¦   ¦       ¦   ¦   \_quoting\_c.cp314-win\_amd64.pyd

¦   ¦       ¦   ¦   \_quoting\_c.pyx

¦   ¦       ¦   ¦   \_quoting\_py.py

¦   ¦       ¦   ¦   \_url.py

¦   ¦       ¦   ¦   \_\_init\_\_.py

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---\_\_pycache\_\_

¦   ¦       ¦           \_parse.cpython-314.pyc

¦   ¦       ¦           \_path.cpython-314.pyc

¦   ¦       ¦           \_query.cpython-314.pyc

¦   ¦       ¦           \_quoters.cpython-314.pyc

¦   ¦       ¦           \_quoting.cpython-314.pyc

¦   ¦       ¦           \_quoting\_py.cpython-314.pyc

¦   ¦       ¦           \_url.cpython-314.pyc

¦   ¦       ¦           \_\_init\_\_.cpython-314.pyc

¦   ¦       ¦           

¦   ¦       +---yarl-1.25.1.dist-info

¦   ¦       ¦   ¦   INSTALLER

¦   ¦       ¦   ¦   METADATA

¦   ¦       ¦   ¦   RECORD

¦   ¦       ¦   ¦   top\_level.txt

¦   ¦       ¦   ¦   WHEEL

¦   ¦       ¦   ¦   

¦   ¦       ¦   +---licenses

¦   ¦       ¦           LICENSE

¦   ¦       ¦           NOTICE

¦   ¦       ¦           

¦   ¦       +---\_\_pycache\_\_

¦   ¦               six.cpython-314.pyc

¦   ¦               

¦   +---Scripts

¦           activate

¦           activate.bat

¦           activate.fish

¦           Activate.ps1

¦           deactivate.bat

¦           dotenv.exe

¦           f2py.exe

¦           idna.exe

¦           numpy-config.exe

¦           pip.exe

¦           pip3.14.exe

¦           pip3.exe

¦           python.exe

¦           pythonw.exe

¦           websockets.exe

¦           

+---\_\_pycache\_\_

&#x20;       main.cpython-314.pyc

&#x20;       




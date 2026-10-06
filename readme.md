# Quote app

Questa applicazione è un mix di front e back end compilati in un singolo eseguibile.

L'applicazione flask si occupa di recuperare citazioni casuali da https://zenquotes.io utilizzando l'api gratuita.

PyWebView renderizza le pagine flask in una finestra

Pyinstaller è stato usato per creare il file eseguibile

## Compilazione
`pyinstaller --onefile --windowed --add-data "templates;templates" --add-data "static;static" --icon=icon.ico main.py`

## Esecuzione
eseguire il file "dist/main.exe" 

## Debug
lanciare l'applicazione flask da linea di comando
`flask run `
oppure
`python app.py`

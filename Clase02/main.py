#  _______   _______
# |  _____| |  ___  |
# | |       | |   | |    @rolodoom
# | |       | |___| |    https://github.com/rolodoom
# |_|       |_______|
#  _         _______
# | |       |  ___  |
# | |       | |   | |
# | |_____  | |___| |    Automatización de trabajo en python
# |_______| |_______|    Código probado en Windows 11
#
#
#
# --------------------------
# Librerías
# --------------------------
import yfinance
import pyautogui
import pyperclip
import webbrowser
import time


# --------------------------
# Constantes
# --------------------------
proveedor_mail = "https://mail.google.com/mail/u/0/#inbox"
destinatario = "micorreo@gmail.com"
asunto = "Prueba Clase 2 de Python: Análisis de acciones"
cuerpo = """Buenas noches,

Acá te envío el análisis de las acciones de los últimos 6 meses de Apple

Cotización máxima: USD {}
Cotización mínima: USD {}
Valor medio: USD {}

Estoy pendiente a cualquier observación

Saludos,

"""


# --------------------------
# Funciones
# --------------------------
def leer_datos_bolsa(idx="AAPL", periodo="6mo"):
    """
    Función para leer los datos de la bolsa de valores

    Args:
        idx (str, optional): Indice de la bolsa de valores. Defaults to "AAPL".
        periodo (str, optional): Período de tiempo. Defaults to "6mo".

    Returns:
        pandas.DataFrame: Datos de la bolsa de valores
    """
    data = yfinance.Ticker(idx).history(periodo)
    return data.Close


def automatizar_email(proveedor_mail, destinatario, asunto, cuerpo):
    """
    Función para automatizar el envío de correo

    Args:
        proveedor_mail (str): Proveedor de correo
        destinatario (str): Destinatario del correo
        asunto (str): Asunto del correo
        cuerpo (str): Cuerpo del correo

    Returns:
        None
    """
    # Abrir el proveedor de correo
    webbrowser.open(proveedor_mail)

    # Esperar 5 segundos y dar clic en Redactar
    time.sleep(5)
    pyautogui.PAUSE = 3
    pyautogui.click(135, 190)

    # Copiar y pegar el destinatario
    pyperclip.copy(destinatario)
    pyautogui.hotkey("ctrl", "v")

    # Tabulador y copiar y pegar el asunto
    pyautogui.hotkey("tab")
    pyperclip.copy(asunto)
    pyautogui.hotkey("ctrl", "v")

    # Tabulador y copiar y pegar el cuerpo
    pyautogui.hotkey("tab")
    pyperclip.copy(cuerpo)
    pyautogui.hotkey("ctrl", "v")

    # Dar clic en Enviar
    pyautogui.click(507, 860)

    # Dar clic en Cerrar
    pyautogui.hotkey("ctrl", "w")


# --------------------------
# Programa principal
# --------------------------
def main():
    # Leer los datos de la bolsa
    cierre = leer_datos_bolsa("AAPL", "6mo")

    maxima = round(cierre.max(), 2)
    minima = round(cierre.min(), 2)
    media = round(cierre.mean(), 2)

    automatizar_email(
        proveedor_mail, destinatario, asunto, cuerpo.format(maxima, minima, media)
    )

    print("Correo enviado!")


if __name__ == "__main__":
    main()

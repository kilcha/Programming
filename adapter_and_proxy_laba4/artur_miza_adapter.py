# Старый интерфейс
class OldPrinter:
    def print_text(self, text):
        print(f"OldPrinter: {text}")


# Новый интерфейс, который мы хотим использовать
class NewPrinterInterface:
    def print(self, text):
        raise NotImplementedError("This method should be overridden.")


# Адаптер, который позволяет использовать OldPrinter как NewPrinterInterface
class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        self.old_printer.print_text(text)


# Клиентский код
def client_code(printer: NewPrinterInterface):
    printer.print("Hello, Adapter Pattern!")


# Использование
if __name__ == "__main__":
    old_printer = OldPrinter()
    adapter = PrinterAdapter(old_printer)

    client_code(adapter)

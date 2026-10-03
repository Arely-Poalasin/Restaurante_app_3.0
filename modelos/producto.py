class Producto:
    def __init__(self, codigo, nombre, precio, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    @staticmethod
    def validar_texto(valor, campo):
        # Reutiliza una validación básica para datos obligatorios.
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacío.")

        return valor.strip()

    @staticmethod
    def validar_precio(valor):
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número válido.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        return precio

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(valor, "código")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = self.validar_precio(valor)

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = self.validar_texto(valor, "categoría")
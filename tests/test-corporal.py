
import unittest
import os

from src.crear_fichero import cargar_desde_txt, guardar_en_txt, nombre_archivo


class TestCrearFichero(unittest.TestCase):

    def setUp(self):
        """Asegura que el archivo de datos no existe antes de cada prueba."""
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)
    
    def tearDown(self):
        """Limpia el archivo de datos después de cada prueba."""
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)
            
    def test_guardar_en_txt_caso_normal(self):
        """Prueba que los datos se guarden correctamente en el archivo."""
        datos = [
            {"nombre": "Ana", "peso": 65.5},
            {"nombre": "Luis", "peso": 78.0}
        ]
        
        resultado = guardar_en_txt(datos)
        
        self.assertTrue(resultado)
        
        with open(nombre_archivo, 'r') as f:
            contenido = f.readlines()
            
        lineas_esperadas = [
            "---- REGISTRO PESO ----\n",
            "Ana, 65.5 Kg\n",
            "Luis, 78.0 Kg\n"
        ]
        self.assertEqual(contenido, lineas_esperadas)
        
    def test_guardar_en_txt_lista_vacia(self):
        """Prueba a guardar una lista vacía (caso límite)."""
        datos = []
        
        self.assertTrue(guardar_en_txt(datos)) 
        
        self.assertTrue(os.path.exists(nombre_archivo))
        with open(nombre_archivo, 'r') as f:
            contenido = f.read()
            
        self.assertEqual(contenido, "---- REGISTRO PESO ----\n")
        
   
    def test_cargar_desde_txt_archivo_inexistente(self):
        """Prueba que, si el archivo no existe, retorne una lista vacía."""
        datos_cargados = cargar_desde_txt()
        
        self.assertEqual(datos_cargados, [])
        
    def test_cargar_desde_txt_datos_correctos(self):
        """Prueba a cargar datos con el formato esperado."""
        contenido_archivo = (
            "---- REGISTRO PESO ----\n"
            "Carlos, 72.8 Kg\n"
            "Elena, 59.0 Kg\n"
        )
        with open(nombre_archivo, 'w') as f:
            f.write(contenido_archivo)
            
        datos_cargados = cargar_desde_txt()
        
        datos_esperados = [
            {"nombre": "Carlos", "peso": 72.8},
            {"nombre": "Elena", "peso": 59.0}
        ]
        self.assertEqual(datos_cargados, datos_esperados)

    def test_cargar_desde_txt_datos_corruptos(self):
        """Prueba que las líneas mal formadas sean ignoradas."""
        contenido_archivo = (
            "---- REGISTRO PESO ----\n"
            "Correcto1, 80.0 Kg\n"
            "SinComa NiPeso\n"
            "Correcto2, 70.0 Kg\n"
            "MalPeso, abc Kg\n"
        )
        with open(nombre_archivo, 'w') as f:
            f.write(contenido_archivo)
            
        datos_cargados = cargar_desde_txt()
        
        datos_esperados = [
            {"nombre": "Correcto1", "peso": 80.0},
            {"nombre": "Correcto2", "peso": 70.0}
        ]
        self.assertEqual(datos_cargados, datos_esperados)

if __name__ == '__main__':
    unittest.main()
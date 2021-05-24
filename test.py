import unittest
from unittest import mock
from unittest.mock import patch, MagicMock, mock_open
from DB import *
from API import *

class Tests(unittest.TestCase):
    
    # @mock.patch('pyodbc.connect')  
    # def test_read_sql_called(self, mock_access_database):
    #     bd = ConexionBD().__init__()
    #     self.assertTrue(mock_access_database.called)
    
    
    @patch('DB.ConexionBD.eliminar_equipo', return_value = True)
    def test_eliminar_equipo(self, mock):
        bd = ConexionBD()
        expected = True
        actual = bd.eliminar_equipo(1)
        assert expected == actual
    
    
    @patch('DB.ConexionBD.eliminar_equipo', return_value = False)
    def test_eliminar_equipo_dos(self,mock):
        bd = ConexionBD()
        resultado_esperado = False
        resultado_actual = bd.eliminar_equipo(2)
        assert resultado_esperado == resultado_actual 
    
    
    @patch('DB.ConexionBD.eliminar_pokemon', return_value = True)
    def test_eliminar_pokemon(self,mock):
        bd = ConexionBD()
        resultado_esperado = True
        resultado_actual = bd.eliminar_pokemon(5)
        assert resultado_esperado == resultado_actual
    
    
    @patch('DB.ConexionBD.eliminar_pokemon', return_value = False)
    def test_eliminar_pokemon_dos(self,mock):
        bd = ConexionBD()
        resultado_esperado = False
        resultado_actual = bd.eliminar_pokemon(5)
        assert resultado_esperado == resultado_actual
    
    
    @patch('DB.ConexionBD.guardar_equipo', return_value = True)
    def test_guardar_equipo(self,mock):
        bd = ConexionBD()
        expected = True
        actual = bd.guardar_equipo("mock")
        assert expected == actual
        
        
    @patch('DB.ConexionBD.guardar_equipo', return_value = False)
    def test_guardar_equipo_dos(self,mock):
        bd = ConexionBD()
        expected = False
        actual = bd.guardar_equipo("mock")
        assert expected == actual
    

    @patch('DB.ConexionBD.guardar_pokemon', return_value = True)
    def test_guardar_pokemon(self,mock):
        bd = ConexionBD()
        expected = True
        actual = bd.guardar_pokemon("mock",12)
        assert expected == actual
        
    @patch('DB.ConexionBD.guardar_pokemon', return_value = False)
    def test_guardar_pokemon_dos(self,mock):
        bd = ConexionBD()
        expected = False
        actual = bd.guardar_pokemon("mock",12)
        assert expected == actual
    
    
    def test_show_db_pokemons(self):
        ConexionBD.mostrar_pokemons = MagicMock()
        ConexionBD.mostrar_pokemons.return_value = 'Pokemon: algun pokemon xd, movimiento1, movimiento2, movimiento3, movimiento4'
        self.assertEqual(ConexionBD().mostrar_pokemons(), 'Pokemon: algun pokemon xd, movimiento1, movimiento2, movimiento3, movimiento4')
    
    
    @patch('API.PokeApi.buscar_pokemon', return_value = "1 bulbasaur grass ['razor-wind', 'swords-dance', 'cut', 'bind'] 64")
    def test_buscar_pokemon_con_name(self, mock):
        api = PokeApi()
        expected = "1 bulbasaur grass ['razor-wind', 'swords-dance', 'cut', 'bind'] 64"
        actual = api.buscar_pokemon('pikachu')
        assert expected == actual

    
    @patch('API.PokeApi.buscar_pokemon', return_value = "1 bulbasaur grass ['razor-wind', 'swords-dance', 'cut', 'bind'] 64")
    def test_buscar_pokemon_con_id(self, mock):
        api = PokeApi()
        expected = "1 bulbasaur grass ['razor-wind', 'swords-dance', 'cut', 'bind'] 64"
        actual = api.buscar_pokemon(50)
        assert expected == actual

    
    def test_search_team(self):
        ConexionBD.buscar_equipo = MagicMock()
        ConexionBD.buscar_equipo.return_value = "Equipo: Rocket\nEntrenador: Cesar\nPokemons: ['pikachu', 'bulbasaur', 'ekans', 'arbok', 'diglett', 'abra']"
        self.assertEqual(ConexionBD().buscar_equipo(1), "Equipo: Rocket\nEntrenador: Cesar\nPokemons: ['pikachu', 'bulbasaur', 'ekans', 'arbok', 'diglett', 'abra']")
    
    
    # @patch('DB.ConexionBD.buscar_equipo', return_value = "Equipo: Rocket\nEntrenador: Cesar\nPokemons: ['pikachu', 'bulbasaur', 'ekans', 'arbok', 'diglett', 'abra']")
    # def tets_buscar_equipo(self, mock):
    #     bd = ConexionBD()
    #     expected = "Equipo: Rocket\nEntrenador: Cesar\nPokemons: ['pikachu', 'bulbasaur', 'ekans', 'arbok', 'diglett', 'abra']"
    #     actual = bd.buscar_equipo(3)
    #     assert expected == actual
    
    
    def test_mostrar_teams(self):
        ConexionBD.mostrar_equipos = MagicMock()
        ConexionBD.mostrar_equipos.return_value = "['rojo', 'amarillo', 'azul']"
        self.assertEqual(ConexionBD().mostrar_equipos(), "['rojo', 'amarillo', 'azul']")
    
    
    # @patch('DB.ConexionBD.mostrar_equipos', return_value = "['rojo', 'amarillo', 'azul']")
    # def tets_mostrar_equipos(self, mock):
    #     bd = ConexionBD()
    #     expected = "['rojo', 'amarillo', 'azul']"
    #     actual = bd.mostrar_equipos()
    #     assert expected == actual


if __name__ == '__main__':
    unittest.main()
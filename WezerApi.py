from bs4 import BeautifulSoup
import requests

class WezerApi:
    def __get_current_players(self, ip: str, port: str):
        resp = requests.get(f"https://tsarvar.com/ru/servers/counter-strike-go/{ip}:{port}")
 
        soup = BeautifulSoup(resp.text, 'lxml')
        current_players = soup.find("span", class_="srvPage-countCur")
        return current_players.text
    
    def __get_max_players(self, ip: str, port: str):
        resp = requests.get(f"https://tsarvar.com/ru/servers/counter-strike-go/{ip}:{port}")
 
        soup = BeautifulSoup(resp.text, 'lxml')
        max_players = soup.find("span", class_="srvPage-countMax")
        return max_players.text

    def __get_normal_view(self, current_players: str, max_players: str) -> str:
        return f"{current_players}/{max_players}"

    def get_status(self, ip: str, port: str) -> str:
        current_players = self.__get_current_players(ip, port)
        max_players = self.__get_max_players(ip, port)
        status = self.__get_normal_view(current_players, max_players)

        return status

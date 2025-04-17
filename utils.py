from variables import SHAPE_LINK, PATH_DATA_JOBS
from selenium.webdriver.common.by import By

class SetLink():

    def __init__(self, chrome_browser, profission: str = "") -> None:
            self.profession = profission
            self._profession_format = ""
            self._shape_link = SHAPE_LINK    
            self.final_link = ""
            self.chrome_browser = chrome_browser

    def format_profission(self) -> str:
        if len(list(self.profession.split())) > 1:
            for d in self.profession.split():
                self._profession_format += "+" + d
        else:
            self._profession_format = "+" + self.profession

    def get_link(self):
        self.format_profission()
        self.final_link = self._shape_link.format(self._profession_format)
        return self.final_link
    
class DatasJobs():
    def __init__(self, chrome_browser, qtd_searchs: int = 0) -> None:
        self.quantity_searchs: int = qtd_searchs
        self.results: list = [[], [], []]
        self.chrome_browser = chrome_browser

    def get_datas_jobs(self):
        quantity_finds_results: int = 0
        i =1
        while(quantity_finds_results <= self.quantity_searchs): # get info of vagas 
            ii = 1
            while (ii <= 3):
                self.results[ii-1].append(self.chrome_browser.find_element(By.XPATH, PATH_DATA_JOBS.format(i, ii)).text)
                ii += 1
            quantity_finds_results += 1
            i += 1

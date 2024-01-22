from datetime import datetime


class work:
    def __init__(self):
        self.time = "21:05"

    def exec(self):
        """
        Função para executar a lógica do código relacionado ao sistema de work schedule.
        """

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Okey - Executado em {current_time}")

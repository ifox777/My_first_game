class Stats():
    """отслежтване статистики"""
    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())


    def reset_stats(self):
        """статистика изменяющаяся вов ремя игры"""
        self.guns_left = 2 #жизни
        self.score = 0  #счет
        

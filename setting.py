class Setting():
    # 储存该游戏中所有要用到的类
    def __init__(self):
        # 初始化游戏的设置,就不用后面再主模型中传入具体参数了
        #屏幕设置
        self.screen_width = 1400
        self.screen_height = 900
        self.bg_color = (230,230,230)

import sys
import pygame
from setting import Setting

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    '''
    创建一个宽1200像素，高800像素的游戏窗口，激活游戏的动画循环后，每经过一次循环都将重绘这个surface
    '''
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():  # 使用pygame.event.get()检测游戏中发生的事件
            if event.type == pygame.QUIT:
                sys.exit()  # 如果游戏退出了，那么系统退出
        # 每次循环结束时，都重绘屏幕
        screen.fill(ai_setting.bg_color)
        # 每一次循环的结束都让最新绘制的屏幕可见，更新屏幕，实现平滑移动的效果
        pygame.display.flip()
run_game() # 初始化游戏，进入主循环

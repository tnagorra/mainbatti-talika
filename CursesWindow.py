import curses

class CursesWindow:
    def __init__(self, strings, width, height, highlights, headrows):
        self.strings = strings
        self.width = width
        self.height = height
        self.posX = 0
        self.posY = 0
        self.hlts = highlights
        self.heads = headrows
        curses.wrapper(self.main)

    def main(self, screen):
        self.window = curses.newpad(self.height, self.width)
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        i = 0
        for row in self.strings:
            j = 0
            for string in row:
                if [i,j] in self.hlts:
                    self.window.addstr(string, curses.color_pair(1))
                else:
                    if i in self.heads:
                        self.window.addstr(string, curses.A_BOLD | curses.A_REVERSE)
                    else:
                        self.window.addstr(string)
                j += 1
            self.window.addstr('\n')
            i += 1

        self.window.keypad(True)
        self.screen = screen
    
        self.scroll()
        while (True):
            event = self.window.getch()
            if event == ord('q'):
                break
            elif event == ord('l') or event == curses.KEY_RIGHT:
                height, width = self.screen.getmaxyx()
                if self.posX+1+width < self.width:
                    self.posX += 1
            elif event == ord('h') or event == curses.KEY_LEFT:
                height, width = self.screen.getmaxyx()
                if self.posX-1 >= 0:
                    self.posX -= 1
            elif event == ord('k') or event == curses.KEY_UP:
                height, width = self.screen.getmaxyx()
                if self.posY-1 >= 0:
                    self.posY -= 1
            elif event == ord('j') or event == curses.KEY_DOWN:
                height, width = self.screen.getmaxyx()
                if self.posY+1+height < self.height:
                    self.posY += 1
    
            self.scroll()
    
    def scroll(self):
        height, width = self.screen.getmaxyx()
        self.window.refresh(self.posY, self.posX, 0, 0, height-1, width-1)
    


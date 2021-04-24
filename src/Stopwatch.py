from win32api import GetKeyState


class Stopwatch:
    pass


# Create main thread
class MainThread:
    # Runs main thread
    def run():
        timer_thread = TimerThread()
        timer_thread.run()
        while True:
            self.get_start_key(timer_thread)
            self.get_end_key(timer_thread)
            self.get_restart_key(timer_thread)
        
    def get_start_key(self, timer_thread):
        started = False
            if GetKeyState(0x11) < 0 and GetKeyState(0x53) < 0 and not started:
                started = True
                timer_thread.start()
                
            else:
                started = False
                
    def get_end_key(self, timer_thread):
        ended = False
            if GetKeyState(0x11) < 0 and GetKeyState(0x45) < 0 and not ended:
                ended = True
                timer_thread.stop()
                
            else:
                ended = False
                
    def get_restart_key(self, timer_thread):
        restarted = False
            if GetKeyState(0x11) < 0 and GetKeyState(0x52) < 0 and not restarted:
                restarted = True
                timer_thread.restart()
                
            else:
                restarted = False


# Create timer thread used for handling a timer
class TimerThread:
    def timer_thread():
        pass
    
    def update():
        pass
    
    @staticmethod
    def start_timer(timer):
        timer.start()
        
    @staticmethod
    def stop_timer(timer):
        timer.stop()
        
    @staticmethod
    def restart_timer(timer):
        timer.restart()
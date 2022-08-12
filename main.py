from messages import Say
from events import Action
from inputs import Menu

class Main:
    def begin(self):
        """
        Shows welcome message and initiates the menu loop.
        """
        Say.hello()
        self.menu()
        Say.goodbye()

    def menu(self):
        """
        Shows the menu and initiates the actions. Recieves
        input and passes selection to menu_select until
        user selects the exit option.
        """
        while True:
            Say.show_menu()
            response = Menu.get_selection()
            if response == '8':
                break
            self.menu_select(response)
            Say.proceed()
            input()


    def menu_select(self, selection):
            if selection == '1':
                Action.add_event()
            elif selection == '2':
                Action.see_all()
            elif selection == '3':
                Action.see_upcoming()
            elif selection == '4':
                Action.see_past()
            elif selection == '5':
                Action.search_events()
            elif selection == '6':
                Action.remove_event()
            elif selection == '7':
                Action.reset_planner()

if __name__ == '__main__':
    controller = Main()
    controller.begin()
class SwitchCase:
    @staticmethod
    def choose_action(choice, controller, view):
        actions = {
            '1': controller.add_animal,
            '2': controller.define_animal_class,
            '3': controller.show_animal_commands,
            '4': controller.train_animal,
            '5': controller.exit_program,
        }

        func = actions.get(choice, view.invalid_choice)
        func()

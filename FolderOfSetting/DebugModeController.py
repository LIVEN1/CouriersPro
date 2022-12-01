class DebugModeController:
    is_debug_mode_on = False

    def is_debug_mode(self):
        return self.is_debug_mode_on

    def set_debug_mode(self):
        self.is_debug_mode_on = not self.is_debug_mode_on
        print(self.is_debug_mode_on)


debug_mode_controller = DebugModeController()

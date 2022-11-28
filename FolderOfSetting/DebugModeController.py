class DebugModeControoler:
    is_debug_mode_on = False

    def is_debug_mode(self):
        return self.is_debug_mode_on

    def set_debug_mode(self, debug_mode_status):
        self.is_debug_mode_on = debug_mode_status
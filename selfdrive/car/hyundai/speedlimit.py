from selfdrive.controls.lib.drive_helpers import update_v_cruise


class VolkswagenSpeedlimits:

    # configurable toggles
    ignore_limit_when_difference_too_high = True
    ignore_limit_when_following_lead = True

    def __init__(self):
        self.initvar = 0

    @classmethod
    def update_speed_limit(cls, CS, v_cruise_kph, enabled):
        return v_cruise_kph

    @staticmethod
    def update_cruise_buttons(v_cruise_kph, buttonEvents, button_timers, enabled, metric, CS):

        v_cruise_kph = VolkswagenSpeedlimits.update_speed_limit(
            CS, v_cruise_kph, enabled)
        v_cruise_kph = update_v_cruise(
            v_cruise_kph, buttonEvents, button_timers, enabled, metric)

        return v_cruise_kph

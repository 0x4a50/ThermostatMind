#!/usr/bin/env python3

"""
The smallest unit of consciousness?
"""

from copy import copy
from random import random
import argparse

__author__ = "Jessica Radley"


class ThermostatMind:
    def __init__(self, ideal_temperature=20):
        """Some variables representing this agent's model of the universe"""
        self.ideal_temperature = ideal_temperature
        self.last_temperature = ideal_temperature
        self.temperature = ideal_temperature
        self.is_heating = False

    def predict_next_temperature(self):
        """
        Is it enough to predict, or to be intelligent do your predictions have to be right?
        Is learning new prediction functions really necessary?
        """
        return self.temperature + (self.temperature - self.last_temperature)

    def decide_to_act(self, temperature):
        self.temperature = temperature
        predicted_temperature = self.predict_next_temperature()
        if predicted_temperature >= self.ideal_temperature:
            self.is_heating = False
        else:
            self.is_heating = True

        self.last_temperature = temperature
        return self.is_heating


if __name__ == "__main__":
    # Set up the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--starting_temperature", type=int, default=15,
                        help="Initial temperature state")
    parser.add_argument("--ideal_temperature", type=int, default=20,
                        help="Temperature the ThermostatMind wants to achieve")
    parser.add_argument("--heat_multiplier", type=int, default=1,
                        help="Multiplies the amount of heating applied each timestep")
    parser.add_argument("--cooling_multiplier", type=int, default=1,
                        help="Multiplies the amount of cooling in the absence of heat")
    args = parser.parse_args()

    m = ThermostatMind(ideal_temperature=args.ideal_temperature)
    temp = args.starting_temperature
    heat_delta = 0  # Using this to make a world that continues to heat for a while after heating is turned off
    for _ in range(100):

        # Get the ThermostatMind's decision
        turn_on_heat = m.decide_to_act(copy(temp))

        # Print current state
        print('temp: {:.1f}, delta: {}, heat: {}'.format(
            temp, heat_delta, turn_on_heat))

        # Update the world
        if turn_on_heat:
            heat_delta = min(5, heat_delta + 1)
        else:
            heat_delta = max(0, heat_delta - 1)
        last_temp = temp
        if heat_delta > 0:
            temp += args.heat_multiplier * random()
        else:
            temp -= args.cooling_multiplier * random()

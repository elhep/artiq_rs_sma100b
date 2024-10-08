#!/usr/bin/env python3

import abc
import asyncio
import logging

from RsSmab import RsSmab


class ArtiqRsSma100bInterface(abc.ABC):
    @abc.abstractmethod
    async def set_frequency(self, frequency):
        pass

    @abc.abstractmethod
    async def set_rf_on(self, rf_on):
        pass

    @abc.abstractmethod
    async def set_power(self, power):
        pass

    @abc.abstractmethod
    async def get_frequency(self):
        pass

    @abc.abstractmethod
    async def get_rf_on(self):
        pass

    @abc.abstractmethod
    async def get_power(self):
        pass

    @abc.abstractmethod
    async def reset(self):
        pass

    async def ping(self):
        return True

    def close(self):
        pass


class ArtiqRsSma100b(ArtiqRsSma100bInterface):
    def __init__(self, device):
        self.smab = RsSmab(device)

    async def set_frequency(self, frequency):
        """
        Set level of the frequency. Unit: Hz.
        """
        self.smab.source.frequency.fixed.set_value(frequency)

    async def set_rf_on(self, rf_on):
        """
        Set boolean state of the RF output state.
        """
        self.smab.output.state.set_value(bool(rf_on))

    async def set_power(self, power):
        """
        Set float level at the RF output. Unit: dBm
        """
        self.smab.source.power.set_power(power)

    async def get_frequency(self):
        """
        Get level of the frequency. Unit: Hz.
        """
        return self.smab.source.frequency.fixed.get_value()

    async def get_rf_on(self):
        """
        Get boolean state of the RF output state.
        """
        return int(self.smab.output.state.get_value())

    async def get_power(self):
        """
        Get float level at the RF output. Unit: dBm
        """
        return self.smab.source.power.get_power()

    async def reset(self):
        """
        Reset state to deafults.
        """
        self.smab.utilities.reset()
        self.smab.utilities.clear_status()

    def close(self):
        self.smab.close()


class ArtiqRsSma100bSim(ArtiqRsSma100bInterface):
    def __init__(self):
        self.frequency = None
        self.power = None
        self.rf_on = None

    async def set_frequency(self, frequency):
        """
        Simulate setting frequency.
        """
        self.frequency = frequency
        logging.warning(f"Simulated: Setting frequency to {frequency}")

    async def set_rf_on(self, rf_on):
        """
        Simulate changing the state of RF.
        """
        self.rf_on = rf_on
        if rf_on:
            logging.warning("Simulated: Turning RF ON")
        else:
            logging.warning("Simulated: Turning RF OFF")

    async def set_power(self, power):
        """
        Simulate setting power.
        """
        self.power = power
        logging.warning(f"Simulated: Setting power to {power}")

    async def get_frequency(self):
        """
        Simulate getting frequency.
        """
        logging.warning(f"Simulated: Frequency redout: {self.frequency}")
        return self.frequency

    async def get_rf_on(self):
        """
        Simulate reading the state of RF.
        """
        logging.warning(f"Simulated: RF state redout: {self.rf_on}")
        return self.rf_on

    async def get_power(self):
        """
        Simulate getting power.
        """
        logging.warning(f"Simulated: Power redout: {self.power}")
        return self.power

    async def reset(self):
        """
        Simulate resetting device.
        """
        self.frequency = None
        self.power = None
        self.rf_on = None
        logging.warning("Simulated: Resetting settings")

import sys

from sipyco.test.generic_rpc import GenericRPCCase


class GenericRsSma100bTest:
    def test_set_frequency(self):
        frequency = 5e6
        self.artiq_rs_sma100b.set_frequency(frequency)
        self.assertEqual(frequency, self.artiq_rs_sma100b.get_frequency())

    def test_set_rf_on(self):
        rf_on = True
        self.artiq_rs_sma100b.set_rf_on(rf_on)
        self.assertEqual(rf_on, self.artiq_rs_sma100b.get_rf_on())

    def test_set_power(self):
        power = 15
        self.artiq_rs_sma100b.set_power(power)
        self.assertEqual(power, self.artiq_rs_sma100b.get_power())


class TestRsSma100bSim(GenericRPCCase, GenericRsSma100bTest):
    def setUp(self):
        GenericRPCCase.setUp(self)
        command = (
            sys.executable.replace("\\", "\\\\")
            + " -m artiq_rs_sma100b.aqctl_artiq_rs_sma100b"
            + " -p 3278 --simulation"
        )
        self.artiq_rs_sma100b = self.start_server("artiq_rs_sma100b", command, 3278)

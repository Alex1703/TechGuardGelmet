class MPU6050:
    def __init__(self, i2c):
        self.i2c = i2c
        self.address = 0x68  # Dirección I2C del sensor MPU6050
        self.accel_data = {'x': 0, 'y': 0, 'z': 0}
        self.gyro_data = {'x': 0, 'y': 0, 'z': 0}
        self.temp_data = 0

    def _read_word(self, register):
        high_byte = self.i2c.readfrom_mem(self.address, register, 1)[0]
        low_byte = self.i2c.readfrom_mem(self.address, register + 1, 1)[0]
        value = (high_byte << 8) | low_byte
        return value

    def _twos_complement(self, value, bits=16):
        if (value & (1 << (bits - 1))) != 0:
            value = value - (1 << bits)
        return value

    def read_accel_data(self):
        self.accel_data['x'] = self._twos_complement(self._read_word(0x3B))
        self.accel_data['y'] = self._twos_complement(self._read_word(0x3D))
        self.accel_data['z'] = self._twos_complement(self._read_word(0x3F))
        return self.accel_data

    def read_gyro_data(self):
        self.gyro_data['x'] = self._twos_complement(self._read_word(0x43))
        self.gyro_data['y'] = self._twos_complement(self._read_word(0x45))
        self.gyro_data['z'] = self._twos_complement(self._read_word(0x47))
        return self.gyro_data

    def read_temp_data(self):
        raw_temp = self._twos_complement(self._read_word(0x41))
        self.temp_data = (raw_temp / 340.0) + 36.53
        return self.temp_data
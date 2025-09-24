Creating a scalable platform for optimizing energy consumption in smart homes and buildings involves several components, including data collection, monitoring, scheduling, and optimization algorithms. Below is a simple example of a Python program to achieve this. This is a basic illustration and can be expanded further with more sophisticated algorithms and data sources.

```python
import random
import logging
from datetime import datetime, timedelta

# Initial setup for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class Device:
    """Class representing a device in a smart home or building"""

    def __init__(self, name, power_rating):
        self.name = name
        self.power_rating = power_rating  # in kilowatts
        self.status = False

    def turn_on(self):
        logging.info(f"Turning on {self.name}.")
        self.status = True

    def turn_off(self):
        logging.info(f"Turning off {self.name}.")
        self.status = False

    def __str__(self):
        return f"{self.name} - {'On' if self.status else 'Off'} - {self.power_rating} kW"


class SmartEnergyHub:
    """Smart Energy Hub for optimizing energy consumption"""

    def __init__(self):
        self.devices = []
        self.energy_tariff = self.get_energy_tariff()

    def add_device(self, device):
        self.devices.append(device)
        logging.info(f"Added device: {device}")

    def get_energy_tariff(self):
        # Mock function to simulate energy tariff variation
        # In a real-world scenario, this would fetch data from an API or database
        return {
            "peak": 0.20,  # price per kWh in dollars during peak hours
            "off_peak": 0.10  # price per kWh in dollars during off-peak hours
        }

    def optimize_energy_usage(self):
        # A simple optimization algorithm that turns off devices during peak hours
        current_hour = datetime.now().hour

        # Define peak hours (e.g., 6 PM to 10 PM)
        peak_hours = range(18, 22)

        if current_hour in peak_hours:
            logging.info("Peak hours detected. Optimizing energy usage.")
            for device in self.devices:
                if device.status:  # Turn off all devices during peak hours
                    device.turn_off()
        else:
            logging.info("Off-peak hours. Devices can be utilized.")
            for device in self.devices:
                if not device.status:  # Turn on devices if off and within off-peak hours
                    device.turn_on()

    def simulate_device_readings(self):
        # Simulate device power consumption readings
        for device in self.devices:
            if device.status:
                consumed_power = device.power_rating * random.uniform(0.8, 1.2)  # kW
                logging.info(f"{device.name} consumed {consumed_power:.2f} kW")

    def run(self):
        try:
            while True:
                logging.info("Running energy optimization...")
                self.optimize_energy_usage()
                self.simulate_device_readings()
                logging.info("Cycle complete. Waiting for next cycle...")
                # Wait for a certain period before re-running the optimization
                # In a real-world scenario, you can schedule this with a task scheduler
                timedelta(seconds=10)
        
        except KeyboardInterrupt:
            logging.info("Shutting down Smart Energy Hub...")

# Create a smart energy hub instance
hub = SmartEnergyHub()

# Add devices to the hub
hub.add_device(Device("Heater", 2.0))      # 2.0 kW
hub.add_device(Device("AC", 3.5))         # 3.5 kW
hub.add_device(Device("Refrigerator", 1.0)) # 1.0 kW

# Run the Smart Energy Hub system
hub.run()
```

### Explanation and Error Handling

1. **Logging**: A logging system is set up to track activities within the program for monitoring and debugging.

2. **Device Class**: Models a device that has a name, power rating, and status. It includes methods to turn the device on or off.

3. **SmartEnergyHub Class**: This class manages the devices and contains methods for optimizing energy use by leveraging different tariffs during peak and off-peak periods.

4. **Energy Tariff Mocking**: For simplicity, the program simulates energy tariffs. In a practical scenario, you would fetch this data from an external source.

5. **Optimization Logic**: A simple rule-based system that turns devices on/off based on time periods. More complex algorithms can be designed based on usage patterns, predictive analytics, etc.

6. **Simulation of Device Readings**: This simulates energy consumption data, which would otherwise be collected via sensors in a real application.

7. **Program Execution**: The hub runs an infinite loop to continually optimize and log energy usage. A `KeyboardInterrupt` exception handler allows for graceful shutdown.

### Future Enhancements

The provided example is a basic structure and can be expanded with more sophisticated and detailed implementations such as:

- Real-time data acquisition via IoT devices.
- Integration with smart grids and flexible pricing models.
- Predictive analytics for energy usage predictions.
- User interfaces for manual overrides or custom scheduling.
- Distributed architecture for scalability in larger buildings or networks.
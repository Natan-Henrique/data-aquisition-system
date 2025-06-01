import subprocess
import time
import random
import string
import argparse

def generate_random_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_random_frequency(min_freq=500, max_freq=2000):
    return random.randint(min_freq, max_freq)

def run_sensor_emulator(sensor_id, frequency):
    command = ["python3", "./emulators/sensor_emulator.py", "--sensor_id", sensor_id, "--frequency", str(frequency)]
    return subprocess.Popen(command)

def main():
    parser = argparse.ArgumentParser(description="Run multiple sensor emulators with random IDs and frequencies.")
    parser.add_argument("--num_sensors", type=int, default=5, help="Number of sensors to run")
    args = parser.parse_args()

    processes = []

    try:
        for _ in range(args.num_sensors):
            sensor_id = generate_random_id()
            frequency = generate_random_frequency()
            print(f"Starting sensor emulator for {sensor_id} with frequency {frequency} ms")
            process = run_sensor_emulator(sensor_id, frequency)
            processes.append(process)

        print("All sensors are running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping all sensors...")
        for process in processes:
            process.terminate()
        print("All sensors stopped.")

if __name__ == "__main__":
    main()
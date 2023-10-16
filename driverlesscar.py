class DriverlessCar:
    def __init__(self):
        self.speed = 0
        self.state = "stopped"
        self.brake_system = BrakeSystem()
        self.lidar_sensor = LightDetectionRanging()
        self.camera = Camera()

    def accelerate(self):
        self.speed += 1
        print("Accelerating. Speed:", self.speed)

    def decelerate(self):
        if self.speed > 0:
            self.speed -= 1
        print("Decelerating. Speed:", self.speed)

    def drive(self, target_speed: int):
        while self.speed!=target_speed:
            self.accelerate()
        #self.speed = 0
        self.state = "driving"
        print("Car driving.")

    def stop(self):
        while self.speed>0:
            self.brake_system.applyBrake()
            self.decelerate()
        self.state = "stopped"
        
        print("Car stopped.")

    def park(self):
        self.speed = 0
        self.state = "parked"
        self.brake_system.applyBrake()
        print("Car parked.")


class BrakeSystem:
    def __init__(self):
        self.brakeLights = BrakeLights()

    def applyBrake(self):
        self.brakeLights.turnOn()
        print("Brake applied.")

    def releaseBrake(self):
        self.brakeLights.turnOff()
        print("Brake released.")


class BrakeLights:
    def __init__(self):
        self.status = False

    def turnOn(self):
        self.status = True
        print("Brake lights turned on.")

    def turnOff(self):
        self.status = False
        print("Brake lights turned off.")


class LightDetectionRanging:
    def __init__(self):
        self.object_distance = 0

    def measureDistance(self):
        # Simulating distance measurement
        self.object_distance = 50 # meters

        # Simulating the distance rate of change from car to object
        self.distance_rate_change = 10 # meters per second
        print("Object Distance measured:", self.object_distance)


class Camera:
    def __init__(self):
        self.image = None

    def captureImage(self):
        # Simulating image capture
        self.image = "Captured image"
        print("Image captured.")


# Example usage
car = DriverlessCar()
car.drive(target_speed=100)

# Simulating the need to stop due to object detected by Lidar
car.lidar_sensor.measureDistance()
if car.lidar_sensor.object_distance < 10 or car.lidar_sensor.distance_rate_change>5:
    car.stop()

# Simulating the need to stop due to an obstacle detected by the camera
car.camera.captureImage()
if car.camera.image is not None:
    car.stop()

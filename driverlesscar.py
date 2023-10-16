class DriverlessCar:
    def __init__(self):
        self.speed = 0
        self.state = "stopped"
        self.brakeSystem = BrakeSystem()
        self.lightSensor = LightDetectionSensor()
        self.camera = Camera()

    def accelerate(self):
        self.speed += 10
        print("Accelerating. Speed:", self.speed)

    def decelerate(self):
        if self.speed > 0:
            self.speed -= 10
        print("Decelerating. Speed:", self.speed)

    def stop(self):
        self.speed = 0
        self.state = "stopped"
        self.brakeSystem.applyBrake()
        print("Car stopped.")

    def park(self):
        self.speed = 0
        self.state = "parked"
        self.brakeSystem.applyBrake()
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


class LightDetectionSensor:
    def __init__(self):
        self.intensity = 0

    def measureIntensity(self):
        # Simulating light intensity measurement
        self.intensity = 50
        print("Light intensity measured:", self.intensity)


class Camera:
    def __init__(self):
        self.image = None

    def captureImage(self):
        # Simulating image capture
        self.image = "Captured image"
        print("Image captured.")


# Example usage
car = DriverlessCar()
car.accelerate()
car.decelerate()

# Simulating the need to stop due to low light intensity
car.lightSensor.measureIntensity()
if car.lightSensor.intensity < 10:
    car.stop()

# Simulating the need to stop due to an obstacle detected by the camera
car.camera.captureImage()
if car.camera.image is not None:
    car.stop()
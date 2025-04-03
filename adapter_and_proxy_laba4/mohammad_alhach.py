from abc import ABC, abstractmethod


# Step 1: Define a common interface (Target) that the client expects.
class Target(ABC):
    @abstractmethod
    def request(self):
        """Abstract method that all concrete implementations must implement."""
        pass


# Step 2: Define the Adaptee (existing service with an incompatible interface).
class ThirdPartyService:
    """This is an existing class with a different method name and behavior."""

    def specific_request(self):
        return "Data from ThirdPartyService"


# Step 3: Create an Adapter to make ThirdPartyService compatible with Target.
class ServiceAdapter(Target):
    """Adapter that translates the Target interface into the Adaptee's interface."""

    def __init__(self, adaptee: ThirdPartyService):
        self._adaptee = adaptee  # Store the adaptee (existing service)

    def request(self):
        """Translate the 'request' method into 'specific_request'."""
        return self._adaptee.specific_request()


# Step 4: Create a Proxy that wraps the adapted service and adds logging.
class LoggingProxy(Target):
    """Proxy that adds logging functionality before and after calling the actual service."""

    def __init__(self, service: Target):
        self._service = service  # Store the real service (could be an adapter)

    def request(self):
        """Log the request before calling the real service."""
        print("[LOG]: Request is being made to the service.")

        # Call the actual service method
        result = self._service.request()

        print(f"[LOG]: Response received -> {result}")
        return result


# Step 5: Client Code (Demonstrating how the patterns work together)
if __name__ == "__main__":
    # Create an instance of the Third-Party Service (Adaptee)
    third_party_service = ThirdPartyService()

    # Wrap it with an Adapter to make it compatible with our system
    adapted_service = ServiceAdapter(third_party_service)

    # Wrap the adapted service with a Proxy to add logging
    proxy_service = LoggingProxy(adapted_service)

    # The client interacts only with the proxy, which internally uses the adapter
    response = proxy_service.request()

    print("Final Output:", response)  # This is what the client receives

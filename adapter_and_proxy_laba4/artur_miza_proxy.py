class RealSubject:
    def __init__(self):
        print("RealSubject created")
        self.data = "Data from RealSubject"

    def request(self):
        return self.data


class LocalProxy:
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        return self._real_subject.request()


class ReferenceCounterProxy:
    def __init__(self):
        self._real_subject = RealSubject()
        self._reference_count = 0

    def add_reference(self):
        self._reference_count += 1

    def remove_reference(self):
        self._reference_count -= 1
        if self._reference_count == 0:
            print("RealSubject is being deleted")

    def get_data(self):
        self.add_reference()
        return self._real_subject.data


class VirtualProxy:
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        return self._real_subject.request()


class SecurityProxy:
    def __init__(self, user_role):
        self._real_subject = RealSubject()
        self._user_role = user_role

    def request(self):
        if self._user_role == "admin":
            return self._real_subject.request()
        else:
            return "Access denied"


# Использование всех прокси

print("=== Local Proxy ===")
local_proxy = LocalProxy()
print(local_proxy.request())  # Вывод: Data from RealSubject

print("\n=== Reference Counter Proxy ===")
reference_counter_proxy = ReferenceCounterProxy()
print(reference_counter_proxy.get_data())  # Вывод: Data from RealSubject
reference_counter_proxy.remove_reference()  # Вывод: RealSubject is being deleted

print("\n=== Virtual Proxy ===")
virtual_proxy = VirtualProxy()
print(virtual_proxy.request())  # Вывод: RealSubject created
                                  #         Data from RealSubject

print("\n=== Security Proxy ===")
admin_proxy = SecurityProxy("admin")
print(admin_proxy.request())  # Вывод: Data from RealSubject

user_proxy = SecurityProxy("user")
print(user_proxy.request())  # Вывод: Access denied
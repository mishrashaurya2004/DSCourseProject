class Node:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number
        self.next = None

class ParkingLinkedList:
    def __init__(self, max_size=6):
        self.head = None
        self.size = 0
        self.max_size = max_size

    def display_available_slots(self):
        current = self.head
        occupied_slots = []
        while current:
            occupied_slots.append(current.vehicle_number)
            current = current.next

        vacant_slots = self.max_size - len(occupied_slots)
        print("Occupied slots:", end=" ")
        print(occupied_slots if occupied_slots else "None")
        print(f"Slots available: {vacant_slots} / {self.max_size}")
        print("Slot numbers:", end=" ")
        for i in range(1, self.max_size + 1):
            if str(i) not in occupied_slots:
                print(i, end=" ")
        print()

    def is_vehicle_present(self, vehicle_number):
        current = self.head
        while current:
            if current.vehicle_number == vehicle_number:
                return True
            current = current.next
        return False

    def find_vehicle_slot(self, vehicle_number):
        current = self.head
        slot = 1
        while current:
            if current.vehicle_number == vehicle_number:
                return slot
            current = current.next
            slot += 1
        return None

    def insert_vehicle(self, vehicle_number):
        if self.size < self.max_size and not self.is_vehicle_present(vehicle_number):
            new_node = Node(vehicle_number)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            print(f"Vehicle {vehicle_number} parked successfully.")
        elif self.is_vehicle_present(vehicle_number):
            print(f"Vehicle {vehicle_number} is already parked.")
        else:
            print("Parking is full. Cannot park more vehicles.")

    def delete_vehicle(self, vehicle_number):
        current = self.head
        prev = None

        while current and current.vehicle_number != vehicle_number:
            prev = current
            current = current.next

        if current:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            self.size -= 1
            print(f"Vehicle {vehicle_number} removed from the parking.")
        else:
            print(f"Vehicle {vehicle_number} not found in the parking.")

# Example usage
parking_lot = ParkingLinkedList()

while True:
    action = input("Enter 'park' to park a vehicle, 'leave' to remove a vehicle, 'search' to find a vehicle, 'display' to show available slots, or 'exit' to exit: ")

    if action == 'exit':
        break
    elif action == 'park':
        vehicle_number = input("Enter vehicle number: ")
        parking_lot.insert_vehicle(vehicle_number)
    elif action == 'leave':
        vehicle_number = input("Enter vehicle number to remove: ")
        parking_lot.delete_vehicle(vehicle_number)
    elif action == 'search':
        vehicle_number = input("Enter vehicle number to search: ")
        slot = parking_lot.find_vehicle_slot(vehicle_number)
        if slot is not None:
            print(f"Vehicle {vehicle_number} is parked in slot {slot}.")
        else:
            print(f"Vehicle {vehicle_number} not found in the parking.")
    elif action == 'display':
        parking_lot.display_available_slots()
    else:
        print("Invalid command. Please enter 'park', 'leave', 'search', 'display', or 'exit'.")

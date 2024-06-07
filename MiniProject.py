With file handling

class ViolationRecordManager:
    def __init__(self):
        self.violation_records = []
        self.next_id = 1
        self.fine_store = {
            "Speeding": 100,
            "Running Red Light": 200,
            "Illegal Parking": 150,
            "Triple Riding": 300
        }
        self.filename = "violation_records.txt"

        # Load existing violation records from file if available
        self.load_violation_records()

    def create_violation_record(self, vehicle_number, violation_type, date):
        if violation_type not in self.fine_store:
            print(f"Invalid violation type: {violation_type}. Cannot create violation record.")
            return None
        
        fine_amount = self.fine_store[violation_type]
        
        violation = {
            "violation_id": self.next_id,
            "vehicle_number": vehicle_number,
            "violation_type": violation_type,
            "date": date,
            "fine_amount": fine_amount  # Include fine amount in the violation record
        }
        
        self.violation_records.append(violation)
        self.next_id += 1
        self.save_violation_records()  # Save updated records to file
        return violation

    def load_violation_records(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    record = eval(line)  # Use eval to convert string back to dictionary
                    self.violation_records.append(record)
                    if record["violation_id"] >= self.next_id:
                        self.next_id = record["violation_id"] + 1
        except FileNotFoundError:
            # If file doesn't exist, start fresh with next_id as 1
            self.violation_records = []
            self.next_id = 1

    def save_violation_records(self):
        with open(self.filename, "w") as file:
            for record in self.violation_records:
                file.write(str(record) + "\n")  # Write dictionary as string to file

    def update_violation_record(self, violation_id, new_violation_type):
        updated = False
        for record in self.violation_records:
            if record["violation_id"] == violation_id:
                if new_violation_type in self.fine_store:
                    record["violation_type"] = new_violation_type
                    record["fine_amount"] = self.fine_store[new_violation_type]
                    updated = True
                else:
                    print(f"Invalid violation type: {new_violation_type}. Cannot update violation record.")
                break
        
        if updated:
            self.save_violation_records()
            print(f"Violation Record {violation_id} updated successfully.")
        else:
            print(f"Violation Record {violation_id} not found or update failed.")

    def print_all_violation_records(self):
        if not self.violation_records:
            print("No violation records found.")
        else:
            print("Violation Records:")
            for record in self.violation_records:
                print(f"Violation ID: {record['violation_id']}")
                print(f"Vehicle Number: {record['vehicle_number']}")
                print(f"Violation Type: {record['violation_type']}")
                print(f"Date: {record['date']}")
                print(f"Fine Amount: {record['fine_amount']}")
                print()

    def add_violation_record_manually(self):
        vehicle_number = input("Enter vehicle number: ").strip()
        violation_type = input("Enter violation type (Speeding/Running Red Light/Illegal Parking/Triple Riding): ").strip()
        if violation_type not in self.fine_store:
            print(f"Invalid violation type: {violation_type}. Cannot create violation record.")
            return
        
        date = input("Enter violation date (YYYY-MM-DD): ").strip()

        # Create the violation record using the entered details
        new_record = self.create_violation_record(vehicle_number, violation_type, date)
        if new_record:
            print("Violation record added successfully.")
        else:
            print("Failed to add violation record.")

    def delete_violation_record(self, violation_id):
        deleted = False
        for i, record in enumerate(self.violation_records):
            if record["violation_id"] == violation_id:
                del self.violation_records[i]
                deleted = True
                break
        if deleted:
            self.save_violation_records()
            print(f"Violation Record {violation_id} deleted successfully.")
        else:
            print(f"Violation Record {violation_id} not found or delete failed.")

    def log_traffic_violation(self, violation_id):
        logger = ViolationLogger()
        logger.log_traffic_violations(violation_id)
        for record in self.violation_records:
            if record["violation_id"] == violation_id:
                print(f"Logging traffic violation for Vehicle Number: {record['vehicle_number']}")
                print(f"Violation Type: {record['violation_type']}")
                print(f"Date: {record['date']}")
                print(f"Fine: {record['fine_amount']}")
                print("Traffic violation successfully logged.")
                return
        print(f"Violation ID {violation_id} not found.")

    def analyze_violation_data(self, vehicle_number):
        analyzer = ViolationAnalyzer()
        analyzer.analyze_violation_data(vehicle_number, self.violation_records)

class ViolationLogger:
    def log_traffic_violations(self, violation_id):
        print(f"Logged traffic violation with ID: {violation_id}")
            
class ViolationAnalyzer:
    def analyze_violation_data(self, vehicle_number, violation_records):
        count = 0
        for record in violation_records:
            if record["vehicle_number"] == vehicle_number:
                count += 1
        print(f"Vehicle {vehicle_number} has committed {count} violations.")
        
def print_menu():
    print("\n\n\n************************************************************************")
    print("\n--- Violation Record Management System Menu ---")
    print("1. Add Violation Record")
    print("2. Update Violation Record")
    print("3. Delete Violation Record")
    print("4. View All Violation Records")
    print("5. Log Traffic Violation")
    print("6. Analyze Violation Data")
    print("7. Exit")

# Example Usage:
manager = ViolationRecordManager()

while True:
    print_menu()
    choice = input("Enter your choice (1-7): ").strip()
    print("\n\n\n************************************************************************")

    if choice == '1':
        manager.add_violation_record_manually()
    elif choice == '2':
        violation_id = int(input("Enter Violation ID to update: ").strip())
        new_violation_type = input("Enter new violation type: ").strip()
        manager.update_violation_record(violation_id, new_violation_type)
    elif choice == '3':
        violation_id = int(input("Enter Violation ID to delete: ").strip())
        success = manager.delete_violation_record(violation_id)
        if success:
            print(f"Violation Record {violation_id} deleted successfully.")
        else:
            print(f"Violation Record {violation_id} not found.")
    elif choice == '4':
        manager.print_all_violation_records()
    elif choice == '5':
        violation_id = int(input("Enter Violation ID to log: ").strip())
        manager.log_traffic_violation(violation_id)
        # violation_id = int(input("Enter Violation ID to log: ").strip())
        # manager.log_traffic_violation(violation_id)
    elif choice == '6':
        vehicle_number = input("Enter vehicle number to analyze: ").strip()
        manager.analyze_violation_data(vehicle_number)
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")





#Without file handling

class ViolationRecordManager:
    def __init__(self):
        self.violation_records = []
        self.next_id = 1
        self.fine_store = {
            "Speeding": 100,
            "Running Red Light": 200,
            "Illegal Parking": 150,
            "Triple Riding": 300
        }

    def create_violation_record(self, vehicle_number, violation_type, date):
        if violation_type not in self.fine_store:
            print(f"Invalid violation type: {violation_type}. Cannot create violation record.")
            return None
        
        fine_amount = self.fine_store[violation_type]
        
        violation = {
            "violation_id": self.next_id,
            "vehicle_number": vehicle_number,
            "violation_type": violation_type,
            "date": date,
            "fine_amount": fine_amount  # Include fine amount in the violation record
        }
        
        self.violation_records.append(violation)
        self.next_id += 1
        return violation

    def read_violation_record(self, violation_id):
        for record in self.violation_records:
            if record["violation_id"] == violation_id:
                return record
        return None

    def update_violation_record(self, violation_id, new_details):
        for record in self.violation_records:
            if record["violation_id"] == violation_id:
                if "violation_type" in new_details:
                    new_violation_type = new_details["violation_type"]
                    if new_violation_type in self.fine_store:
                        record["violation_type"] = new_violation_type
                        record["fine_amount"] = self.fine_store[new_violation_type]
                    else:
                        print(f"Invalid violation type: {new_violation_type}. Cannot update violation record.")
                        return False
                record.update(new_details)
                return True
        return False

    def delete_violation_record(self, violation_id):
        for i, record in enumerate(self.violation_records):
            if record["violation_id"] == violation_id:
                del self.violation_records[i]
                return True
        return False

    def print_all_violation_records(self):
        if not self.violation_records:
            print("No violation records found.")
        else:
            print("Violation Records:")
            for record in self.violation_records:
                print(f"Violation ID: {record['violation_id']}")
                print(f"Vehicle Number: {record['vehicle_number']}")
                print(f"Violation Type: {record['violation_type']}")
                print(f"Date: {record['date']}")
                print(f"Fine Amount: {record['fine_amount']}")
                print()

    def add_violation_record_manually(self):
        vehicle_number = input("Enter vehicle number: ").strip()
        violation_type = input("Enter violation type (Speeding/Running Red Light/Illegal Parking/Triple Riding): ").strip()
        if violation_type not in self.fine_store:
            print(f"Invalid violation type: {violation_type}. Cannot create violation record.")
            return
        
        date = input("Enter violation date (YYYY-MM-DD): ").strip()

        # Create the violation record using the entered details
        new_record = self.create_violation_record(vehicle_number, violation_type, date)
        if new_record:
            print("Violation record added successfully.")
        else:
            print("Failed to add violation record.")

    def log_traffic_violation(self, violation_id):
        logger = ViolationLogger()
        logger.log_traffic_violations(violation_id)
        for record in self.violation_records:
            if record["violation_id"] == violation_id:
                print(f"Logging traffic violation for Vehicle Number: {record['vehicle_number']}")
                print(f"Violation Type: {record['violation_type']}")
                print(f"Date: {record['date']}")
                print(f"Fine: {record['fine_amount']}")
                print("Traffic violation successfully logged.")
                return
        print(f"Violation ID {violation_id} not found.")

    def analyze_violation_data(self, vehicle_number):
        analyzer = ViolationAnalyzer()
        analyzer.analyze_violation_data(vehicle_number, self.violation_records)


class ViolationLogger:
    def log_traffic_violations(self, violation_id):
        print(f"Logged traffic violation with ID: {violation_id}")
            
class ViolationAnalyzer:
    def analyze_violation_data(self, vehicle_number, violation_records):
        count = 0
        for record in violation_records:
            if record["vehicle_number"] == vehicle_number:
                count += 1
        print(f"Vehicle {vehicle_number} has committed {count} violations.")
        
def print_menu():
    print("\n\n\n************************************************************************")
    print("\n--- Violation Record Management System Menu ---")
    print("1. Add Violation Record")
    print("2. Update Violation Record")
    print("3. Delete Violation Record")
    print("4. View All Violation Records")
    print("5. Log Traffic Violation")
    print("6. Analyze Violation Data")
    print("7. Exit")

# Example Usage:
manager = ViolationRecordManager()

while True:
    print_menu()
    choice = input("Enter your choice (1-7): ").strip()
    print("\n\n\n************************************************************************")

    if choice == '1':
        manager.add_violation_record_manually()
    elif choice == '2':
        violation_id = int(input("Enter Violation ID to update: ").strip())
        new_violation_type = input("Enter new violation type: ").strip()
        success = manager.update_violation_record(violation_id, {"violation_type": new_violation_type})
        if success:
            print(f"Violation Record {violation_id} updated successfully.")
        else:
            print(f"Violation Record {violation_id} not found.")
    elif choice == '3':
        violation_id = int(input("Enter Violation ID to delete: ").strip())
        success = manager.delete_violation_record(violation_id)
        if success:
            print(f"Violation Record {violation_id} deleted successfully.")
        else:
            print(f"Violation Record {violation_id} not found.")
    elif choice == '4':
        manager.print_all_violation_records()
    elif choice == '5':
        violation_id = int(input("Enter Violation ID to log: ").strip())
        manager.log_traffic_violation(violation_id)
    elif choice == '6':
        vehicle_number = input("Enter vehicle number to analyze: ").strip()
        manager.analyze_violation_data(vehicle_number)
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

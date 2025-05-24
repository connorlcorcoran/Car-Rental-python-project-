from datetime import datetime

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, date_of_birth):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year - \
              ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    def is_eligible(self):
        return self.get_age() >= 25
    
    def __str__(self):
        return f"Customer [ID: {self.customer_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Phone: {self.phone}, Age: {self.get_age()}]"

class CarRental:
    def __init__(self, rental_id, agent_name, rental_price, daily_rate, car_model):
        self.rental_id = rental_id
        self.agent_name = agent_name
        self.rental_price = rental_price
        self.daily_rate = daily_rate
        self.car_model = car_model
        self.customer = None
        self.rental_duration = 0  # in days
    
    def assign_customer(self, customer):
        if customer.is_eligible():
            self.customer = customer
            return True
        else:
            return False
    
    def calculate_total_cost(self):
        return self.daily_rate * self.rental_duration
    
    def __str__(self):
        rental_details = f"Car Rental [ID: {self.rental_id}, Agent: {self.agent_name}, Car: {self.car_model}, Daily Rate: ${self.daily_rate:.2f}]"
        if self.customer:
            return f"{rental_details}, Assigned to: {self.customer.first_name} {self.customer.last_name}, Rental Duration: {self.rental_duration} days"
        return f"{rental_details}, Not assigned to any customer"

# Function to display available cars
def display_available_cars():
    available_cars = [
        ("Toyota Camry", 50.0),
        ("Honda Civic", 45.0),
        ("Ford Mustang", 75.0),
        ("Chevrolet Malibu", 60.0)
    ]
    print("\nAvailable Cars for Rent:")
    for index, (car_model, daily_rate) in enumerate(available_cars, start=1):
        print(f"{index}. {car_model} - ${daily_rate}/day")
    return available_cars

# Main application
def main():
    print("Welcome to the Car Rental System")
    
    # Gather Customer information
    customer_id = input("Enter Customer ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    
    customer = Customer(customer_id, first_name, last_name, email, phone, dob)
    
    # Display Customer info and eligibility
    print("\nCustomer Information:")
    print(customer)
    if customer.is_eligible():
        print("Customer is eligible for a car rental.")
    else:
        print("Customer is NOT eligible for a car rental.")
        return  # Exit if not eligible
    
    # Display available cars and allow the user to choose a car
    available_cars = display_available_cars()
    car_choice = int(input("\nChoose a car by entering the number (1-4): "))
    if car_choice < 1 or car_choice > len(available_cars):
        print("Invalid choice, exiting the program.")
        return
    
    # Get chosen car details
    chosen_car_model, daily_rate = available_cars[car_choice - 1]
    
    # Create CarRental instance
    rental_id = "R123"
    agent_name = "Jane Smith"
    rental_price = daily_rate  # Assuming price is just the daily rate for simplicity
    rental = CarRental(rental_id, agent_name, rental_price, daily_rate, chosen_car_model)
    
    # Assign customer to rental if eligible
    if rental.assign_customer(customer):
        rental_duration = int(input(f"\nEnter rental duration (in days) for {chosen_car_model}: "))
        rental.rental_duration = rental_duration
        print("\nRental successfully assigned!")
        
        # Display rental information and total cost
        print("\nRental Information:")
        print(rental)
        print(f"Total rental cost: ${rental.calculate_total_cost():.2f}")
    else:
        print("\nRental assignment failed due to ineligibility.")

if __name__ == "__main__":
    main()
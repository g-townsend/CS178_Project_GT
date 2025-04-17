import boto3

TABLE_NAME = "Vacation"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)


def add_vacation_spot():
     Newcity = input("What city would you like to add to your vacation list?: ")
     table.put_item(
            Item = { 
             'City': Newcity,
             'Cost': []
     }
    )
     print("adding your vacation spot")

def vacation_list(vacation_dict):
    # print out the values of the movie dictionary
    print("City: ", vacation_dict["City"])
    print("Cost: ", vacation_dict.get("Cost"))
    print()
    
def print_entire_list():
    response = table.scan() #get all of the movies
    for city in response["Items"]:
        vacation_list(city)


def update_vacationspot():
    try:
     newspot=input("What is the vacation spot you would like to update? ")
     addcost = int(input("What is the average cost for a 5 day trip? : "))
    
     table.update_item(
            Key = {"City": newspot}, 
            UpdateExpression = "SET Cost = list_append(Cost, :r)", ExpressionAttributeValues = {':r': [addcost],}
     )
    except ValueError: 
        print("Error in adding cost to vacation spot. Please enter a numeric value.")


def delete_vacationspot():
    remove = input("What vacation spot would you like to remove from the database?: ")
    table.delete_item( 
        Key = {
            'City': remove
        }
    )
    print("deleting city")

def query_vacationspot():
    search = input("What vacation spot are you looking for?: ")
    response = table.get_item(
        Key = {
            'City' : search 
        }
    )
    if "Item" not in response: 
        print ("City not found")
    else: 
        findcity = response.get("Item")
        city_cost = findcity.get("Cost") 
        print ("The cost for your vacation to", search, "is", city_cost)
           # print (average)
    print("query vacation spot")
    
def print_menu():
    print("----------------------------")
    print("Press C: to CREATE a vacation spot")
    print("Press R: to READ vacation list")
    print("Press U: to ADD a cost to a vacation spot")
    print("Press D: to DELETE a vacation spot")
    print("Press Q: to Query a vacation's spot cost for a 5 day trip")
    print("Press X: to EXIT application")
    print("----------------------------")


def main():
    input_char = ""
    while input_char.upper() != "X":
        print_menu()
        input_char = input("Choice: ").strip()
        if input_char.upper() == "C":
            add_vacation_spot()
        elif input_char.upper() == "R":
            print_entire_list()
        elif input_char.upper() == "U":
            update_vacationspot()
        elif input_char.upper() == "D":
            delete_vacationspot()
        elif input_char.upper() == "Q":
            query_vacationspot()
        elif input_char.upper() == "X":
            print("exiting...")
        else:
            print('Not a valid option. Try again.')
main()
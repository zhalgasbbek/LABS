import json

# Load JSON data from file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Extract relevant information
interface_data = data['imdata']

# Print header
print("Interface Status")
print("=" * 80)
print("{:<52} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Iterate over interface data
for interface in interface_data:
    attributes = interface['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')

    # Print interface information
    print("{:<52} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))

print("=" * 80)

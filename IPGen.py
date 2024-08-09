import random

def generate_octet():
    """
    Generates a random number between 0 and 255,
    representing an octet in an IPv4 address.
    """
    return random.randint(0, 255)

def generate_ip():
    """
    Generates a random IPv4 address by concatenating four octets.

    Returns:
        str: A string representation of the IPv4 address.
    """
    return f"{generate_octet()}.{generate_octet()}.{generate_octet()}.{generate_octet()}"

def generate_multiple_ips(count):
    """
    Generates a specified number of random IPv4 addresses.

    Args:
        count (int): The number of IP addresses to generate.

    Returns:
        list: A list of randomly generated IPv4 addresses.
    """
    ips = [generate_ip() for _ in range(count)]
    return ips

def main():
    try:
        count = int(input("Enter the number of IP addresses to generate: "))
        if count <= 0:
            raise ValueError("The number of IP addresses must be a positive integer.")

        ip_addresses = generate_multiple_ips(count)
        
        print(f"\nGenerated {count} IP address(es):")
        for idx, ip in enumerate(ip_addresses, 1):
            print(f"{idx}. {ip}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()

def create_namespace_dict():
    # Initialize an empty namespace dictionary
    namespace_dict = {}

    # Define standard and reserved prefixes
    standard_prefixes = ["xml", "xmlns", "xsi", "xsd", "html"]
    reserved_prefixes = ["ns", "ns0", "ns1", "ns2", "ns3"]

    # Prompt the user to input prefixes and their corresponding URIs
    while True:
        prefix = input("Enter a prefix (or 'q' to quit): ")
        if prefix == "q":
            break
        uri = input("Enter the corresponding URI: ")

        # Check if the prefix is a standard or reserved prefix
        if prefix in standard_prefixes or prefix in reserved_prefixes:
            print("This prefix is reserved. Please choose a different prefix.")
        else:
            # Add prefix/URI pair to the namespace dictionary
            namespace_dict[prefix] = uri

    # Return the namespace dictionary
    return namespace_dict

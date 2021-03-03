def show_the_sandwich(*sandwiches_components):
        """
        Show the components of the sandwich
        """
        print("The components of the sandwhich are: ")
        for sandwiches_component in sandwiches_components:
            print(f"\t-{sandwiches_component}")


show_the_sandwich('bread')
print()
show_the_sandwich('bread', 'cheese', 'cucumber', 'mushrooms')
print()
show_the_sandwich('bread', 'cheese')

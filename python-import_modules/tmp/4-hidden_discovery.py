if __name__ == "__main__":
    import hidden_4
    for value in dir(hidden_4):
        if value[:2] != ("__"):
            print(value)

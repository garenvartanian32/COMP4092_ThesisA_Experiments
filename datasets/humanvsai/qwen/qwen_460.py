def do_command(self):
    command = self.command
    args = self.args
    if command == 'add':
        self.add(args)
    elif command == 'subtract':
        self.add(args, subtract=True)
    elif command == 'multiply':
        self.multiply(args)
    elif command == 'divide':
        self.divide(args)
    elif command == 'power':
        self.power(args)
    elif command == 'sqrt':
        self.sqrt(args)
    elif command == 'log':
        self.log(args)
    elif command == 'sin':
        self.sin(args)
    elif command == 'cos':
        self.cos(args)
    elif command == 'tan':
        self.tan(args)
    elif command == 'exit':
        self.exit()
    else:
        print('Unknown command')
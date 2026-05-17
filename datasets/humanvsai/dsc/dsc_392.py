from Redy.Collections import Flow, Traversal

x = [1, 1, 2]
result = Flow(x)[Traversal.group].unbox()

print(result)
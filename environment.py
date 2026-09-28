class EnvironmentError(RuntimeError):
    """Base class for NovaLang environment/runtime lookup errors."""


class UndefinedVariableError(EnvironmentError):
    """Raised when a variable is read or assigned before it exists."""


class Environment:
    """A lexical environment mapping variable names to runtime values.

    Each block can create a child Environment. Lookup and assignment walk
    through parent environments so a loop can update a variable declared
    outside the loop.
    """

    def __init__(self, parent=None):
        self.values = {}
        self.parent = parent

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name in self.values:
            return self.values[name]
        if self.parent is not None:
            return self.parent.get(name)
        raise UndefinedVariableError(f"Undefined variable '{name}'")

    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
            return
        if self.parent is not None:
            self.parent.assign(name, value)
            return
        raise UndefinedVariableError(f"Undefined variable '{name}'")

from dataclasses import dataclass
from typing import List


class ASTNode:
    """Base class for all NovaLang AST nodes."""

    def pretty(self, indent=0):
        raise NotImplementedError


@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode]

    def pretty(self, indent=0):
        lines = [" " * indent + "ProgramNode"]

        for statement in self.statements:
            lines.append(statement.pretty(indent + 2))

        return "\n".join(lines)


@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode]

    def pretty(self, indent=0):
        lines = [" " * indent + "ProgramNode"]

        for statement in self.statements:
            lines.append(statement.pretty(indent + 2))

        return "\n".join(lines)

@dataclass
class NumberNode(ASTNode):
    value: str

    def pretty(self, indent=0):
        return " " * indent + f"NumberNode({self.value})"

@dataclass
class VariableNode(ASTNode):
    name: str

    def pretty(self, indent=0):
        return " " * indent + f"VariableNode({self.name})"

@dataclass
class BinaryOpNode(ASTNode):
    operator: str
    left: ASTNode
    right: ASTNode

    def pretty(self, indent=0):
        lines = [
            " " * indent + f"BinaryOpNode({self.operator})",
            self.left.pretty(indent + 2),
            self.right.pretty(indent + 2),
        ]

        return "\n".join(lines)


@dataclass
class UnaryOpNode(ASTNode):
    operator: str
    operand: ASTNode

    def pretty(self, indent=0):
        lines = [
            " " * indent + f"UnaryOpNode({self.operator})",
            self.operand.pretty(indent + 2),
        ]

        return "\n".join(lines)

@dataclass
class AssignmentNode(ASTNode):
    name: str
    value: ASTNode
    declaration: bool = False

    def pretty(self, indent=0):
        kind = "Declaration" if self.declaration else "Assignment"

        lines = [
            " " * indent + f"AssignmentNode({kind})",
            " " * (indent + 2) + f"VariableNode({self.name})",
            self.value.pretty(indent + 2),
        ]

        return "\n".join(lines)


@dataclass
class PrintNode(ASTNode):
    expression: ASTNode

    def pretty(self, indent=0):
        lines = [
            " " * indent + "PrintNode",
            self.expression.pretty(indent + 2),
        ]

        return "\n".join(lines)
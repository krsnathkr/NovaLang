from __future__ import annotations

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
class NumberNode(ASTNode):
    value: str

    def pretty(self, indent=0):
        return " " * indent + f"NumberNode({self.value})"


@dataclass
class BooleanNode(ASTNode):
    value: bool

    def pretty(self, indent=0):
        return " " * indent + f"BooleanNode({str(self.value).lower()})"


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


@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode]

    def pretty(self, indent=0):
        lines = [" " * indent + "BlockNode"]
        for statement in self.statements:
            lines.append(statement.pretty(indent + 2))
        return "\n".join(lines)


@dataclass
class IfNode(ASTNode):
    condition: ASTNode
    then_branch: BlockNode
    else_branch: BlockNode | None = None

    def pretty(self, indent=0):
        lines = [
            " " * indent + "IfNode",
            " " * (indent + 2) + "Condition",
            self.condition.pretty(indent + 4),
            " " * (indent + 2) + "Then",
            self.then_branch.pretty(indent + 4),
        ]
        if self.else_branch is not None:
            lines.append(" " * (indent + 2) + "Else")
            lines.append(self.else_branch.pretty(indent + 4))
        return "\n".join(lines)


@dataclass
class WhileNode(ASTNode):
    condition: ASTNode
    body: BlockNode

    def pretty(self, indent=0):
        lines = [
            " " * indent + "WhileNode",
            " " * (indent + 2) + "Condition",
            self.condition.pretty(indent + 4),
            " " * (indent + 2) + "Body",
            self.body.pretty(indent + 4),
        ]
        return "\n".join(lines)


# Part 5 AST nodes

@dataclass
class FunctionDefNode(ASTNode):
    name: str
    parameters: List[str]
    body: BlockNode

    def pretty(self, indent=0):
        lines = [
            " " * indent + f"FunctionDefNode({self.name})",
            " " * (indent + 2) + "Parameters: " + ", ".join(self.parameters),
            " " * (indent + 2) + "Body",
            self.body.pretty(indent + 4),
        ]
        return "\n".join(lines)


@dataclass
class FunctionCallNode(ASTNode):
    name: str
    arguments: List[ASTNode]

    def pretty(self, indent=0):
        lines = [
            " " * indent + f"FunctionCallNode({self.name})",
            " " * (indent + 2) + "Arguments",
        ]
        for argument in self.arguments:
            lines.append(argument.pretty(indent + 4))
        return "\n".join(lines)


@dataclass
class ReturnNode(ASTNode):
    expression: ASTNode

    def pretty(self, indent=0):
        lines = [
            " " * indent + "ReturnNode",
            self.expression.pretty(indent + 2),
        ]
        return "\n".join(lines)

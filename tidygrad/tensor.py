# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_tensor.ipynb.

# %% auto 0
__all__ = ['Tensor', 'AddTensor', 'SubTensor', 'MulTensor', 'MatMulTensor', 'SumTensor', 'SigmoidTensor', 'ReluTensor',
           'LogTensor', 'BroadcastTensor']

# %% ../nbs/01_tensor.ipynb 3
import numpy as np

# %% ../nbs/01_tensor.ipynb 4
def calculate_target_shape(s1, s2):
    """Calculate the target shape for broadcasting two tensors"""

    # expand shaped to be the same length. Note (1,) * <negative> is empty
    s2 = (1,) * (len(s1) - len(s2)) + s2
    s1 = (1,) * (len(s2) - len(s1)) + s1

    out_shape = ()
    for dims in list(zip(reversed(s1), reversed(s2))):
        if dims[0] != 1 and dims[1] != 1 and dims[0] != dims[1]:
            raise ValueError(f"Cannot broadcast {s1} and {s2}")
        out_shape = (max(dims),) + out_shape

    return out_shape

# %% ../nbs/01_tensor.ipynb 5
def maybe_broadcast_elementwise(a, b):
    """Broadcast two tensors if they have different shapes"""
    if a.data.shape != b.data.shape:
        target_shape = calculate_target_shape(a.data.shape, b.data.shape)
        # print(
        #     f"Elementwise broadcasted {a.data.shape} and {b.data.shape} to {target_shape}"
        # )
        a = a.broadcast(target_shape)
        b = b.broadcast(target_shape)

    return a, b


def maybe_broadcast_matmul(a, b):
    """Broadcast two tensors if they have different shapes, except for the last two dimensions"""

    a_short_shape = a.data.shape[:-2]
    b_short_shape = b.data.shape[:-2]

    if a_short_shape != b_short_shape:
        target_shape = calculate_target_shape(a_short_shape, b_short_shape)
        print(
            f"Matmul broadcasted {a.data.shape} and {b.data.shape} to {target_shape + a.data.shape[-2:]}"
        )
        a = a.broadcast(target_shape + a.data.shape[-2:])
        b = b.broadcast(target_shape + b.data.shape[-2:])

    return a, b

# %% ../nbs/01_tensor.ipynb 6
class Tensor:
    op = "L"
    name: str = ""
    parents: list = []

    def __init__(self, data, name=""):
        self.data = data
        self.name = name
        self.grad = np.zeros_like(self.data)

    def broadcast(self, target_shape):
        self_shape = self.data.shape
        if self_shape == target_shape:
            return self

        if len(self_shape) < len(target_shape):
            expanded_shape = (len(target_shape) - len(self_shape)) * (1,) + self_shape
        else:
            expanded_shape = self_shape

        final_shape = ()
        broadcasted_dims = ()

        for s_expanded, s_target in reversed(list(zip(expanded_shape, target_shape))):
            if s_expanded != s_target:
                if s_expanded != 1:
                    raise ValueError(f"Cannot broadcast {self_shape} to {target_shape}")
                else:
                    broadcasted_dims = (True,) + broadcasted_dims
                    final_shape = (s_target,) + final_shape

            else:
                broadcasted_dims = (False,) + broadcasted_dims
                final_shape = (s_expanded,) + final_shape

        broadcasted_data = np.broadcast_to(self.data, final_shape)

        assert final_shape == broadcasted_data.shape

        out = BroadcastTensor(data=broadcasted_data, name=self.name + "_broadcasted")
        out.parents = [self]
        out.broadcasted_dims = broadcasted_dims
        return out

    # Elementwise operations
    def add(self, other, name="Noname"):
        a, b = maybe_broadcast_elementwise(self, other)

        out = AddTensor(data=a.data + b.data, name=name)
        out.parents = [a, b]
        return out

    def sub(self, other, name="Noname"):
        a, b = maybe_broadcast_elementwise(self, other)
        out = SubTensor(data=a.data - b.data, name=name)
        out.parents = [a, b]
        return out

    def neg(self, name="Noname"):
        zero_tensor = Tensor(data=np.zeros_like(self.data), name="zero")
        out = zero_tensor.sub(self, name)
        out.parents = [zero_tensor, self]
        return out

    def mul(self, other, name="Noname"):
        a, b = maybe_broadcast_elementwise(self, other)
        out = MulTensor(data=a.data * b.data, name=name)
        out.parents = [a, b]
        return out

    def log(self, name="Noname"):
        out = LogTensor(data=np.log(self.data), name=name)
        out.parents = [self]
        return out

    def sigmoid(self, name="Noname"):
        out = SigmoidTensor(data=1 / (1 + np.exp(-self.data)), name=name)
        out.parents = [self]
        return out

    def relu(self, name="Noname"):
        out = ReluTensor(data=np.maximum(0, self.data), name=name)
        out.parents = [self]
        return out

    # Matrix operations
    def mmul(self, other, name="Noname"):
        a, b = maybe_broadcast_matmul(self, other)
        # a, b = self, other
        out = MatMulTensor(data=np.matmul(a.data, b.data), name=name)
        out.parents = [a, b]
        return out

    # Reduction operations
    def sum(self, name="Noname"):
        out = SumTensor(data=self.data.sum(), name=name)
        out.parents = [self]
        return out

    def backward(self):
        # Create a list of all parent nodes, in reverse order
        # Start with the current node
        visited = []
        nodes = []

        def walk(node):
            for p in node.parents:
                if p not in visited:
                    visited.append(p)
                    walk(p)
                    nodes.append(p)

        walk(self)
        nodes.append(self)

        # print(nodes)
        self.grad = np.ones_like(self.data)
        for n in nodes[::-1]:
            if hasattr(n, "_backward"):
                n._backward()

    def __repr__(self):
        value_repr = repr(self.data)
        if "\n" in value_repr:
            res = (
                f"\n{self.name}=\n{str(self.data)}\n{self.name}.grad=\n{str(self.grad)}"
            )
        else:
            res = f"{self.name}={str(self.data)} {self.name}.grad={str(self.grad)}"

        if self.parents:
            res += (
                f" {self.name}.parents=["
                + ",".join([p.name for p in self.parents])
                + "]"
            )

        return f"Tensor(shape=[{self.data.shape}])] op={self.op or ''} {res}"


class AddTensor(Tensor):
    op = "+"

    def _backward(self):
        self.parents[0].grad += self.grad
        self.parents[1].grad += self.grad


class SubTensor(Tensor):
    op = "-"

    def _backward(self):
        self.parents[0].grad += self.grad
        self.parents[1].grad -= self.grad


class MulTensor(Tensor):
    op = "*"

    def _backward(self):
        self.parents[0].grad += self.grad * self.parents[1].data
        self.parents[1].grad += self.grad * self.parents[0].data


class MatMulTensor(Tensor):
    op = "@"

    def _backward(self):
        # print(self.grad)
        self.parents[0].grad += np.matmul(self.grad, self.parents[1].data.T)
        self.parents[1].grad += np.matmul(self.parents[0].data.T, self.grad)


class SumTensor(Tensor):
    op = "sum"

    def _backward(self):
        self.parents[0].grad += self.grad


class SigmoidTensor(Tensor):
    op = "sigmoid"

    def _backward(self):
        self.parents[0].grad += self.grad * self.data * (1 - self.data)


class ReluTensor(Tensor):
    op = "relu"

    def _backward(self):
        self.parents[0].grad += self.grad * (self.data > 0)


class LogTensor(Tensor):
    op = "log"

    def _backward(self):
        self.parents[0].grad += self.grad * (1 / self.data)


class BroadcastTensor(Tensor):
    op = "broadcast"

    def _backward(self):
        axis = tuple([i for i, dim in enumerate(self.broadcasted_dims) if dim])
        summed = self.grad.sum(axis=axis, keepdims=True)

        if summed.shape != self.parents[0].data.shape:
            summed = summed.reshape(self.parents[0].data.shape)

        self.parents[0].grad += summed

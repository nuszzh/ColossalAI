from typing import Dict, List

from ..sharding_strategy import OperationData, OperationDataType
from .node_handler import NodeHandler
from .strategy import PlaceholderGenerator, StrategyGenerator

__all__ = ['PlacehodlerHandler']


class PlacehodlerHandler(NodeHandler):
    """
    A PlacehodlerHandler which deals with the sharding strategies for Placeholder Node.
    """

    def get_strategy_generator(self) -> List[StrategyGenerator]:
        op_data_mapping = self.get_operation_data_mapping()
        generators = []
        generators.append(PlaceholderGenerator(op_data_mapping, self.device_mesh))
        return generators

    def get_operation_data_mapping(self) -> Dict[str, OperationData]:
        # use transposed shape for strategies
        # the strategies will be transformed back to its original shape in self.post_process
        physical_output = OperationData(name=str(self.node), type=OperationDataType.OUTPUT, data=self.node._meta_data)

        mapping = {"output": physical_output}

        return mapping

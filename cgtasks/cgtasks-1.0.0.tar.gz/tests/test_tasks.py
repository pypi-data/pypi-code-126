from unittest import TestCase
from MarkLib.models.base import BinTreeNode, Region, Point
from MarkLib.models.condition import PointListAndRegionCondition, PointListCondition
from graham.model import GrahamCenterPointCell, GrahamPiCompareCell, GrahamPoint, GrahamPointList, GrahamTable, GrahamTableRow, GrahamToAddCell, GrahamTrinityCell, PiCompare, ToAddGraham
from kd_tree.model import Intersection, KdTree, KdTreeInterscetionCell, KdTreeOrderedLists, KdTreePartitionCell, KdTreePartitionTable, KdTreePartitionTableRow, KdTreePoint, KdTreePointCell, KdTreeSearchTable, KdTreeSearchTableRow, KdTreeToAddCell, Partition, ToAddKdTree
from quickhull.model import QuickhullInitialPartition, QuickhullNodeData, QuickhullPartition, QuickhullPoint, QuickhullTree, QuickhullTreeNode
from graham.task import GrahamTask
from kd_tree.task import KdTreeTask
from quickhull.task import QuickhullTask


class TestTasks(TestCase):
    def test_graham(self):
        task = GrahamTask(PointListCondition(point_list=[
            Point(x=6, y=4),
            Point(x=4, y=2),
            Point(x=4, y=0),
            Point(x=1, y=0),
            Point(x=3, y=2),
            Point(x=2, y=4)
        ]))
        centroid = GrahamPoint(x=4.666666666666667, y=2.0)
        ordered = GrahamPointList(points=[
            GrahamPoint(x=4, y=0),
            GrahamPoint(x=6, y=4),
            GrahamPoint(x=2, y=4),
            GrahamPoint(x=4, y=2),
            GrahamPoint(x=3, y=2),
            GrahamPoint(x=1, y=0)
        ])
        origin = GrahamPoint(x=4, y=0)
        steps = GrahamTable(rows=[
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[0], ordered.points[1], ordered.points[2])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[3])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[2]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[3], ordered.points[4])),
                GrahamPiCompareCell(content=PiCompare.more),
                GrahamCenterPointCell(content=ordered.points[3]),
                GrahamToAddCell(content=ToAddGraham.no)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[4])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[2]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[4], ordered.points[5])),
                GrahamPiCompareCell(content=PiCompare.more),
                GrahamCenterPointCell(content=ordered.points[4]),
                GrahamToAddCell(content=ToAddGraham.no)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[5])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[2]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[5], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[5]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
        ])
        
        self.assertAlmostEqual(task.stages[0].items[0].answer, centroid)
        self.assertEqual(task.stages[1].items[0].answer, ordered)
        self.assertEqual(task.stages[2].items[0].answer, origin)
        self.assertEqual(task.stages[3].items[0].answer, steps)

    def test_kd_tree(self):
        task = KdTreeTask(PointListAndRegionCondition(
            point_list=[
                Point(x=3, y=2),
                Point(x=5, y=1),
                Point(x=4, y=3),
                Point(x=7, y=3),
                Point(x=6, y=2)
            ],
            region=Region(x_range=(2, 5), y_range=(2, 4))
        ))

        ordered_x = [
            KdTreePoint(x=3, y=2),
            KdTreePoint(x=4, y=3),
            KdTreePoint(x=5, y=1),
            KdTreePoint(x=6, y=2),
            KdTreePoint(x=7, y=3)
        ]
        ordered_y = [
            KdTreePoint(x=5, y=1),
            KdTreePoint(x=3, y=2),
            KdTreePoint(x=6, y=2),
            KdTreePoint(x=4, y=3),
            KdTreePoint(x=7, y=3)
        ]
        ordered = KdTreeOrderedLists(ordered_x=ordered_x, ordered_y=ordered_y)
        partition_table = KdTreePartitionTable(rows=[
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[2]),
                KdTreePartitionCell(content=Partition.vertical)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[1]),
                KdTreePartitionCell(content=Partition.horizontal)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[0]),
                KdTreePartitionCell(content=Partition.vertical)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[4]),
                KdTreePartitionCell(content=Partition.horizontal)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[3]),
                KdTreePartitionCell(content=Partition.vertical)
            ))
        ])
        tree = KdTree(
            nodes=[
                BinTreeNode(data=ordered_x[2], left=ordered_x[1], right=ordered_x[4]),
                BinTreeNode(data=ordered_x[1], left=ordered_x[0], right=None),
                BinTreeNode(data=ordered_x[0], left=None, right=None),
                BinTreeNode(data=ordered_x[4], left=ordered_x[3], right=None),
                BinTreeNode(data=ordered_x[3], left=None, right=None),
            ],
            region=Region(x_range=(2, 5), y_range=(2, 4))
        )
        search_table = KdTreeSearchTable(rows=[
            KdTreeSearchTableRow(cells=(
                KdTreePointCell(content=ordered_x[2]),
                KdTreeToAddCell(content=ToAddKdTree.no),
                KdTreeInterscetionCell(content=Intersection.yes)
            )),
            KdTreeSearchTableRow(cells=(
                KdTreePointCell(content=ordered_x[1]),
                KdTreeToAddCell(content=ToAddKdTree.yes),
                KdTreeInterscetionCell(content=Intersection.yes)
            )),
            KdTreeSearchTableRow(cells=(
                KdTreePointCell(content=ordered_x[0]),
                KdTreeToAddCell(content=ToAddKdTree.yes),
                KdTreeInterscetionCell(content=Intersection.yes)
            ))
        ])

        self.assertEqual(task.stages[0].items[0].answer, ordered)
        self.assertEqual(task.stages[0].items[1].answer, partition_table)
        self.assertEqual(task.stages[1].items[0].answer, tree)
        self.assertEqual(task.stages[2].items[0].answer, search_table)
    
    def test_quickhull(self):
        pts = [QuickhullPoint(x=3, y=4), QuickhullPoint(x=0, y=0), QuickhullPoint(x=7, y=2)]
        task = QuickhullTask(PointListCondition(point_list=pts))
        
        min_point, max_point = pts[1], pts[2]
        s1, s2 = [pts[1], pts[0], pts[2]], [pts[2], pts[1]]
        s11, s12 = [pts[1], pts[0]], [pts[0], pts[2]]

        tree = QuickhullTree(nodes=[
            QuickhullTreeNode(
                data=QuickhullNodeData(points=s1, hull_piece=s1),
                left=QuickhullNodeData(points=s1, h=pts[0], hull_piece=s1),
                right=QuickhullNodeData(points=s2, hull_piece=s2)
            ),
            QuickhullTreeNode(
                data=QuickhullNodeData(points=s1, h=pts[0], hull_piece=s1),
                left=QuickhullNodeData(points=s11, hull_piece=s11),
                right=QuickhullNodeData(points=s12, hull_piece=s12)
            ),
            QuickhullTreeNode(
                data=QuickhullNodeData(points=s11, hull_piece=s11)
            ),
            QuickhullTreeNode(
                data=QuickhullNodeData(points=s12, hull_piece=s12)
            ),
            QuickhullTreeNode(
                data=QuickhullNodeData(points=s2, hull_piece=s2)
            )
        ])

        initial_partition = QuickhullInitialPartition(
            min_point=min_point,
            max_point=max_point,
            s1=s1,
            s2=s2
        )
        partition = QuickhullPartition(initial_partition=initial_partition, tree=tree)

        self.assertEqual(task.stages[0].items[0].answer, partition)
        self.assertEqual(task.stages[1].items[0].answer, tree)

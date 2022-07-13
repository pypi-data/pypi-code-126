from unittest import TestCase
from MarkLib.models.base import BinTreeNode, Point, PointList, Region
from graham.model import GrahamCenterPointCell, GrahamPiCompareCell, GrahamTable, GrahamTableRow, GrahamToAddCell, GrahamTrinityCell, PiCompare, ToAddGraham
from kd_tree.model import Intersection, KdTree, KdTreeInterscetionCell, KdTreeOrderedLists, KdTreePartitionCell, KdTreePartitionTable, KdTreePartitionTableRow, KdTreePoint, KdTreePointCell, KdTreeSearchTable, KdTreeSearchTableRow, KdTreeToAddCell, Partition, ToAddKdTree
from quickhull.model import QuickhullInitialPartition, QuickhullNodeData, QuickhullPartition, QuickhullPoint, QuickhullTree, QuickhullTreeNode
from graham.grader import GrahamGrader, ItemMarkData
from kd_tree.grader import KdTreeGrader
from quickhull.grader import QuickhullGrader


class TestGraders(TestCase):
    def test_graham_grader(self):
        centroid = Point(x=3.3333333333333335, y=1.0)
        ordered = PointList(points=[Point(x=7, y=0), Point(x=3, y=3), Point(x=0, y=0)])
        origin = Point(x=7, y=0)
        steps_table = GrahamTable(rows=[
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[0], ordered.points[1], ordered.points[2])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.yes)
            ))
        ])

        # Center point in last triple is deleted, not added
        answer_steps_table = GrahamTable(rows=[
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[0], ordered.points[1], ordered.points[2])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.no)
            ))
        ])

        correct = [
            centroid,
            ordered,
            origin,
            steps_table
        ]
        answer = [
            centroid,
            ordered,
            origin,
            answer_steps_table
        ]
        mark = GrahamGrader.grade(correct, answer)
        self.assertEqual(mark[0], 1.75)
        markdata = [
            (ItemMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (ItemMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (ItemMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (ItemMarkData(max_mark=1.25, min_mark=0), 1.0)
        ]
        self.assertEqual(mark[1], markdata)
    
    def test_quickhull_grader(self):
        pts = [QuickhullPoint(x=3, y=4), QuickhullPoint(x=0, y=0), QuickhullPoint(x=7, y=2)]
        
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

        # Right-most leaf not included
        answer_tree = QuickhullTree(nodes=[
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
            )
        ])

        correct = [partition, tree]
        answer = [partition, answer_tree]

        mark = QuickhullGrader.grade(correct, answer)
        self.assertEqual(mark[0], 1.0)
        markdata = [
            (ItemMarkData(max_mark=1.0, min_mark=0), 1.0),
            (ItemMarkData(max_mark=1.0, min_mark=0), 0.0)
        ]
        self.assertEqual(mark[1], markdata)
    
    def test_kd_tree_grader(self):
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
            )),
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

        # Partition types tweaked to opposite
        answer_partition_table = KdTreePartitionTable(rows=[
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[2]),
                KdTreePartitionCell(content=Partition.horizontal)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[1]),
                KdTreePartitionCell(content=Partition.vertical)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[0]),
                KdTreePartitionCell(content=Partition.horizontal)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[4]),
                KdTreePartitionCell(content=Partition.vertical)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered_x[3]),
                KdTreePartitionCell(content=Partition.horizontal)
            ))
        ])

        correct = [ordered, partition_table, tree, search_table]
        answer = [ordered, answer_partition_table, tree, search_table]

        mark = KdTreeGrader.grade(correct, answer)
        self.assertEqual(mark[0], 2.25)
        markdata = [
            (ItemMarkData(max_mark=0.25, min_mark=0), 0.25),
            (ItemMarkData(max_mark=0.75, min_mark=0), 0.0),
            (ItemMarkData(max_mark=1.0, min_mark=0), 1.0),
            (ItemMarkData(max_mark=1.0, min_mark=0), 1.0)
        ]
        self.assertEqual(mark[1], markdata)

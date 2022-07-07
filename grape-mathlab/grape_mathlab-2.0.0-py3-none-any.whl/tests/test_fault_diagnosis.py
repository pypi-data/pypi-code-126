"""TestFaultDiagnosis to check FaultDiagnosis"""

from unittest import TestCase
import numpy as np
from grape.fault_diagnosis import FaultDiagnosis


def test_closeness_centrality_after_element_perturbation():
    """
    The following test checks the closeness centrality after a perturbation.
    The perturbation here considered is the perturbation of element '1'.
    """
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    clo_cen_after_element_perturbation = {
        '2': 0,
        '3': 0,
        '4': 0.058823529411764705,
        '5': 0.058823529411764705,
        '6': 0.18823529411764706,
        '7': 0.11764705882352941,
        '8': 0.11764705882352941,
        '9': 0.15126050420168066,
        '10': 0.12538699690402477,
        '11': 0.1660899653979239,
        '12': 0.1859114015976761,
        '13': 0.16020025031289112,
        '14': 0.1859114015976761,
        '15': 0,
        '16': 0.1711229946524064,
        '17': 0.12981744421906694,
        '18': 0.17346938775510204,
        '19': 0.22145328719723184
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(clo_cen_after_element_perturbation.values())),
        np.asarray(sorted(F.G.closeness_centrality.values())),
        err_msg="FINAL CLOSENESS CENTRALITY failure: perturbation of element 1")

def test_closeness_centrality_after_element_perturbation_parallel():
    """
    The following test checks the closeness centrality after a perturbation.
    The perturbation here considered is the perturbation of element '1'.
    This time, in FaultDiagnosis class we set parallel flag as True.
    """
    F = FaultDiagnosis("tests/TOY_graph.csv", parallel=True)
    F.simulate_element_perturbation(["1"])

    clo_cen_after_element_perturbation = {
        '2': 0,
        '3': 0,
        '4': 0.058823529411764705,
        '5': 0.058823529411764705,
        '6': 0.18823529411764706,
        '7': 0.11764705882352941,
        '8': 0.11764705882352941,
        '9': 0.15126050420168066,
        '10': 0.12538699690402477,
        '11': 0.1660899653979239,
        '12': 0.1859114015976761,
        '13': 0.16020025031289112,
        '14': 0.1859114015976761,
        '15': 0,
        '16': 0.1711229946524064,
        '17': 0.12981744421906694,
        '18': 0.17346938775510204,
        '19': 0.22145328719723184
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(clo_cen_after_element_perturbation.values())),
        np.asarray(sorted(F.G.closeness_centrality.values())),
        err_msg="FINAL CLOSENESS CENTRALITY failure: perturbation of element 1")

def test_degree_centrality_after_element_perturbation():
    """
    The following test checks the degree centrality after a perturbation.
    The perturbation here considered is the perturbation of element '1'.
    """
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    deg_cen_after_element_perturbation = {
        '2': 0.058823529411764705,
        '3': 0.058823529411764705,
        '4': 0.11764705882352941,
        '5': 0.11764705882352941,
        '6': 0.29411764705882354,
        '7': 0.11764705882352941,
        '8': 0.17647058823529413,
        '9': 0.17647058823529413,
        '10': 0.11764705882352941,
        '11': 0.17647058823529413,
        '12': 0.23529411764705882,
        '13': 0.23529411764705882,
        '14': 0.29411764705882354,
        '15': 0.058823529411764705,
        '16': 0.17647058823529413,
        '17': 0.17647058823529413,
        '18': 0.058823529411764705,
        '19': 0.29411764705882354
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(deg_cen_after_element_perturbation.values())),
        np.asarray(sorted(F.G.degree_centrality.values())),
        err_msg="FINAL DEGREE CENTRALITY failure: perturbation of element 1")

def test_indegree_centrality_after_element_perturbation():
    """
    The following test checks the indegree centrality after a perturbation.
    The perturbation here considered is the perturbation of element '1'.
    """
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    indeg_cen_after_element_perturbation = {
        '2': 0.0,
        '3': 0.0,
        '4': 0.058823529411764705,
        '5': 0.058823529411764705,
        '6': 0.17647058823529413,
        '7': 0.058823529411764705,
        '8': 0.058823529411764705,
        '9': 0.11764705882352941,
        '10': 0.058823529411764705,
        '11': 0.11764705882352941,
        '12': 0.11764705882352941,
        '13': 0.11764705882352941,
        '14': 0.11764705882352941,
        '15': 0.0,
        '16': 0.11764705882352941,
        '17': 0.058823529411764705,
        '18': 0.058823529411764705,
        '19': 0.17647058823529413
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(indeg_cen_after_element_perturbation.values())),
        np.asarray(sorted(F.G.indegree_centrality.values())),
        err_msg="FINAL INDEGREE CENTRALITY failure: perturbation of element 1")

def test_outdegree_centrality_after_element_perturbation():
    """
    The following test checks the outdegree centrality after a perturbation.
    The perturbation here considered is the perturbation of element '1'.
    """
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    outdeg_cen_after_element_perturbation = {
        '2': 0.058823529411764705,
        '3': 0.058823529411764705,
        '4': 0.058823529411764705,
        '5': 0.058823529411764705,
        '6': 0.11764705882352941,
        '7': 0.058823529411764705,
        '8': 0.11764705882352941,
        '9': 0.058823529411764705,
        '10': 0.058823529411764705,
        '11': 0.058823529411764705,
        '12': 0.11764705882352941,
        '13': 0.11764705882352941,
        '14': 0.17647058823529413,
        '15': 0.058823529411764705,
        '16': 0.058823529411764705,
        '17': 0.11764705882352941,
        '18': 0.0,
        '19': 0.11764705882352941
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(outdeg_cen_after_element_perturbation.values())),
        np.asarray(sorted(F.G.outdegree_centrality.values())),
        err_msg="FINAL OUTDEGREE CENTRALITY failure: perturbation of element 1")

def test_nodal_efficiency_after_element_perturbation():
    """
	The following test checks the nodal efficiency after a perturbation.
	The perturbation here considered is the perturbation of element '1'.
	"""
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    nodal_eff_after_element_perturbation = {
        '2': 0.20847763347763348,
        '3': 0.1607843137254902,
        '4': 0.21412231559290384,
        '5': 0.1568627450980392,
        '6': 0.2391223155929038,
        '7': 0.18471055088702149,
        '8': 0.2638655462184874,
        '9': 0.17072829131652661,
        '10': 0.1568627450980392,
        '11': 0.1568627450980392,
        '12': 0.16666666666666666,
        '13': 0.17647058823529413,
        '14': 0.20588235294117646,
        '15': 0.17563025210084035,
        '16': 0.16568627450980392,
        '17': 0.21960784313725493,
        '18': 0.0,
        '19': 0.17647058823529413
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(nodal_eff_after_element_perturbation.values())),
        np.asarray(sorted(F.G.nodal_efficiency.values())),
        err_msg="FINAL NODAL EFFICIENCY failure: perturbation of element 1")

def test_local_efficiency_after_element_perturbation():
    """
	The following test checks the local efficiency after a perturbation.
	The perturbation here considered is the perturbation of element '1'.
	"""
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    local_eff_after_element_perturbation = {
        '2': 0.21412231559290384,
        '3': 0.1568627450980392,
        '4': 0.2391223155929038,
        '5': 0.1568627450980392,
        '6': 0.22428804855275444,
        '7': 0.2391223155929038,
        '8': 0.2049253034547152,
        '9': 0.16568627450980392,
        '10': 0.1568627450980392,
        '11': 0.17647058823529413,
        '12': 0.17647058823529413,
        '13': 0.18627450980392157,
        '14': 0.11764705882352942,
        '15': 0.17072829131652661,
        '16': 0.21960784313725493,
        '17': 0.16127450980392155,
        '18': 0.0,
        '19': 0.18627450980392157
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(local_eff_after_element_perturbation.values())),
        np.asarray(sorted(F.G.local_efficiency.values())),
        err_msg="FINAL LOCAL EFFICIENCY failure: perturbation of element 1")

def test_global_efficiency_after_element_perturbation():
    """
    The following test checks the nodal efficiency after a perturbation.
    The perturbation here considered is the perturbation of element '1'.
    """
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    np.testing.assert_almost_equal(F.G.global_efficiency, 0.17771187599618973,
        err_msg="FINAL GLOBAL EFFICIENCY failure: perturbation of element 1")

def test_residual_service_after_element_perturbation():
    """
    The following test checks the residual service after a perturbation.
    The perturbation here considered is the perturbation of element '1'.
    """
    F = FaultDiagnosis("tests/TOY_graph.csv")
    F.simulate_element_perturbation(["1"])

    res_service_after_element_perturbation = {
        '2': 0.0,
        '3': 0.0,
        '4': 0.0,
        '5': 0.0,
        '6': 0.0,
        '7': 0.0,
        '8': 0.0,
        '9': 0.0,
        '10': 0.0,
        '11': 0.0,
        '12': 0.0,
        '13': 0.0,
        '14': 0.0,
        '15': 0.0,
        '16': 0.0,
        '17': 0.0,
        '18': 2.0,
        '19': 0.0
    }

    np.testing.assert_array_almost_equal(
        np.asarray(sorted(res_service_after_element_perturbation.values())),
        np.asarray(sorted(F.G.service.values())),
        err_msg="FINAL RESIDUAL SERVICE failure: perturbation of element 1")

class Test_FD(TestCase):
    """
    Class Test_FD to check other FaultDiagnosis attributes.
    """

    def test_check_input_with_gephi_mark(self):
        """
        The following test checks mark attribute of edges_df member
        of FaultDiagnosis class.
        """
        F = FaultDiagnosis("tests/TOY_graph.csv")
        F.check_input_with_gephi()
        edges_dict = F.edges_df.to_dict()

        mark_dict = {
            1: '2',
            2: '3',
            3: '4',
            4: '5',
            5: '6',
            6: '6',
            7: '7',
            8: '8',
            9: '6',
            10: '9',
            11: '9',
            13: '16',
            14: '16',
            15: '17',
            16: '10',
            17: '11',
            18: '11',
            19: '19',
            20: '19',
            21: '19',
            22: '12',
            23: '12',
            24: '13',
            25: '13',
            26: '14',
            27: '14',
            28: '18'
        }

        self.assertDictEqual(
            mark_dict,
            edges_dict['mark'],
            msg="MARK failure: check_input_with_gephi function")

    def test_check_input_with_gephi_father_mark(self):
        """
        The following test checks father_mark attribute of edges_df member
        of FaultDiagnosis class.
        """
        F = FaultDiagnosis("tests/TOY_graph.csv")
        F.check_input_with_gephi()
        edges_dict = F.edges_df.to_dict()

        father_mark_dict = {
            1: '1',
            2: '1',
            3: '2',
            4: '3',
            5: '4',
            6: '7',
            7: '6',
            8: '6',
            9: '8',
            10: '8',
            11: '15',
            13: '9',
            14: '17',
            15: '16',
            16: '17',
            17: '10',
            18: '5',
            19: '11',
            20: '12',
            21: '14',
            22: '19',
            23: '13',
            24: '14',
            25: '12',
            26: '19',
            27: '13',
            28: '14'
        }

        self.assertDictEqual(
            father_mark_dict,
            edges_dict['father_mark'],
            msg="FATHER MARK failure: check_input_with_gephi function")

    def test_mark_status_after_element_perturbation(self):
        """
        The following test checks mark_status attribute after a perturbation.
        The perturbation here considered is the perturbation of element '1'.
        """
        F = FaultDiagnosis("tests/TOY_graph.csv")
        F.simulate_element_perturbation(["1"])

        mark_status_after_element_perturbation = {
            '2': 'ACTIVE',
            '3': 'ACTIVE',
            '4': 'ACTIVE',
            '5': 'ACTIVE',
            '6': 'ACTIVE',
            '7': 'ACTIVE',
            '8': 'ACTIVE',
            '9': 'ACTIVE',
            '10': 'ACTIVE',
            '11': 'ACTIVE',
            '12': 'ACTIVE',
            '13': 'ACTIVE',
            '14': 'ACTIVE',
            '15': 'ACTIVE',
            '16': 'ACTIVE',
            '17': 'ACTIVE',
            '18': 'ACTIVE',
            '19': 'ACTIVE'
        }

        self.assertDictEqual(
            mark_status_after_element_perturbation,
            F.G.mark_status,
            msg="FINAL MARK STATUS failure: perturbation of element 1")
